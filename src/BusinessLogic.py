"""
Author: Denis Kotnik, april 2021
TODO: maybe encapsulate logic from methods processFlower, processDesign and processBouquet.
"""

import collections

from Bouquet import Bouquet
from Design import Design
from Flower import Flower

class BusinessLogic:
    def __init__(self):
        self.designs = {'L' : [], 'S' : []}
        self.flowers = []
    
    def addDesign(self, data):
        design = Design(data["designCode"], data["designName"], data["designSize"], data["designCapacity"], data["designFlowers"])
        self.designs[design.getSize()].append(design)

    def addFlower(self, data):
        flower = Flower(data["flowerSpecies"], data["flowerSize"])
        self.flowers.insert(0, flower)
    
    def processFlower(self):
        """
        Process first flower in the queue.
        """
        flower = self.flowers.pop()
        for design in self.designs[flower.getSize()]:
            if (design.getSize() == flower.getSize()):
                if flower.getSpecies() in design.getFlowers():
                    return self.processDesign(design, flower)
    
    def processDesign(self, design, flower):
        """
        Process design.
        """
        designFlowers = design.getFlowers()
        if designFlowers[flower.getSpecies()] > 0 and design.getAvailable() > 0:
            designFlowers[flower.getSpecies()] -= 1
            design.setAvailable(design.getAvailable() - 1)
            design.appendUsedFlower(flower.getSpecies())
        if design.getAvailable() <= 0:
            return self.processBouquet(design)
    
    def processBouquet(self, design):
        """
        Create bouquet from the data in design and return its name.
        """
        counter = collections.Counter(design.getUsedFlowers())

        freq = sorted(counter.items(), key=lambda item: item[0])
        flowers = ''.join(str(x[1]) + str(x[0]) for x in freq)
        design.reset()
        
        bouquet = Bouquet(design.getName(), design.getSize(), flowers)
        return bouquet.getName()