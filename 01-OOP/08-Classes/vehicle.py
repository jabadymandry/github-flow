# pylint: disable=missing-docstring

# TODO: implement the `Vehicle` class
class Vehicle:
    """ """
    def __init__(self, marque, couleur):
        """ """
        self.started = False
        self.brand = marque
        self.color = couleur
        
    def start(self):
        """ """
        self.started = True
        
    def stop(self):
        """ """
        self.started = False