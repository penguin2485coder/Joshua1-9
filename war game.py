'''anything=["pouncer",574,True,6743.654,6]
print(anything[1])
anything.append("pouncer eats a lot")
print(anything)
anything.remove(pouncer)
print(anything)'''
import random

print ("welcome to the number war game")
myhand=[]
comhand=[]
for i in range(10):
    myhand.append(random.randint(1,100))
    comhand.append(random.randint(1,100))
print("here is your hand")
print (myhand)
print("here is the computers hand") 
print(comhand)
myscore=0
cscore=0

for i in range(10):
    print("this is your updated list")
    print (myhand)
    choice=int(input("what number would you like to play"))
    while choice not in myhand:
          choice=int(input("what number would you like to play"))
    myhand.remove(choice)
    comchoice=random.choice(comhand)
    comhand.remove(comchoice)
    print("the computer chose",comchoice)
    if choice>comchoice:
        print("you won this round")
        myscore+=2
    elif choice<comchoice:
        print("you lost this round")
        cscore+=2
    print("tie")
if score>cscore:
    print ("you win")
else:
    print("you lost")
