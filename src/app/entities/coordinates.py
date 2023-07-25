from math import sqrt


class Coordinates:
    x: float
    y: float

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Coordinate: {self.x},{self.y}"
    
    @staticmethod
    def distance(first,second):
        return sqrt(((first.x - second.x)**2) + ((first.y - second.y)**2))
    
    def moviment (self, moviment:str):
        if moviment == "up":
            return Coordinates(self.x, self.y + 1)
        elif moviment == "down":
            return Coordinates(self.x, self.y - 1)
        elif moviment == "left":
            return Coordinates(self.x - 1, self.y)
        elif moviment == "right":
            return Coordinates(self.x + 1, self.y)
        else:
            return Coordinates(self.x, self.y)