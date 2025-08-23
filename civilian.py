
from human import Human

class Civilian(Human):

    def __init__(self, arena):
        super().__init__(arena, 0.7)
        self.colour = (0,255,0)



    