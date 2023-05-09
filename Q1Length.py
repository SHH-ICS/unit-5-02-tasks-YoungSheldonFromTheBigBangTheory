# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.


while True:
        i = (input("Type in word here: "))
        print("\nThe number of charcters in your word is ",(len(i)))
        q = input("\nWould you like another question or Quit? y/n: ")

        s = str.upper(q)
        if s == "YES" or s == "Y":
            s = s
        elif s == "NO" or s == "N":
            print("\nOk, Thank you for using Q1Length!\n")
            break
            
        while s != "YES" and s != "Y" and s == "NO" and s == "N":
            print("\nPlease answer with yes or no\n")
            q = input("\nWould you like another question or Quit? y/n: ")
            