
import math 

class Shapes:
    """
    a class for all geometric shapes .
    """
    def __init__ (self,name="shape "):
        self.name = name 

    def area(self):
        """this will calculate the area
        """
        raise NotImplementedError("override area with a subclass")
    
    def perimeter(self):
        """
        this will be calculating the perimeter 
        """
        raise NotImplementedError("överride the perimeter with a subclass")
    
    def __str__(self):
        return f"{self.name} no specific dimensions provided "
class Rectangle (Shapes):    

    def __init__(self,width,height):
        if width <= 0 or height <= 0:
           raise ValueError("those must be positive numbers")
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area (self):
         return self.width * self.height
    def perimeter(self):
         
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"{self.name} (width={self.width}, height={self.height})"
    


class Circle(Shapes):
    def __init__(self,radius):
        if radius <= 0:
            raise ValueError("it must be positive")
        super().__init__("circle")
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2 
    def perimeter (self):
        return 2 * math.pi * self.radius
    def __str__(self):
        return f"{self.name}(radius ={self.radius})"
    @classmethod
    def from_diameteer(cls,diameter):
        if diameter <= 0:
            raise ValueError("enter a positive number plz")
        return cls(diameter /2)
    

class Square(Rectangle):
    """

    squasre shape class to inherit from rectangle

    
    """
    def __init__(self,side):
        if side <= 0 :
            raise ValueError("enter a positive value") 
        super().__init__(side,side)
        self.name = "square"
    def __str__(self):
          return f"{self.name}(side ={self.width})"   
    
    

    