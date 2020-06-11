print("\t========Guess the Number Game==========")
n=45
guesses=1
print("Provided number of guesses=10")
while(guesses<=10):
    n1=int(input("Guess the Number\n"))
    if n1>45:
        print("You Enetered a Larger Input !Try Again\n")
    elif n1<45:
        print("You Entered a Smaller Input ! Try Again\n")
    else:
        print("You Won\n")
        print("No of Guesses Used:",guesses)
        break
    print("No of Guesses Left:",10-guesses)
    guesses = guesses + 1
if(guesses>10):
    print("Game Over")
