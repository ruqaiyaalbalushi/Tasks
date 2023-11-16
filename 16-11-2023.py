
start = 1
i = int(input("Enter a number"))
sum1 = 0
while(start<=i):
    sum1+=start
    start+=1
    print(sum1)


i= 0
n = input("enter number")
sum1 = 0
while(i<len(n)):
    sum1+=int(n[i])
    i+=1
print(sum1)

i=0
n=int(input("enter a number "))
sum1 =0
while(n !=0):
    sum1+=n%10
    n=n//10
print(sum1)
    
i=0
n=int(input("enter a number "))
sum1 =0
while(i<=len(str(n))):
    sum1+=n%10
    n=n//10
    i+=1
print(sum1)


i=1
while(i<=6):
    if(i==4):
        i+=1
        continue
    print(i)
    i+=1


message= "|rx#duh#juhdwh"
x=0
while(x<len(message)):
    new= ord(message[x])-3
    print(chr(new), end="")
    x+=1

#for loop

for i in range (1,5):
    print("*"*i)
for i in range (4,0,-1):
    print("*"*i)

x=0
while(True):
    n=int(input("guess the number"))
    
    if(n>19):
    
        print("go down")
    
    
    elif(n<19):
        print("go up")
    
    else:
        print("you win")
        break
    
    
     


