# n=3
# product=1
# for i in range(n):
#     product=product*(i+1)
# print(product)

# def factorial_iter(n):
#     product=1
#     for i in range(n):
#       product=product*(i+1)
#     return product

# f=factorial_iter(5)
# print(f)

def factorial_recursion(n):
  if n==0 or n==1:
      return 1
  return n*factorial_recursion(n-1)

f=factorial_recursion(1)
print(f)