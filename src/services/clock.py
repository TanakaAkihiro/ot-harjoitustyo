import pygame


class Clock:
    '''
    Luokka, joka käsittelee palikoiden liikkumisen nopeutta.

    Attributes:
        clock: Pygamen Clock-olio
    '''

    def __init__(self):

        self._clock = pygame.time.Clock()

    def tick(self, fps):
        '''
        Liikuttaa kelloa eteenpäin.
        '''
        self._clock.tick(fps)
