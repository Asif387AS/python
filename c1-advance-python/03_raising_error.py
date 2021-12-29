try:
    def increment(num):
        return int(num)+1
except:
    raise ValueError("This is not good bro")
print("Quiin is great")

i=increment('43')
print(i)