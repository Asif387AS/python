while(True):
    print("Enter the q to quit")
    a=input("Enter the integer")
    if a=='q':
        break
    try:
        a=int(a)
        if a>6:
            print("Number is greater than 6")
    except Exception as e:
        print(f"Your input is resulted in error :{e}")
print("Thanks for playing this game")
