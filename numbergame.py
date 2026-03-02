print("welcome to the number game") #genarate a random integeer and match it wuth input given by user
import random
playing=True
number=str(random.randint(1,5))
print("the computer will genrate a number from 1 to 5 and you have to guesse the number")
while playing:
    guess=input("enter your guesse:")
    if guess==number:
        print("you win the game")
        print("the number was:",number)
        break
    else:
        print("the number was:",number)
        print("your guess is not correct. Try again!")

             



