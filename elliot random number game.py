import random

#for i in range(10,20,2):
#print ()

#for i in range(20):
   # print(random.randint(1<100))
'''print("welcome to the fortune teller")
print ("your furtune is")
random=random.randint(1,3)
if random==1:
    print ("you will win a lot of money")
elif random==2:
    print ("you will get pulled over by police when your 24")
elif random==3:
    print("you will get a pet lizard")'''


'''password="Pouncer"
guess=input("guess the password")
while guess!=password:
    guess=input("guess again")'''

print("this is the number random game")
number=random.randint(0,10000)
tries=1
guess=int(input("guess the number 0 to 1000000000"))
while guess!=number:
    tries=tries+1
    print("incorect")
    if guess > number:
        print ("the number is less then that")
    elif guess < number:
        print ("the number is more that that")
    guess=int(input("guess again"))
print ("you got it the number was",number) 
print ("it took you",tries,"tries")
