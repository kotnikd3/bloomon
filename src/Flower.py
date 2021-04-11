"""
Author: Denis Kotnik, april 2021
"""

class Flower:
    def __init__(self, species, size):
        self.species = species
        self.size = size
    
    def getSize(self):
        return self.size
    
    def getSpecies(self):
        return self.species