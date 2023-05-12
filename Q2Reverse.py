# Create a program that will accept a word and output the word one letter at a time in reverse.
s = input("Enter a word: ")[::-1]

for char in s:
    print (char)