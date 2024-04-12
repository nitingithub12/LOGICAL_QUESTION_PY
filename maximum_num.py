def find_maximum(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
num_1=float(input("enter a number 1st "))
num_2=float(input("enter a number 2nd"))
num_3=float(input("enter a number 3rd"))

maximum=find_maximum(num_1,num_2,num_3)
print("maximum number is ",maximum)