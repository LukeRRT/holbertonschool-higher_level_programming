#!/usr/bin/env python3
"""
The Mystical Dragon - Mastering Mixins
"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Testing
if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()  # Outputs: The creature swims!
    dragon.fly()   # Outputs: The creature flies!
    dragon.roar()  # Outputs: The dragon roars!
