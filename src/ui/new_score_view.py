import pygame


class NewScoreView:
    def __init__(self, screen, width, height, score, clock, event_handler, event_queue):
        self._screen = screen
        self._width = width
        self._height = height
        self._score = score
        self._clock = clock
        self._event_handler = event_handler
        self._event_queue = event_queue

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0), "Yellow": (255, 255, 0)}

    def render(self):
        rect = pygame.Rect(self._width//2 - 300,
                           self._height//2 - 200, 600, 400)
        pygame.draw.rect(self._screen, self._colors["Black"], rect)

        text_font = pygame.font.SysFont(None, 48)
        text_content = "Score: " + str(self._score)
        text = text_font.render(text_content, True, self._colors["White"])
        rect = text.get_rect()
        self._screen.blit(
            text, ((self._width - rect[2])//2, self._height//2 - 150))

        text_content = "Type your name"
        text = text_font.render(text_content, True, self._colors["Yellow"])
        rect = text.get_rect()
        self._screen.blit(
            text, ((self._width-rect[2])//2, self._height//2 - 100))

        text_content = "Press 'Enter' when you are ready"
        text = text_font.render(text_content, True, self._colors["White"])
        rect = text.get_rect()
        self._screen.blit(
            text, ((self._width-rect[2])//2, self._height//2 + 100))

        text_content = ""

        while True:
            name_rect = pygame.Rect(
                self._width//2 - 100, self._height//2 - 15, 200, 30)
            pygame.draw.rect(self._screen, self._colors["White"], name_rect)

            player_input = self._event_handler.handle_name_input(
                text_content, self._event_queue)
            if player_input or player_input == "":
                text_content = player_input
            elif player_input is False:
                return text_content

            text = text_font.render(text_content, True, self._colors["Black"])
            self._screen.blit(
                text, (self._width//2 - 100, self._height//2 - 15))
            pygame.display.flip()
            self._clock.tick(10)
