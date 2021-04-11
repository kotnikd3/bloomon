"""
Author: Denis Kotnik, april 2021
"""

class Design:
    def __init__(self, code, name, size, totalCapacity, flowers):
        self.code = code
        self.name = name
        self.size = size
        self.totalCapacity = totalCapacity
        self.flowers = flowers

        self.originalFlowers = flowers.copy()
        self.available = self.totalCapacity
        self.usedFlowers = []
    
    def getFlowers(self):
        return self.flowers
    
    def reset(self):
        """
        Reset the values to its original values - the values that they have been used for instatiation.
        """
        self.__init__(self.code, self.name, self.size, self.totalCapacity, self.originalFlowers)
    
    def getSize(self):
        return self.size
    
    def getAvailable(self):
        return self.available
    
    def setAvailable(self, n):
        self.available = n
    
    def appendUsedFlower(self, flower):
        self.usedFlowers.append(flower)
    
    def getUsedFlowers(self):
        return self.usedFlowers
    
    def getName(self):
        return self.name
    
    def getSize(self):
        return self.size