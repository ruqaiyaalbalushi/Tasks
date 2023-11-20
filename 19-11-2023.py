

#practic loop:
#Q2:
"""for i in range (1,6):
    print("*"*i)
for i in range (4,0,-1):
    print("*"*i)"""


#counting voilt litter
"""v= "aoeui"
count=0
mass = input("Enter a text: ")
for char1 in mass:
    if(char1 in v):
        count+=1
print(count)"""

#counting numbers:
"""n="0,1,2,3,4,5,6,7,8,9"
message=input("Ener a text")
count=0
for char1 in message:
    if (char1 in n):
        count+=1
print(count)"""

    



#Q3:
#checking the perfect number:
sum1 = 0

for num in range(1,101) :
    
    for i in range(1, num):
        if num%i == 0:
            
            sum1+= i

    if(sum1 == num):
        print(f"{num} is a Perfect number")
    sum1=0
    #else:
        #print(f"{num} is not a Perfect number")
        
    

"""n=input("Enter your number")
v = len(n)==14
p=0
while v and p < len(n):
    v= ((p ==0 and n[p] == "+") or
            (p ==4 and n[p] == "") or
            (p == 9 and n[p]=="-") or
            (p !=0 and p !=4 and p !=9 and
            n[p].isdigit()))
    p=+1
if v :
    print(n,"number is valid")
else:
    print("number is not valid")"""
    
    
    
    























