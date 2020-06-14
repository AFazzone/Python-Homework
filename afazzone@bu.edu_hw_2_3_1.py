import math

r = eval(input("Enter a length from the center to a vertex: "))
s = 2*r * math.sin(math.pi/5)
area = (3*math.sqrt(3)/2) * s**2
print ("The area of the pentgon is", int(area *100)/100.0)  
