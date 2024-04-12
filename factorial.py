def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
number=int(input("enter a number"))
if number<0:
    print("factorial is note define for -ve number ")
else:
    print("the factorial of",number,"is this:",factorial(number))