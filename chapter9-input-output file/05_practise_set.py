#problem:1
# f=open('peom.txt','r')
# a=f.read()
# if 'twinkle' in a :
#     print("Twinkle is present in peom")
# else:
#     print("twinkle is not present in peoms")
#     f.close()
    
    #problem:2
# def game():
#     return 88340

# highscore=game()
# with open('highscore.txt') as f:
#     score=f.read()
# if score=='':
#     with open('highscore.txt','w') as f:
#          f.write(str(highscore))

# elif int(score)<highscore:
#     with open('highscore.txt','w') as f:
#         f.write(str(highscore))


#problem:4
# with open('tiddi.txt') as f:
#     read=f.read()
#     content=read.replace('tiddi','shabnam')
# with open('tiddi.txt','w') as f:
#     f.write(content)

#problem:5
# words=['tiddi','saba','bestie','honey bee']
# with open('tiddi.txt') as f:
#     read=f.read()
# for word in words:
#     content=read.replace(word,'shabnam')

#     with open('tiddi.txt','w') as f:
#      f.write(content)

#problem:6
# with open('tiddi.txt') as f:
#     data=f.read().lower()
# if 'python' in data:
#     print("python is present")
# else:
#     print("python is not present")

#problem:7
# data=True
# i=1
# with open('tiddi.txt') as f:
#     while data:
#        data=f.readline()
#        if 'python' in data.lower():
#          print(data)
#          print(f"python is present at line number {i}")
#        i=i+1

#problem:8
# with open('tiddi.txt') as f:
#     copyText=f.read()
# with open('tiddi2.txt','w') as f:
#     f.write(copyText)

#problem:9
# with open('tiddi.txt') as f:
#     f1=f.read()
# with open('tiddi2.txt') as f:
#     f2=f.read()
# if f1==f2:
#     print("files are identical")
# else:
#     print("files are not identical")

#problem:10
# with open('write.txt','w') as f:
#     f.write("")

#problem:11
import os
with open('asif.txt') as f:
    copyText=f.read()
with open('asif2.txt','w') as f:
    f.write(copyText)
os.remove('asif.txt')