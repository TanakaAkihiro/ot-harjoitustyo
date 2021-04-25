import pygame


class EventQueue:
    '''
    Luokka, joka käsittelee tapahtumasarjoja.
    '''

    def get(self):
        '''
        Palauttaa tapahtumasarjoja.
        '''
        return pygame.event.poll()

    def clear_queue(self):
        '''
        Tyhjentää tapahtumasarjan.
        '''
        pygame.event.clear()
