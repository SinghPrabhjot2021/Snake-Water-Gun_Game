import random
def game(comp,you):
 
    if comp==you:
        print("Game is tie")
    elif comp=='s':
        if you=='w':
            print("Computer Wins",comp)
        elif you=='g':
            print("You Win",you)     
    elif comp=='w':
        if you=='g':
           print("Computer Wins",comp)
        elif you=='s':
            print("You Win",you) 
    elif comp=='g':
        if you=='s':
           print("Computer Wins",comp)
        elif you=='w':
           print("You Win",you)           
Random= random.randint(1,3)
if Random==1:
        comp ='s'
elif Random==2:
        comp='w'
elif Random==3:
    comp='g' 
you=input("Your Turn : ")
print(f"Computer Chose {comp}")
print(f"You Chose {you}")
game(comp,you)