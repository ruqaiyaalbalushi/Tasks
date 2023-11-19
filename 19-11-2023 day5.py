

#practic loop:
#Q2:
for i in range (1,6):
    print("*"*i)
for i in range (4,0,-1):
    print("*"*i)


#counting voilt litter
v= "aoeui"
count=0
mass = input("Enter a text: ")
for char1 in mass:
    if(char1 in v):
        count+=1
print(count)

#counting numbers:
n="0,1,2,3,4,5,6,7,8,9"
message=input("Ener a text")
count=0
for char1 in message:
    if (char1 in n):
        count+=1
print(count)

    



#Q3:
#checking the perfect number:
sum = 0

for n in range(1,101) :
    
    for i in range(1, n):
        if n%i == 0:
            sum += i

    if n == sum:
        print(f"{n} is a Perfect number")
    else:
        print(f"{n} is not a Perfect number")
    
#checking the format of valid number
=input("Enter your number in format +123 1234-1234")      
if (len(n)==12):
        n1=n[0:4]
        if (n1[0] == '+'):
            if (n[1: ].isdigit()):
                
                n2= n[4:8]
                n3= n[8:]
                print("Your phone number is: (",
                
                n1,")",n2,"-",n3)
                
            else:
                print("Please enter only number.")
        else:
            print("Please start with +.")
else:
        print("Enter valid lenght")
#random library
import random
x = random.randint
print(x)
#Random number exerrcise
ran= random.randint(1,20)
while(True):
    i=int(input("Enter a number: "))
    if (ran == i):
        print("you Win")
        break
    elif (i < ran):
        print("Go up")
    elif (i > ran):
        print("Go Down")


#Average of grade
sum1=0
n=int(input("Enter the students number :"))
for i in range (1, n+1):
    g=float(input("Enter students grade: "))
    sum1+=g
avg=sum1/n
print("The average grade: ",avg)
# stop or continue exercise
sum1=0
i=1
avg=0
while(True):
    n=input("Enter n to continue or y to stop")
    if (n.lower() == "n"):
        g=float(input("Enter students grade: "))
        sum1+=g
        avg=sum1/i
        i+=1
        continue
    else:
        print("The average grade: ",avg)
        break

#Function

def grade_avg(x):
    sum1=0
    for i in range(1, x+1):
        g=float(input("Enter the grade: "))
        sum1+=g
    avg=sum1/x
    print(avg)
    
grade_avg(2)


#Function to calculate average 
i=int(input("Enter student number: "))
def grade_avg(x):
    sum1=0
    for i in range(1, x+1):
        g=float(input("Enter the grade: "))
        sum1+=g
    avg=sum1/x
    print(avg)
    
grade_avg(i)
#Function to return whether it's an even number or not (Not Return example)
i = int(input("Enter a number : "))
def check_type(n):
    if (n%2 == 0):
        print("Even")
    else:
        print("Odd")
check_type(i)

# Function with return




i=int(input("enter number"))
def check_num (x):
    if(x%2==0):
        return "even"
    else:
        return"odd"
n=check_num(i)
print(n)
# Functions to calculate shapes, in a loop until quit

while(True):
    n=int(input("""Enter a number  to calculate:
                        1. Triangle
                        2. Square
                        3. Circle
                        4. Cylinder
                        5. Exit
                        """))
    if (n == 1):
        triangle=0
        def T_c(t):
            tb=float(input("Enter triangle base : "))
            th=float(input("Enter triangle height : "))
            triangle=(tb*th)/2
            return n
        r1 = T_c(n)
        print("triangle is : ",r1)
        
    elif (n == 2):
        square=0
        def s_c(n2): 
            sw=float(input("Enter square width : "))
            sl=float(input("Enter square length : "))
            square=sw*sl
            return square
        r2=s_c(square)
        print("square is : ",r2)
        
    elif (n == 3):
        circle=0
        def c_c(c):
            pi=3.14
            red=float(input("Enter circle raduis : "))
            circle=pi*(red**2)
            return circle
        r3=c_c(circle)
        print(" circle is : ",r3)
        
    elif (n == 4):
        cylinder=0
        def cyli_c(cylinder):
            pi=3.14
            cylir=float(input("Enter cylinder raduis : "))
            hc=float(input(" Enter Height of the cylinder : "))
            cylinder=(2*pi*(cylir**2))+(2*3.14*cylir*hc)
            return cylinder
        r4=cyli_c(cylinder)
        print("The circle is : ",r4)
        
    elif (n == 5):
        break
        
    else:
        print("Enter a number: ")

    
    























