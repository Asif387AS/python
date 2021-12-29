# f=open('tiddi.txt','r')
f=open('tiddi.txt') #by default read r mode 
# data=f.read()
data=f.readline() #read the first line
print(data)
data=f.readline() #iread the second line
print(data)
data=f.readline() #read the third line
print(data)
data=f.readline() #read the fourth line
print(data)
data=f.readline() #read the fifth line
print(data)
data=f.readline() #read the fifth line
print(data)
f.close()