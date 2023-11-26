"""def reverse_list(my_list:List[str]) ->int:
    my_list.pop()
    return "hi"""
"""new_list =  [8,5,2,3,0,1]
new_list.sort()"""



"""def readfloats(n) :
    result = []
    for i in range(n):
         num=float(input("enter a number: "))
         result.append(num)
    return result     
    
    
def multiplay(ls, factor):
    for i in range (len(ls)):
        ls[i]= ls[i]*factor
    return ls
def print_reverse(ls):
    ls.reverse()
    return ls

    
def main():
    my_list = readfloats(3)
    number = int(input("Enter the factor"))
    new_list = multiplay(my_list , number)
    final_list = print_reverse(new_list)
    print(final_list)
main()"""
"""matrix= [[0,5,1],
         [4,0,0],
         [11,6,7]]

#print(matrix[1][2])
for i in range (len(matrix)):
    for j in range(len(matrix)):
         print(matrix[i][j]*2, end=" ")
    print()"""

"""count=0
matrix= [[0,5,1],
         [4,0,0],
         [11,6,7]]
#print(matrix[1][2])
for i in range (len(matrix)):
    for j in range(len(matrix)):
        if(matrix[i][j] == 0):
            count+=1
print(count)"""

#print(matrix[1][2])
"""for i in range (len(matrix)):
    for j in range(len(matrix)):
         print(matrix[i][j]*2, end=" ")
    print()"""
        
"""matrix1= [[0,5,1],
         [4,9,0],
         [0,6,0]]
matrix2 = [[1,2,3],
           [5,8,1],
           [9,2,6]]
def add(mtrx1, mtrx2):
    new_mtrx = []
    for row in range (len(mtrx1)):
        rows = []
        for clmn in range(len(mtrx1)):
            rows.append(mtrx1[row][clmn]+mtrx2[row][clmn])
        new_mtrx.append(rows)
    print(new_mtrx)
add(matrix1, matrix2)"""


"""n=int(input("inter a number"))
matrix=[]
for i in range(n):
    for j in range(n):
        if(i==j ):
            print(1, end= " ")
        else:
            print(0, end= " ")
    print()"""



"""n=int(input("inter a number"))
matrix=[]
for i in range(n):
    for j in range(n):
        if(i<=j ):
            print(1, end= " ")
        else:
            print(0, end= " ")
    print()"""



"""dic={1: "green", 2:"blue"}
print(dic.get(9,"red"))"""

"""dic={1: "green", 2:"blue"}
print(dic.pop(1))
print(dic)"""


#dictionaries
"""dic = {1:{"name":"ali", "age":23},
       2:{"name":"Ruqaiya","age":22}}
for key1 in dic:
    for key2 in dic[key1]:
        print(dic[key1][key2])
print()"""



"""dic = {1:{"name":"jhon", "age":27, "sex": "male"},
       2:{"name":"marie","age":22, "sex": "female"},
       3:{"name":"sali","age":23, "sex": "female"}}
print("age above 22 are: ")
for i in dic:
    if(dic[i]["age"]>22):
        print(dic[i]["name"])
    
print()"""
#tuple
"""def func(t):
    t=t*2
t=(1,2,3)
print(t)
func(t)
print(t)"""

ls = set([2,5,3,6,7])
ls.add(0)
ls.update((32,45))
print(ls)



    
        


   

    