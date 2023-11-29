class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, department, ):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.department = department
    def assign_dep(self,new_dep):
        self.department=new_dep
    def __str__(self):
        #super().__init__()
        return "Employee ID is {} , Employee name is {}, Employee Salary is {}, Employee department is {}".format(self.emp_id,self.emp_name, self.emp_salary,self.department )
    def calc_sal(self,hours):
        
        overtime=0
        overtime_amnt=0
        new_salary
        if(self.hours>50):
            overtime=self.hours-50
            overtime_amnt=(overtime*(emp_salary / 50))
            new_salary=emp_salary+overtime_amnt
            t
            return emp_salary
        else:
            emp_salary
            
            
        
person1 = Employee(122,"ahmed",500,"IT")
print(person1)
person1.assign_dep("ENG")
print(person1)





"""class Math:
    @staticmethod
    def add_numbers(x ,y):
        return x+y
    @staticmethod
    def pi():
        return 3.14
class shape:
    def __init__(self, name, color):
        self.name
        self.color = color
    def area(self, r):
        return 2*Math.pi()*self.r
sh1 = Shape("ca","Red",4)
print
print(Math.add_number)"""









"""class Numbers:
    def __init__(self):
        self.numbers = []
    def add_numbers(self, num):
        self.numbers.append(num)
    def sum_numbers(self):
        summ=0
        for i in self.numbers:
            summ+=i
        return summ
n1 = Numbers()
n1.add_numbers(2)
n1.add_numbers(3)
print(n1.sum_numbers())"""
class Library:
    def __init__(self):
        
        self.library = []
    def add_book(self,title,auther,copies):
        book={"Title":title, "Author":auther,"Copies":copies}
        
        self.library.append(book)
    
    def display(self):
        for i in self.library:
            print(i)
        #return("Auther name is {} book title is {}  book copies are{} ".format(self.book_title, self.book_author,self.book_copies))
        
    def search(self,title):
        for i in self.library:
            if(i["Title"] == title ):
                print(i["Author"])
        
book1=Library()
print(book1)
book1.add_book("math", "ahmed",3)
book1.add_book("m", "ahd",5)
book1.display()
book1.search("math")
