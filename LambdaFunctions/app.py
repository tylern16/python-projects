# LAMBDA, MAP, LIST COMPREHENSIONS, FILTER


# def func(x):
#     func2 = lambda x: x+5
#     return func2(x)+3

# print(func(7))

# say_hello = lambda str: print(str)
# say_hello("Tyler")

# li = [1,2,3,4,5]

# # print(list(map(lambda x: x**x, li)))

# newList = [x**x for x in li]
# print(newList)


def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9]

b = list(filter(isOdd,a))

c = list()

print(a)
print(b)