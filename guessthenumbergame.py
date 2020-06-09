print("Welcome to My Guess the Number Game")
n=23
guesses=1
print("Provided no of Guesses = 9")
while(guesses <=9 ):
     number=int(input("Guess the Number:\n"))
     if number>18:
        print("You Entered a Greater Input\n")
     elif number<18:
        print("You Entered a Lesser Input\n")
     else:
        print("You Won\n")
        print(guesses,"No. of Guesses You Used")
        break
     print(9-guesses,"no of guesses left")
     guesses=guesses+1
if(guesses>9):
    print("Game Over")