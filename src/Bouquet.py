class Bouquet:
    def __init__(self, design_name, flower_size, flowers):
        self.design_name = design_name
        self.flower_size = flower_size
        self.flowers = flowers

    @property
    def name(self):
        return self.design_name + self.flower_size + self.flowers
