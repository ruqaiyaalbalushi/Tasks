
#for loop
"""n=5
sum1=1
for i in range (1, n+1):
    if(i !=n):
        print(i, end ="x")
    else:
        print(i)
    sum1*=i
print()
print(sum1)"""
#while loop
"""n=5
i=1
sum1=1
while (True):
    if(i !=n):
        print(i, end ="x")
    else:
        print(i)
    sum1*=i
    i+=1
    if(i == n+1):
        break
print()
print(sum1)"""

"""n=int(input("Enter a number"))
i=1
x=2
sum1=0
while(i<=n):
    for j in range(1 , 6)
    
    i+=1
    print(r)"""

#print 2 time n and find the calculation
"""n=int(input("Enter a number"))
sum1=0
result=0
for i in range (1,n+1):
    result = "2"*i
    sum1+=int(result)
    print(result)
print(sum1)"""


"""result=0
correct_ans="abaacb"
ans=input("Enter your answer a,b,a")
for i in range(len(correct_ans)):
    if(ans[i] == correct_ans[i]):
        result+=1
    
print(result, "out of", len(correct_ans))"""
"""def grade_exam(num_question , mark_of_each):
    result=0
    correct_ans=input("Enter the answer for {}".format(num_question))
    ans=input("Enter your answer a,b,a")
    for i in range(len(correct_ans)):
        if(ans[i] == correct_ans[i]):
            result+=mark_of_each
        
    print(result, "out of", len(correct_ans)*mark_of_each)
grade_exam(12, 2)"""

#using function to calculae sum
"""def sum_num(*args):
    sum1=0
    for n in args:
        sum1+=n
    return sum1
result=sum_num(1,2,3)
print(result)"""
#usig main function
"""def main():
    result=sum_num(1,2,3)
    print(result)
def sum_num(*args):
    sum1=0
    for n in args:
        sum1+=n
    return sum1
main()"""

#using main with tow funcions
"""def main():
     print(func1(2), func2(1))
def func1(x):
    num=5
    return x*num
def func2(x):
    i=4
    y=3
    return i*x+y
    
main()"""
#definding num ou of the function:
"""num=5
def main():
     print(func1(2), func2(1))
def func1(x):
    
    return x*num
def func2(x):
    i=4
    y=3
    return i*x+y-num
    
main()"""


#calculate add of sum
"""def add_sum(x):   
    sum1 =0
    while(x !=0):
        sum1+=x%10
        x=x//10
    print(sum1)
add_sum(234)"""
#calculate add of sum with main function
num=5
def main():
     func1(123)
def func1(x):
    sum1 =0
    while(x !=0):
        sum1+=x%10
        x=x//10
    print(sum1)

    
main()









    
    
