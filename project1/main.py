import random
randNo=random.randint(1,3)
print(randNo)

def gameWin(comp,you):
    if comp==you:
        None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    

print("Com Turn: Snake(s) Water(w) or Gun(g)?")
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
else:
    comp='g'

your=input("Your turn: Snake(s),Water(s),Gun(g)")
a=gameWin(comp,your)

print(f"Computer choose{comp}  ")
print(f"You choose {your} ")
if a==None:
    print("Tie the match")
elif a:
    print("You win the match")
else:
    print("You Lose the match")
