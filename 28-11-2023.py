"""try:
    x=[6,2,5,7,2]
    print(x[10])
except ZeroDivisionError:
    print("zero division error")
except



except Exception as exc:
    print("error: ",str(exc))"""
    
try:  
    while(True):
        n=float(input("Enter the number"))
        
        print(int(n))
except Exception as ext:
    print("error is ",type(ext), str(ext))