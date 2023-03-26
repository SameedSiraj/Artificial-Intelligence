print("Scissor (0), Rock (1), Paper(2)")
print("Enter the number 0, 1, or 2")
number=int(input())
from random import randint
random_value = randint(0, 2)
if(number==0):
    if(random_value==0):
        print("The computer is scissor. You are scissor too. It is a draw")
    if(random_value==1):
        print("The computer is rock. You are scissor. You lose")
    if(random_value==2):
        print("The computer is paper. You are scissor. You won")
if(number==1):
    if(random_value==0):
        print("The computer is scissor. You are rock. You won")
    if(random_value==1):
        print("The computer is rock. You are rock too. It is a draw")
    if(random_value==2):
        print("The computer is paper. You are rock. You loose")
if(number==2):
    if(random_value==0):
        print("The computer is scissor. You are paper. You loose")
    if(random_value==1):
        print("The computer is rock. You are paper. You win")
    if(random_value==2):
        print("The computer is paper. You are paper too. It is a draw")