def reverse_string(input_string):
    reverse_string=''
    for i in range(len(input_string)-1,-1,-1):
        reverse_string+=input_string[i]
    return reverse_string
    
input_string=input("enter the string")
result_reverse=reverse_string(input_string)
print("reverse string is ", result_reverse)