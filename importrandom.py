import random
class fruitquiz:
    def __init__(self):
        self.fruits={"apple":"red","banana":"yellow","grape":"purple","orange":"orange"}
    def quiz(self):
        while True:
            fruit,colour=random.choice(list(self.fruits.items()))
            print("what is the colour of ",fruit)
            useranswer=input("enter your answer:")
            if useranswer.lower()==colour:
                print("correct answer")
            else:
                print("wrong answer")
                option=int(input("do you want to continue enter 0 if you wnat to play again or enter 1 to exit"))
                if option==0:
                    break
print("welcome to fruit quiz")
fq=fruitquiz()
fq.quiz()


                    
                

    