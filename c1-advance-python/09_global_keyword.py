a=44 #global  variable
def Quiin():
    global a
    print(f"The value of statement 1:{a}")
    a=22  #llocal variable
    print(f"The value of statement 2 :{a}")
Quiin()
print(f"The value of statement i3 is :{a}")