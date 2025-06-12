def add2nums(a=5, b=10):
    try:
        c = float(a) + float(b)
    except ValueError:
        return False
    return c

def MyObjects(listordict):
    mylist = listordict.copy()  # Create a copy to avoid modifying the original
    mylist[0] = 42
    print(f"in function: {mylist}")

myownlist = [1, 2, 3, 4]
print(f"myownlist before: {myownlist}")
MyObjects(myownlist)
print(f"myownlist after: {myownlist}")

result = add2nums(1,3)
print(result)
result = add2nums("x","y")
result = add2nums(15)
print(result)
result = add2nums()
result = add2nums(b=67)
print(result)
