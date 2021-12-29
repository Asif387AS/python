# f=open('tiddi.txt','r')
f=open('tiddi.txt') #by default read r mode 
# data=f.read()
data=f.read(5) #it will read first 5 characters 
print(data)
f.close()