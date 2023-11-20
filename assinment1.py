#Question 1:
def calculate_grade(r_h, c_c, t_s):
    if r_h > 50 and c_c > 0.7 and t_s > 5600:
        return 10
    elif r_h > 50 and c_c > 0.7:
        return 9
    elif c_c > 0.7 and t_s > 5600:
        return 8
    elif r_h > 50 and t_s > 5600:
        return 7
    else:
        return 0


r_h = float(input("Enter Rockwell hardness: "))
c_c = float(input("Enter carbon content: "))
t_s = float(input("Enter tensile strength (kg/cm2): "))

grade = calculate_grade(r_h, c_c, t_s)
print("Steel Grade:", grade)
#Question2:
T=10000
annual_increase =0.05
years=10

#Question3:
for i in range(1, years+1):
     T*=1+annual_increase


t_10=T

t_4=sum(T*(1+annual_increase)** i for i in range (years, years+1))
print ("Tuition after 10 years :" ,t_10)
print ("Tuition after 4 years  worth of tuition after 10 years :" ,t_4)



# Q3
"""rows = 8
for i in range(rows):
    n=0
    for j in range(i , rows):
        print(" ", end=" ")

    for j in range( i):
        print(format (2**n), end=" ")
        n+=1

    for j in range(i+1):
        print(format (2**n), end=" ")
        n-=1
        
    print()"""








