import random
str="welcome to our python virtual game!"
print(str.center(65))
user=int(input("enter your move do you want:\nmove for snake press 1\nfor water enter 2\nfor gun enter 0\n"))
comp=random.randint(0,2)
print("computer choosed:",comp)
if(user==comp):
    print("Draw")
elif(user==0 and comp==1):
    print("win the match")
elif(user==1 and comp==2):
    print("you won")
elif(user==2 and comp==0):
    print("you won the game")
elif(user==0 and comp==2):
    print("looser")
elif(user==1 and comp==0):
    print("you lost the match..")
elif(user==2 and comp==1):
    print("computer won")
else:
    print("your input is invalid please try again")



