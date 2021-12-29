try:
    a=int(input("Enter the Number"))
    c=3/a
    print(c)
except Exception as e:
    print("Exception occoured")
    print(e)
else:
    print("We are successfull")
