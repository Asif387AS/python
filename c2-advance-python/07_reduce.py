
from functools import reduce
sum=lambda a,b:a+b
l=[4,4,5,6,7,7]
val=reduce(sum,l)
print(val)