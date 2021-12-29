print("string slicing")
a="asif,"
b="tidd"
c=a+b #string concatenation 
print(c)  


name="asifkitiddi"
print(name[2])
print(name[-2])
#name[4]="s"  #does not allow 

# slicing and special case slicing 
print(name[0:3])  # 0 is included and 3 is excluded 
print(name[0:]) #is same as name[0:lenght] mean at the end string or till miaximum number
print(name[1:]) # is same as name[1:length] meant 1 to last 
print(name[:4])  #is same as name[0:4] mean start from minimal number 
print(name[-6:-2])  #is same as name[5:10]

# skiping string technique

name="asifKiTiddi"
print(name[0::2]) #every after printing one character 1 character will skip
print(name[0::3]) #every after printing one character 2 character will skip
print(name[0::4])  #every after printing one character 3 character will 

# String functions 
story="once upon a time there Was a asif    one who uploaded asif pthon tuturial video"
print(len(story))
print(story.count("a"))
print(story.endswith('video'))
print(story.capitalize())
print(story.find("one")) #it will only return the index of first character
print(story.replace("asif","codewithasif"))  #it will replace with all the character in string
print(story.format())

#end at 2:14