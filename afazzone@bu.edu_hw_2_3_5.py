import math

n = eval(input("Enter the number of sides of the polygon: "))
s = eval(input("Enter the length of the side: "))
area = (n*s**2)/(4 * math.tan(math.pi/n))
print ("The area of the polygon is", area)

