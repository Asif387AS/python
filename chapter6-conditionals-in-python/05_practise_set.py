#problem :1 find greates number 
# num1=int(input("Enter the num1"))
# num2=int(input("Enter the num2"))
# num3=int(input("Enter the num3"))
# num4=int(input("Enter the num4"))
# if(num1>num4):
#     f1=num1
# else:
#     f1=num4 #(pass) if we want to remain it empty then use pass

# if(num2>num3):
#     f2=num2
# else:
#     f2=num3

# if(f1>f2):
#     print(str(f1) +"  is greatest") 
# else:
#     print(str(f2) + "  is greatest")

    #problem:2 
# sub1=int(input("Enter the mark of subject 1\n"))
# sub2=int(input("Enter the mark of subject 2\n"))
# sub3=int(input("Enter the mark of subject 3\n"))
# if(sub1<33 or sub2<33 or sub3<33):
#     print("Sorry! You are fail.")
# elif(sub1+sub2+sub3)/3<40:
#     print("Sorry! you are fail due total percentage less than 40")
# else:
#     print("Congratulation! you are passed")


#problem:3
# text=input("Enter the text\n")
# if("make a lot of money" in text):
#     Spam=True
# elif("buy this" in text):
#     Spam=True
# elif("click this" in text):
#     Spam =True
# elif("subscribe this" in text):
#     Spam=True
# else:
#     Spam=False

# if(Spam):
#     print("This is Spam")
# else:
#     print("This is not Spam")

#problem:4 (solve by own)
# username=input("Enter the name\n")
# if(len(username)<10):
#     print("Username is less than 10 characters")
# else:
#     print("username is not contain 10 characters")

#problem:5
# names=['asif','hassan','haris','hussnain','adeel']
# name=input("Enter your name:\n")
# if(name in names):
#     print("Name is present in list")
# else:
#     print("Name is not present in the list")

#problem:6
# marks=int(input("Enter your marks \n"))
# if marks>=90:
#     grade="Ex"
# elif marks>=80:
#     grade="A"
    
# elif marks>=70:
#     grade="B"
# elif marks>=60:
#     grade="C"
# elif marks>=50:
#     grade="D"
# else:
#     grade="F"

# print("You Grade is "+ grade)    


#problem:7
post=input("Write a post\n")
name="asif"
name1="Asif"
if(name in post):
    print("post contain asif")
elif(name1 in post):
    print("post contain Asif")
else:
    print("post not contain asif")