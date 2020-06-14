mport math

#  Latitude is X, Longitude is Y
 
#Atlanta (x1,y1)

x1 = 33.7489954 
y1 = -84.3879824
 
#Orlando (x2,y2)

x2 = 28.5383355 
y2 = -81.3792365

#Savannah (x3,y3)

x3 = 32.0835407 
y3= -81.0998342
 
#Charlotte (x4,y4)

x4 = 35.2270869
y4= -80.84312667
 
# Compute the length of the three sides of Triangle 1

# Atlanta to Orlando
t1_side1 = 6371.01 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
      math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * 
      math.cos(math.radians(y1 - y2)))

#Atlanta to Savannah
t1_side2 = 6371.01 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x3)) +
      math.cos(math.radians(x1)) * math.cos(math.radians(x3)) * 
      math.cos(math.radians(y1 - y3)))

#Savannah to Orlando
t1_side3 = 6371.01 * math.acos(math.sin(math.radians(x2)) * math.sin(math.radians(x3)) +
      math.cos(math.radians(x2)) * math.cos(math.radians(x3)) * 
      math.cos(math.radians(y2 - y3)))
                              
 
t1_s = ((t1_side1 + t1_side2 + t1_side3) / 2)
t1_area = (t1_s * (t1_s - t1_side1) * (t1_s - t1_side2) * (t1_s - t1_side3)) ** 0.5
 
# Compute the length of the three sides of Triangle 2
#Altanta to Charlotte
t2_side1 = 6371.01 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x4)) +
      math.cos(math.radians(x1)) * math.cos(math.radians(x4)) * 
      math.cos(math.radians(y1 - y4)))

#Atlanta to Savannah
t2_side2 = 6371.01 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x3)) +
      math.cos(math.radians(x1)) * math.cos(math.radians(x3)) * 
      math.cos(math.radians(y1 - y3)))

#Savannah to Charlotte
t2_side3 = 6371.01 * math.acos(math.sin(math.radians(x4)) * math.sin(math.radians(x3)) +
      math.cos(math.radians(x4)) * math.cos(math.radians(x3)) * 
      math.cos(math.radians(y4 - y3)))
                              

t2_s = ((t2_side1 + t2_side2 + t2_side3) / 2)
t2_area = (t2_s * (t2_s - t2_side1) * (t2_s - t2_side2) * (t2_s - t2_side3)) ** 0.5
 
total_area = t1_area  + t2_area
 
print("The area enclosed by Atlanta, Orlando, Charlotte, and Savannah is: ", round(total_area, 2) , \
      " kilometers")


