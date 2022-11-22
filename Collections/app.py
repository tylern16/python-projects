# import collections 
# from collections import Counter

# """
# Containers
# List(Array), Dict, Set, Tuple

# Types - from collections
# counter, deque, namedTuple. ordereddict, defaultdict
# """

# c = Counter("gallad")
# print(c["a"])

# l = list(c.elements())
# print(l)

# print(c.most_common(2))




# ARGS AND KWARGS

def add_items(*args):
    print(args)
    result = sum(args)
    print(result)

# add_items(1,2,3)
# add_items(1,2,3,5)
# add_items(1,2,3,4,5,6)




# blog_title = "My Blog"

# def blog_posts(title, *args, **kwargs):
#     print(title)
#     for arg in args:
#         print(arg)
#     for p_titile, post in kwargs.items():
#         print(p_titile, post)

# blog_posts(blog_title,
#     1,2,3,
#     blog1 = "I am Awesome",
#     blog2 = "Cars",
#     blog3 = "Cat"
# )

# import matplotlib.pyplot as plt

# def graph_operation(x,y):
#     print('function that graphs {} and {}'.format(str(x), str(y)))
#     plt.plot(x,y)
#     plt.show()

# x1 = [1,2,3]
# y1 = [2,3,1]

# graph_operation(x1,y1)



# STRING CONCAT

names = ["Tyler", 'Gary', 'Tim', 'Bill']

# for name in names:
    # print("Hello there: " + name)
    # print(' '.join(["Hello there:", name]))

# print((", ").join(names))

# import os

# location_files = '/Users/tylernenninger/Desktop/Projects/python-projects/Collections/'
# file_name = 'example.txt'

# with open(os.path.join(location_files, file_name)) as f:
#     print(f.read())

# who = 'Gary'
# how_many = 12

# print(f'{who} bought {how_many} apples today!')



