"""lst=[10,50,20,70,80,40,30]
key=80
lst.sort()
for i in range (len(lst)):
    li=0
    hi=len(lst)-1
#print(lst)"""
    


"""def binary_search(key,lst):
    li ,hi = 0, len(lst)-1
    while(li<=hi):
        mid = (hi+li)//2
        if(lst[mid] == key):
            return mid
        elif(lst[mid]< key):
            li = mid + 1
        else:
            hi=mid - 1
    return -1
num = [10,50,20,70,80,40,30]
num.sort()
target = int(input("Enter a number"))
result = print("Your target is in index",binary_search(target,num) )"""

"""def binary_search(x):
    li ,hi = 1, x
    if(x==1 or x==0):
        return x
    while(li<=hi):
        mid = (hi+li)//2
        if(mid *mid == x):
            return mid
        elif(mid * mid < x):
            li = mid + 1
        else:
            hi=mid - 1
    return -1


num = int(input("Enter a number"))
target = binary_search(num)
print(target)"""
def inseart_sort(array):
    for step in range (1, len(array)):
        kay = array[step]
        j = step - 1
        while j >=0 and key < array[j]:
                array[j+1] = array[j]
                j = j - 1
    
    
    
    
    
    array[j+1]= key
data = [6,2,1,9,8]
inseart_sort(data)
print("sorted data is: ")
print(data)
        












