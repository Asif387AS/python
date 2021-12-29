try:
    a=int(input("Enter the Number"))
    c=3/a
    print(c)
except Exception as e:
    print("Exception occoured")
    print(e)
    exit()
finally:
    print("We are successfull")
print("We are done")