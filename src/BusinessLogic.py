"""
Author: Denis Kotnik, april 2021
"""

import collections

from Bouquet import Bouquet
from Design import Design
from Flower import Flower


class BusinessLogic:
    def __init__(self):
        self.designs = {'L': [], 'S': []}
        self.flowers = []
    
    def add_design(self, data):
        design = Design(
            data["design_code"],
            data["design_name"],
            data["design_size"],
            data["design_capacity"],
            data["design_flowers"]
        )

        self.designs[design.size].append(design)

    def add_flower(self, data):
        flower = Flower(data["flower_species"], data["flower_size"])
        self.flowers.insert(0, flower)
    
    def process_flower(self):
        """
        Process first flower in the queue.
        """
        flower = self.flowers.pop()
        for design in self.designs[flower.size]:
            if design.size == flower.size:
                if flower.species in design.flowers:
                    return self.process_design(design, flower)
    
    def process_design(self, design, flower):
        design_flowers = design.flowers

        if design_flowers[flower.species] > 0 and design.available > 0:
            design_flowers[flower.species] -= 1
            design.set_available(design.available - 1)
            design.append_used_flower(flower.species)

        if design.available <= 0:
            return self.process_bouquet(design)

    @staticmethod
    def process_bouquet(design):
        """
        Create bouquet from the data in design and return its name.
        """
        counter = collections.Counter(design.flowers)

        freq = sorted(counter.items(), key=lambda item: item[0])
        flowers = ''.join(str(x[1]) + str(x[0]) for x in freq)
        design.reset()
        
        bouquet = Bouquet(design.name, design.size, flowers)
        return bouquet.name
