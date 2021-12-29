s=set()
s.add(32)
s.add(62)
s.add(38)#  adding the value repetatily does not matter it will ignore
s.add(38)
# s.add([4,6,2,5])  #we cannot add list in set because it is hashable or changeable and set is unhashable
s.add((4,5,5,6,7))  #qw CAN  add tuple in set because it is unhashable
# s.add({4,5,6,7,7,8}) #we cannot add dictionay in set because it is also hashable
print(s)

# prints the length of set 
print(len(s))  
#remove element from set if exit
print(s.remove(32))

#pop method will remove the random element from set
print(s.pop())
print(s)

# print(s.clear()) #will clear all elements 
 
# intersection of set 
# union of set 
#differene of set 
s1=(4,5,3,2,5)
s.intersection(s1)
print(s)
