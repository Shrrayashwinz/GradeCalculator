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


grade = input("Please enter your grade (in numbers please):")

if grade <= 100 and grade >= 93:
    print ("A")

elif grade <= 92 and grade >= 90:
    print ("A-")

elif grade <= 89 and grade >= 87:
    print ("B+")

elif grade <= 86 and grade >= 83:
    print ("B")

elif grade <= 80 and grade >= 82:
    print ("B-")

elif grade <= 89 and grade >= 87:
    print ("B+")

elif grade <= 86 and grade >= 83:
    print ("B")

elif grade <= 80 and grade >= 82:
    print ("B-")
elif grade <= 89 and grade >= 87:
    print ("B+")

elif grade <= 86 and grade >= 83:
    print ("B")

elif grade <= 80 and grade >= 82:
    print ("B-")

else:
    print("F is for failure. You suck you stupid loser")


#more to be added soon to a repo near you!

else:
    raise ValueError("Not an acceptable format.")
