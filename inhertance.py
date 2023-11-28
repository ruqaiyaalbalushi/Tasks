class person:
    
    def __init__(self, name, age):
       self.name= name
       self.age= age
       
    def __str__(self):
        return("hello {} you are {} years old".format(self.name, self.age))
person1 = person("ahmed", 24)
person2 = person("mohammed", 26)
print(person1)
print(person1.name)
print(person1.age)
 
class person:
    num=0
    
    def __init__(self, name, age):
       self.__name= name
       self.__age= age
       #count how many person
       person.num +=1
    def __str__(self):
        return("hello {} you are {} years old".format(self.__name, self.__age))
    def __talk__(self):
        return "{} is talking".format(self.name)
    
    def set_name(self,new_name):
        self.__name=new_name
    def get_name(self):
        print(self.__name)
person1 = person("ahmed", 24)
person2 = person("mohammed", 26)
print(person2)
person2.set_name("Ruqaiya")
person2.get_name()
#print(person.num)
print(person1)

print(person2)"""

"""class person:
    def __init__(self, name, age=22):
        self.name = name
        self.age = age
    def say_hi(self):
        print("hello {} from parent calss".format(self.name))
class student(person):
    def __init(self, name, age = 22):
        super().__init__()
    def say_hi(self):
        print ("hello {} from student class".format(self.name))
p1=person("A", 22)
s1=student("B", 15)
s2=student("Ruqaiya", 26)
s1.say_hi()
p1.say_hi()
s2.say_hi()

#call from another file but should save in same file
    
class student(person):
    def __init(self, name, age = 22):
        super().__init__()
    def say_hi(self):
        print ("hello {} from student class".format(self.name))
p1=person("A", 22)
s1=student("B", 15)
s2=student("Ruqaiya", 26)
s1.say_hi()
p1.say_hi()
s2.say_hi()

def shapes:
    def __init__(self, color, name, area, discription):
        self.color = color
        self.name = name
        self.area = area
        self.disc = disc
    def
    
    
    
    
    
    
    
    
    











































