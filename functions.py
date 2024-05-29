
def calculate_area(base,height):
    area = 1/2 * base* height 
    return area


base = 10
height = 5
area = calculate_area(base, height)
print(f"The area of the triangle is: {area}")





def print_pattern(n):     
    for i in range(n):
        s = ' '
        for j in range(i+1):
            s = s + '*'
        print(s)

print("Print pattern with input=3")
print_pattern(3)
print("Print pattern with input=4")
print_pattern(4)
print("Print pattern with no input number")
print_pattern(2)

