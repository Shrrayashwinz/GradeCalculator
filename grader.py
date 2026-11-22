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

#more to be added soon to a repo near you!

else:
    raise ValueError("Not an acceptable format.")
