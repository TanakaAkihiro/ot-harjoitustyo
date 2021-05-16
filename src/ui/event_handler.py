import sys
import pygame


class EventHandler:
    def handle_menu_events(self, event_queue, renderer, gameloop):
        ''' Käsittelee näppäimistön tapahtumia alkunäkymässä
        Args:
            event_queue: EventQueue-olio
            renderer: Renderer-olio
            gameloop: Gameloop-olio
        
        Returns:
            score eli pelikierroksen tuloksen kokonaislukuna
            "DELETE", kun käyttäjä haluaa poistaa tietokannan tiedot
            None muulloin 
        '''

        while True:
            event = event_queue.get()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score = gameloop.start()
                    return score

                if event.key == pygame.K_1:
                    renderer.show_game_rules()
                    while True:
                        event = event_queue.get()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                return
                        elif event.type == pygame.QUIT:
                            sys.exit()

                if event.key == pygame.K_2:
                    renderer.show_control_options()
                    while True:
                        event = event_queue.get()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                return
                        elif event.type == pygame.QUIT:
                            sys.exit()

                if event.key == pygame.K_3:
                    renderer.show_high_scores()
                    while True:
                        event = event_queue.get()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                return
                            if event.key == pygame.K_d:
                                return "DELETE"
                        elif event.type == pygame.QUIT:
                            sys.exit()

            elif event.type == pygame.QUIT:
                exit()

    def ensure_deleting(self, renderer, event_queue):
        '''Varmistaa pelaajalta, haluaako pelaaja oikeasti poistaa tietokannan tiedot
        '''
        renderer.ensure_deleting()
        
        while True:
            event = event_queue.get()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                if event.key == pygame.K_n:
                    return False


    def handle_game_events(self, event_queue, renderer, field, block, emptied_rows):
        '''Käsittelee näppäimistön tapahtumia pelin aikana

        Args:
            event_queue: EventQueue-olio
            renderer: Renderer-olio
            field: Field-olio
            block: Block-olio (laskeutuva palikka)
            emptied_rows: Tyhjennettyjen rivien määrä

        Returns:
            True, jos laskeutuva palikka on laskeutunut ja halutaan luoda uusi palikka.
            False, jos käyttäjä keskeyttää sovelluksen ajamisen.
            None muulloin.
        '''

        event = event_queue.get()
        boolean = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if block.movable(field.get_field(), (0, -1)):
                    block.move((0, -1))
                    boolean = True
            elif event.key == pygame.K_RIGHT:
                if block.movable(field.get_field(), (0, 1)):
                    block.move((0, 1))
                    boolean = True
            elif event.key == pygame.K_DOWN:
                if block.movable(field.get_field(), (1, 0)):
                    block.move((1, 0))
            elif event.key == pygame.K_UP:
                if block.rotatable(field.get_field(), 1):
                    block.rotate(1)
            elif event.key == pygame.K_z:
                if block.rotatable(field.get_field(), -1):
                    block.rotate(-1)
            elif event.key == pygame.K_p:
                while True:
                    renderer.show_pause()
                    event = event_queue.get()
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            renderer.show_game_background()
                            break

            renderer.draw_field(field.get_field(), block, emptied_rows)
            event_queue.clear_queue()
            if boolean:
                return None

        elif event.type == pygame.QUIT:
            return False

        current_field = field.get_field()
        if not block.movable(current_field):
            field.update(block.stop(current_field))
            return True
        else:
            block.move()

    def handle_name_input(self, text, event_queue):
        '''Käsittelee näppäimistön tapahtumat pelikierroksen jälkeen, kun pelaaja näppäilee nimensä

        Args:
            text: Merkkijono, jonka pelaaja on näppäillyt tähän mennessä
            event_queue: EventQueue-olio
        
        Returns:
            False, kun pelaaja on valmis
            text[:len(text)-1], eli palauttaa attribuuttina annetun merkkijonon ilman viimeistä merkkiä
            text + event.unicode, eli palauttaa merkkijonon, johon on lisätty pelaajan näppäilemä merkki
        '''
        event = event_queue.get()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return False
            if event.key == pygame.K_BACKSPACE:
                if len(text) == 1:
                    return ""
                return text[:len(text)-1]
            else:
                if len(text) == 7:
                    return text
                return text + event.unicode