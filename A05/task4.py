# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:09:16 2023

@author: jacob
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        dummy = str(self.area())
        dummy2 = str(self.perimeter())
        answer = "area: " + dummy + "\nperimeter: "+ dummy2
        return answer
    
    def __repr__(self):
        return "Circle({})".format(self.radius)
    

    # 4)
    #the __repr__() method returns a string containing a printable represetnation 
    # of an object.
    # The example below will print: Circle(5)
        # c = Circle(5)
        # print(repr(c))
    
    
    
    def __getattr__(self, name):
       if name == 'diameter':
           return 2 * self.radius
       elif name == 'circumference':
           return 2 * math.pi * self.radius
       else:
           raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
           
           
    # 4)
    #the __getattr__() method is meant to handle specific requests that adhere to the overall class. 
    # if the attribute is not found, then it will raise an attribute error      
    # For example, the code below will print 6
        # c = Circle(3)
        # print(c.diameter)
    # This will raise an attribute area 
        # c = Circle(3)
        #  print(c.volumeCircle)
        # Output: AttributeError: 'Circle' object has no attribute 'volumeCircle'
           