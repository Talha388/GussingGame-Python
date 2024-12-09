
# PROJECT 2 == The perfect Guess  (GUessing Number)


import random
import pyttsx3
engine = pyttsx3.init()
engine.say("Welcome to the Guessing Number Game")
print("Welcome to the Guessing Number Game ✨✨✨✨")

n = random.randint(1,100)

a = -1        # in this game negative number is not possible  and for while loop we make this condtion
guesses = 1

while(a != n):
    a = int(input("Guess the Number 🤔 :  "))
    if(a>n):
        print("Please enter lower number")
        guesses+=1
    
    elif(a<n):
        print("Please enter higher number")
        guesses+=1
        
engine = pyttsx3.init()
engine.say("Congraats!")
engine.runAndWait()
print("Congraats!🎉🎉🎉")
print(f"You guess the number {n} correctly in {guesses} attempts")

















