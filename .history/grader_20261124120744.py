"""
Program Name: grader.py

Author: Shrrayash Srinivasan

Purpose: Main file for the grader.

Date: November 21, 2026
"""
from collections.abc import Callable

import os

import json


# Main grade calculator

grade = input(int("Please enter your grade (in numbers please):"))

if grade <= 100 and grade >= 93:
    print ("A")

elif grade <= 92 and grade >= 90:
    print ("A-")

elif grade <= 89 and grade >= 87:
    print ("B+")

elif grade <= 86 and grade >= 83:
    print ("B")

elif grade <= 82 and grade >= 80:
    print ("B-")

elif grade <= 79 and grade >= 77:
    print ("C+")

elif grade <= 76 and grade >= 73:
    print ("C")

elif grade <= 72 and grade >= 70:
    print ("C-")

elif grade <= 69 and grade >= 67:
    print ("D+")

elif grade <= 66 and grade >= 63:
    print ("D")

elif grade <= 62 and grade >= 60:
    print ("D-")

elif grade <= 59:
    print("F is for failure. You suck you stupid loser")

else:
    raise ValueError("Not an acceptable format.")
