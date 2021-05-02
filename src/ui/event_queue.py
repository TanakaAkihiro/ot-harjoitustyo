import pygame


class EventQueue:
    '''
    Luokka, joka käsittelee tapahtumasarjoja.
    '''

    def get(self):
        '''
        Palauttaa tapahtumasarjasta ensimmäisen komennon.
        '''
        return pygame.event.poll()

    def get_all(self):
        '''
        Palauttaa koko tapahtumasarjan.
        '''
        return pygame.event.get()

    def clear_queue(self):
        '''
        Tyhjentää tapahtumasarjan.
        '''
        pygame.event.clear()
