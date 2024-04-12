def generate_fibonacci(n):
    fibonacci_series=[0,1]
    for i in range(2,n):
        next_terms=fibonacci_series[-1]+fibonacci_series[-2]
        fibonacci_series.append(next_terms)
    return fibonacci_series
terms=int(input("enter a number"))
if terms<=0:
    print("positive number enter")
else:
     fibonacci_series = generate_fibonacci(terms)
     print("fibonacci is:",fibonacci_series)
    
        
