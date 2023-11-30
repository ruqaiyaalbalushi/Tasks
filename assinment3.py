
#Q1:
import random
def roll_dice():
    return random.randint(1, 6)

def play_craps():
    point = 0
    roll_sum = roll_dice() + roll_dice()
    print(f"You rolled {roll_sum}")
    if roll_sum in [7, 11]:
        print("You win!")
    elif roll_sum in [2, 3, 12]:
        print("You lose.")
    else:
        point = roll_sum
        print(f"Point is {point}")
        while True:
            roll_sum = roll_dice() + roll_dice()
            print(f"You rolled {roll_sum}")

            if roll_sum == point:
                print("You win!")
                break
            elif roll_sum == 7:
                print("You lose.")
                break
play_craps()
#Q2:
    def index_of_smallest_element(lst):
    
    for i in range(11):
        num=int(input("Ebter numbers"))
        lst.append(num)
    index_of_smallest=lst.index(min(lst))
    print("Index of smallest elements is ",index_of_smallest)
lst=[]
index_of_smallest_element(lst)
print(lst)


#Q3:
def readfloats(lst):
    result = []
    for i in range(10):
         num=int(input("enter a number: "))
         if(num not in result):
             result.append(num)
         
    print(result)
readfloats([])












