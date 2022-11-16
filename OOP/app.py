# Object Oriented Programming in Python

#What is an object? instance of a class

# class Dog:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name

#     def set_name(self, new_name):
#         self.name = new_name
#         return self.name

#     def get_age(self):
#         return self.age

#     def set_age(self, new_age):
#         self.age = new_age
#         return self.age


# a = Dog("Tyler", 24)
# print(a.get_name())
# print(a.set_name("Big T"))
# print(a.get_name())
# print(a.get_age())
# print(a.set_age(25))



#STUDENTS AND COURSE

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade

# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()

#         return value / len(self.students)

# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s3)

# print(course.get_average_grade())





#INHERITANCE

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


    def speak(self):
        print("Meow")

a = Dog("Charlie", 1)
a.show()
a.speak()


