list1=[54,65,34,65,75,52,98,65,43]
#make a new list,dic,set from existing list on the base of condition

# list2=[]
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# print(list2)

#shortcut to write the above code 
# b=[i for i in list1 if i%2==0]
b=[i for i in list1 if i>50]
print(b)

t=[4,4,5,5,6,6,7]
s={i for i in t}
print(s)
