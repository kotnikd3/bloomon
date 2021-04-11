"""
Author: Denis Kotnik, april 2021
"""

class Bouquet:
    def __init__(self, designName, flowerSize, flowers):
        self.designName = designName
        self.flowerSize = flowerSize
        self.flowers = flowers
    
    def getName(self):
        return self.designName + self.flowerSize + self.flowers