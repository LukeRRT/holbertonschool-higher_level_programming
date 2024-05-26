#!/usr/bin/env python3
"""
Noname
"""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
        
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius
