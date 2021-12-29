def square(num):
    return num*num

l1=[4,5,6]

# Method 1
# l2=[]
# for items in l1:
#      l2.append(square(items))
#      print(l2)

#Method 2
print(list(map(square,l1)))