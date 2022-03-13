class Design:
    def __init__(self, code, name, size, total_capacity, flowers):
        self.code = code
        self.name = name
        self.size = size
        self.total_capacity = total_capacity
        self.flowers = flowers

        self.original_flowers = flowers.copy()
        self.available = self.total_capacity
        self.used_flowers = []

    def reset(self):
        """
        Reset the values to its original values.
        """
        self.__init__(
            self.code,
            self.name,
            self.size,
            self.total_capacity,
            self.original_flowers
        )
    
    def set_available(self, n):
        self.available = n
    
    def append_used_flower(self, flower):
        self.used_flowers.append(flower)
