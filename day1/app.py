# functions



# def say_hello(name):
#   print("Hi " + name + "!")

# say_hello("Tyler")

# mutable vs immutable

lst = [1,2,3]
lst2 = lst
# print(lst is lst2)

lst3 = lst[:]
# print(lst is lst3)

print(id(lst), id(lst2), id(lst3))
