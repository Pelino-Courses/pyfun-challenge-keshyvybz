"""
shapes.py

Defines a base Shape class and specific shape subclasses with overridden methods.
"""

import math

class Shape:
    """
    Base class for all geometric shapes.

    Attributes:
    ----------
    name : str
        The name of the shape.
    """

    def __init__(self, name="Shape"):
        self.name = name

    def area(self):
        """
        Calculate the area of the shape.

        Raises:
        ------
        NotImplementedError:
            If not overridden by a subclass.
        """
        raise NotImplementedError("Area method must be overridden by subclass.")

    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Raises:
        ------
        NotImplementedError:
            If not overridden by a subclass.
        """
        raise NotImplementedError("Perimeter method must be overridden by subclass.")

    def __str__(self):
        return f"{self.name} - No specific dimensions provided."


class Rectangle(Shape):
    """
    Rectangle shape class.

    Attributes:
    ----------
    width : float
        The width of the rectangle (must be positive).
    height : float
        The height of the rectangle (must be positive).
    """

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.name} (width={self.width}, height={self.height})"


class Circle(Shape):
    """
    Circle shape class.

    Attributes:
    ----------
    radius : float
        The radius of the circle (must be positive).
    """

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"{self.name} (radius={self.radius})"

    @classmethod
    def from_diameter(cls, diameter):
        """
        Alternate constructor to create a circle from its diameter.

        Parameters:
        ----------
        diameter : float
            The diameter of the circle.

        Returns:
        -------
        Circle
            A Circle instance.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be positive.")
        return cls(diameter / 2)


class Square(Rectangle):
    """
    Square shape class (inherits from Rectangle).

    Attributes:
    ----------
    side : float
        The side length of the square (must be positive).
    """

    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive.")
        super().__init__(side, side)
        self.name = "Square"

    def __str__(self):
        return f"{self.name} (side={self.width})"
