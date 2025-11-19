import math
class Shape:
    def __init__(self,fillColor):
        self.fillcolor = fillColor
class Circle(Shape):
    def __init__(self,rad,fillColor):
        super().__init__(fillColor)
        self.rad = rad

    def area(self):
        return math.pi * self.rad**2
    
    def __lt__(self,other):
        return self.area()<other.area()
    
class Rectangle(Shape):
    def __init__(self,l,b,fillColor):
        super().__init__(fillColor)
        self.l=l
        self.b=b

    def area(self):
        return self.l *self.b

