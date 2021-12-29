try:
    a=int(input("Enter the number"))
    c=2/a
    print(c)
except ValueError as e:
    print("Plzz enter the valid value")
    print(e)
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero")
    print(e)
print("Thanks for using this code!")