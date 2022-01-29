from random import seed
from random import randint
rocksc = "rock,paper,scissors"
print ("rock,paper,scissors")
humchoice = int (input("enter a number from 0 to 2: "))

value = randint(0, 2)
if value == 1 :
   aichoic = "paper"
   print (aichoic)
elif value == 2:
    aichoic = "scissors"
    print (aichoic)
else :
    aichoic = "rock"
    print (aichoic)
if humchoice == 1 :
   hum = "paper"
elif humchoice == 2:
    hum = "scissors"
else :
    hum = "rock"
if hum == "rock" and aichoic == "paper":
    print ("ai wins")
if hum == "rock" and aichoic == "scissors":
    print ("human wins")
elif hum == "paper" and aichoic == "rock":
    print ("human wins")
elif hum == "scissors" and aichoic == "paper":
    print ("human wins")
elif hum == "scissors" and aichoic == "rock":
    print ("ai wins")
elif hum == "paper" and aichoic == "scissors":
    print ("ai wins")
elif hum == "rock" and aichoic == "rock":
    print ("draw")
elif hum == "scissors" and aichoic == "scissors":
    print ("draw")
elif hum == "paper" and aichoic == "paper":
    print ("draw")