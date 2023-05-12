# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.


while True:
        i = (input("Type in word here: "))
        print("\nThe number of charcters in your word is ",(len(i)))
        q = input("\nWould you like another question or Quit? y/n: ").lower()

        if q == "yes" or q == "y":
            q = q
        elif q == "no" or q == "n":
            print("\nBye bye\n")
            break
            
        while q != "yes" or q != "y" or q == "no" or q == "n":
            print("\nPlease answer with yes or no")
            q = input("\nWould you like another question or Quit? y/n: ").lower()
            