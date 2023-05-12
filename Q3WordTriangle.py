# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON

import time

s = input("Enter a word: ")

for char in range(len(s)):
    for col in range(char+1):
        print(s[col],end=' ')
    print()
