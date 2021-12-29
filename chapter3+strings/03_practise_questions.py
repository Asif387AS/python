# Problem:1
# name=input("Enter your name\n")
# print("Good afternoon,"+name)

#problem:2
# str='''Dear <|Name|> 
# Greeatings from ABC house. i am happy to till you about your seasiflection
# Have a great day ahead,
# Thanks and Regards,
# Tiddi
# <|Date|>'''
# name=input("Enter you name\n")
# date=input("Enter the date\n")
# str=str.replace("<|Name|>",name)
# str=str.replace("<|Date|>",date)
# print(str)

#problem:3
str="asif is a great boy and tiddi is  bomb"
doubleSpaces=str.find("  ")
print(doubleSpaces)
#problem:4
str="asif is a great    boy and tiddi is  bomb"
doubleSpaces=str.replace("  "," ")
print(doubleSpaces)

#problem: 5
letter="Dear Asif,This python course is very halpfu!,Thanks"
print(letter)
formatted_letter="Dear Asif,\n\tThis python course is very halpfu!,\nThanks"
print(formatted_letter)
