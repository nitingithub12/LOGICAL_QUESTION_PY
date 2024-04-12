import math

def distance(x1, y1, x2, y2):

    diff_x = x1 - y1
    diff_y = x2 - y2
    square_sum = diff_x ** 2 + diff_y ** 2

    
    distance = math.sqrt(square_sum)
    
    return distance


x1 =float(input("enter x1"))
y1 = float(input("enter y1"))
x2 = float(input("enter x2"))
y2 = float(input("enter y2"))

result = distance(x1, y1, x2, y2)
print("Distance:", result)
