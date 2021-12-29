def greater_than_5(num):
    if num>5:
        return True
    else:
        return False
l=[4,6,7,8,9]
print(list(filter(greater_than_5,l)))