import math
def calculate_circle_area(radius):
    return math.pi*radius**2
def calculate_squire_area( side):
    return side**2
def calculate_rectangle_area(length,width):
    return length * width
def calculate_triangle_area(triangle):
    return 0.5 * base * height

def main():
    print("Select the shape to calculate the area:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
choice=int(input("enter your choice (1/2/3/4)"))

if choice==1:
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print("Area of the circle:", area) 
elif choice==2:
    side=int(input("enter side :")) 
    area=calculate_squire_area(side)
    print("area of squire is:",area) 
elif choice == 3:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print("Area of the rectangle:", area)
elif choice == 4:
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print("Area of the triangle:", area)
else:
        print("Invalid choice!") 


if __name__=="__main__":
    main()
