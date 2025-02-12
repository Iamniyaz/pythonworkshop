
# class student:
#     pass # pass is use to avoid error because of empty declaration
# class Person:
#    # "This is a person class"
#     age=10
#     def greet(self):
#         print("hello")
# P1=Person()
# P1.greet()
# print(P1.age)
# P1.age=20
# print(P1.age)
# '''constructor is help to create an object send the request to os to allocate space
#    operating system(os) will allocate the space in the memory
#    every constructor have there will be deconstructor
# '''
# '''class Shark:
#     def __init__(self):
#         print("The constructor is executed:")
#     def swim(self):
#         print("The shark is swimming")
#     def awesome(self):
#         print("the shark is being awesome ")
# s1=Shark()
# s1.swim()
# s1.awesome()
# print(id(s1))'''



# class Student:
#     schoolName='ABC School' # class attribute
#     def __init__(self):
#         self.name=''
#         self.age=0
# s1=Student()
# print(s1.name)
# s1.name="khadar"
# s1.age=23
# print(s1.name)
# print(s1.age)
 

#example5 what is the output of this program 
# class Shark:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def swim(self):
#         #Reference the name 
#         print(self.name+"is swimming")
#         print("The age is ",self.age)
#     def awesome(self):
#         #Reference the name
#         print(self.name+"is being awesome")
#         print("I am",self.age,"year old")
# S1=Shark("sammy",10)
# print(S1.name)
# print(S1.age)
# S1.swim()
# S1.awesome()



# class Person:
#     def __init__(self,name,age ,profession):
#         #data members( instance variables)
#         self.name=name
#         self.age=age
#         self.profession=profession
    
#     #Behavior (instance methods)
#     def show(self):
#         print('Name',self.name,'Age:',self.age,'Profession:',self.profession)
    
#     #Behavior (instance methods)
#     def work(self):
#         print(self.name,'working as a',self.profession)

# p1=Person('Khadar',23,'Aademician')
# p1.show()
# p1.work()

#polymorphism is poly is many and morphs : shapes
# poly morphism is a technique when one method attach to function is changes according to the requiment /

# print(len("Hello"))
# print(len([1,2,3,4]))
# print(max(1,3,2))
# print(max("a","z","m"))
# def add(a,b):
#     return a+b

# print(add(3,4))
# print(add("hello","World!"))
# print(add([1,2],[3,4]))




# class Car:
#     def __init__ 



#     def move(self):
#         print("sail!")

# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("fly!")
    
# car1 = Car("Ford","Mustang")
# boat1 = Boat("ibiza","Touring" 20)




# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand= brand
#         self.model= model
    
#     def move(self):
#         print("Move!")
# class Car(Vehicle):
#     pass
# class Boat(Vehicle):
#     pass
# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")

# class Plane(Vehicle):
#     def move(self)
  