







x = int(input("enter a number"))
if (x%2==0):
    input("the number if even")
else :
    input ("the nmber is odd")"""
    
    
"""TA = int(input("Enter total amount"))
if (TA >100):
    discount= TA-(TA*10/100)
    print("10% discount: "+str(discount))
else:
    discount=TA-(TA*5/100)
    print("5% discount: "+str(discount))




#program 2:

gender= input("Enter your gender M OR F: ")

if (gender == 'M'):
    age = int(input("Enter you age:  "))
    if( 24<=  age <=30):
         print("accepted")
    else:
         print ("rejected")
else:
    print ("rejected")

#Time
time1 = int(input("Enter the time1"))
minut1=int(input("enter minut1: "))
p1 =input ("Enter the perioud am or pm")   

time2= int(input("Enter the time2"))
minut2=int(input("enter minut: "))
p2 =input ("Enter the perioud am or pm")


if(p1== "am" and p2 =="pm"):
    print(time1 ,":", minut1 , p1)

elif (p2=="am" and p1=="pm"):
    print(time2 ,":", minut2 , p2)

else:
     if(time1 <= time2):
         if(minut1<=minut2):
             print(time1 ,":", minut1 , p1)
         else:
            print(time2 ,":", minut2 , p2)
     else:
        print(time2 ,":", minut2 , p2)




#bank account:
pin=0
amount=1000
while(True):
    
    
    pin=int(input("Enter pin :"))
    if (pin==1234):
        option=int(input("""choose the option:
          1.check balance
          2.cash withdrwal
          3.deposit money:  """   ))
        if(option == 1):
            print ("your balance in bank is:" + str(amount))
        elif(option == 2):
            withdrwa =int(input("Enter the amout  :"))
            amount=(amount - withdrwa)
            print("your balance is  :" + str(amount))
        elif(option == 3):
            deposit =int(input("Enter the amout  :"))
            amount=(amount + deposit)
            print("your balance is  :" + str(amount))


else:
    print("Enter correct pin")
        


#self study:
a=int(input("Enter fist variable :"))
b=int(input("Enter secnd variable :"))
c=int(input("Enter third variable :"))
if(a >b>c):
    print("the lagest variable is" ,(a))
elif(b>a>c):
    print("the lagest variable is",(b))
elif(c>b>a):
    print("the lagest variable is",(c))
else:
    print("some numbers are equal")


#leap year:
year=int(input("Enter year"))
if(year % 400 == 0) and (year % 100 ==0):
    print(year ," is leap year ")
elif(year % 4 == 0) and (year % 100 !=0):
        print(year,"is leap year ")
else:
    print(year,"is not leap year " )

    


    



