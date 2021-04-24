import pygame


class EventQueue:
    '''
    Luokka, joka käsittelee tapahtumasarjoja.
    '''
    def get(self):
        '''
        Palauttaa tapahtumasarjoja.
        '''
        return pygame.event.get()
