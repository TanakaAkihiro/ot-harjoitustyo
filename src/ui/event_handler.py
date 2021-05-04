import pygame


class EventHandler:
    def handle_events(self, event_queue, renderer, field, block, emptied_rows, current_field):
        '''
        Käsittelee näppäimistön tapahtumat
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

            renderer.draw_field(field.get_field(), block, emptied_rows)
            event_queue.clear_queue()
            if boolean:
                return None

        elif event.type == pygame.QUIT:
            return False  
        
        if not block.movable(current_field):
            field.update(block.stop(current_field))
            return True
        else:
            block.move()
