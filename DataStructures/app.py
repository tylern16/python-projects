'''
https://www.youtube.com/watch?v=kQDxmjfkIKY
'''

# TUPLES - immutable, faster

# tuple1 = (1,2,3)
# tuple2 = ()
# tuple3 = 1,2,3,4,5
# tuple4 = 1,

# list1 = [1,2,3,4]
# tuple5 = tuple(list1)
# print(tuple5, type(tuple5))




#SETS - non-duplicate items
# y = {1,2,3,2,1}
# print(type(y),y)


# DICTIONARY - dict- like java hashmap - key/value pair

# x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
# print(type(x))

# LIST COMPREHENSION - format: new_list = [transform sequence[filter]]

# import random

# under_10 = [x for x in range(10)]
# # print(under_10)

# squares = [x**2 for x in under_10]
# # print(squares)

# odds = [x for x in squares if x%2 == 0]
# # print(odds)



# STACKS - LIFO

# my_stack = list()
# my_stack.append(4)
# my_stack.append(5)
# my_stack.append(6)
# my_stack.append(7)

# print(my_stack.pop())

# class Stack():

#     def __init__(self):
#         self.stack = list()
    
#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if len(self.stack) > 0:
#             return self.stack.pop()
#         else:
#             return None
    
#     def peek(self):
#         if len(self.stack) > 0:
#             return self.stack[len(self.stack)-1]
#         else:
#             return None
    
#     def __str__(self):
#         return str(self.stack)


# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# print(my_stack)
# print(my_stack.peek())
# print(my_stack.pop())
# print(my_stack.peek())
# print(my_stack.pop())
# print(my_stack.pop())




#QUEUES - FIFO

# from collections import deque
# my_queue = deque()
# my_queue.append(5)
# my_queue.append(10)
# my_queue.popleft() # removes from left





# MAXHEAP - binary tree -every node is less than its parent

# class MaxHeap:

#     def __init__(self, items = []):
#         super().__init__()
#         self.heap = [0]
#         for item in items:
#             self.heap.append(item)
#             self.__floatUp(len(self.heap) - 1)

#     def push(self, data):
#         self.heap.append(data)
#         self.__floatUp(len(self.heap) - 1)

#     def peek(self):
#         if self.heap[1]:
#             return self.heap[1]
#         else:
#             return False

#     def pop(self):
#         if len(self.heap) > 2:
#             self.__swap(1, len(self.heap) - 1)
#             max = self.heap.pop()
#             self.__bubbleDown(1)
#         elif len(self.heap) == 2:
#             max = self.heap.pop()
#         else:
#             max = False
#         return max 

#     def __swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#     def __floatUp(self, index):
#         parent = index//2
#         if index <= 1:
#             return
#         elif self.heap[index] > self.heap[parent]:
#             self.__swap(index, parent)
#             self.__floatUp(parent)

#     def __bubbleDown(self, index):
#         left = index * 2
#         right = index * 2 + 1
#         largest = index
#         if len(self.heap) > left and self.heap[largest] < self.heap[left]:
#             largest = left
#         if len(self.heap) > right and self.heap[largest] < self.heap[right]:
#             largest = right
#         if largest != index:
#             self.__swap(index, largest)
#             self.__bubbleDown(largest)

#     def __str__(self):
#         return str(self.heap)

# m = MaxHeap([95,3,21])
# m.push(10)
# print(m)
# print(m.pop())
# print(m.peek())



# LINKED LIST

