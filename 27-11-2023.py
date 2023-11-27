"""matrix1=[[1,2,3],
         [6,7,8]]
matrix2=[[6,1],
         [2,10],
         [0,2]]
res = [[0 for x in range(2)] for y in range(2)]
for i in range (len(matrix1)):
    for j in range (len(matrix2[0])):
        for k in range (len(matrix2)):
         # resulted matrix
            res[i][j] += matrix1[i][k] * matrix2[k][j]
 
print (res)"""
"""file=open("test.txt", "r")
print(file.readline())"""

"""file=open("test.txt", "r")
line=file.readline()
sum1=0
count=1
for line in file:
    
    sum1+= float(line)
    count+=1
print(sum1/count)"""


"""file=open("test1.txt", "r")
for line in file:
    line=line.rsplit(" ")
    print(line)"""

file=open("test1.txt", "r")
for line in file:
    line=line.rsplit(" ")
    print(line[0],"mark is :", line[0])


    
    
   
        
        