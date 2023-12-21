# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 13:48:24 2023

@author: jacob
"""

class Student:
    def __init__(self, lastName='Popescu', gpa=3.8):
        self.lastName = lastName
        if type(self.lastName) != str:
            print('Error: Last name should be a string silly goose. Setting default last name: "Popescu".')
            self.lastName = 'Popescu'
        if 0 <= gpa <= 4:
            self.gpa = gpa
        else:
            print('Error: GPA should be between 0 and 4. Setting default gpa: 3.8.')
            self.gpa = 3.8

    def compareGPA(self, other):
        if self.gpa > other.gpa:
            print(self.lastName)
        elif self.gpa < other.gpa:
            print(other.lastName)
        else:
            print('Both students have the same GPA')
   
    
"Testing the code below"
        
if __name__ == "__main__":
   s1 = Student('Kocemba', 3.45)
   s2 = Student('Loser', 2.5)
   errorTest= Student(123, 5.0)
   s4 = Student ()
   
   s1.compareGPA(s2)
   s2.compareGPA(s1)
   s1.compareGPA(errorTest)
   errorTest.compareGPA(s2)
   s4.compareGPA(s1)
   s4.compareGPA(errorTest)