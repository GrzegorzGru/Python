#Receinve input from user: two points in plane (x, y coordinates)
#Find its middle. Calculate radius of  circle, which this line is diameter.
#Calculate area and circumference of this circle.
#*Try to calculate are and circumference of rectangle, which this line is hypotenuse.
from math import sqrt, pi

x1 = float(input('Enter first coordinate (x) '))
y1 = float(input('Enter first coordinate (y) '))
x2 = float(input('Enter second coordinate (x) '))
y2 = float(input('Enter second coordinate (y) '))

#Calculate lenght of line
lenght = sqrt( ( x2 - x1 ) ** 2 + ( y2 - y1 ) ** 2 )

#Calculate coordinates of the middle of the line
middle_x = ( x1 + x2 ) / 2
middle_y = ( y1 + y2 ) / 2

#Calculate radius of circle, which this line is diameter
radius = lenght / 2

#Calculate area and circumference of this circle
circle_area = pi * radius ** 2
circle_circumference = 2 * pi * radius

#Calculate circumference of rectangle described on this line
rectangle_hypotenuse = lenght

#Rectangle points in plane coordinates
rectangle_a_x = x2
rectangle_a_y = y1
rectangle_b_x = x1
rectangle_b_y = y2

#Rectangle sides lenght
rectangle_lenght_a = sqrt( ( rectangle_a_x - x2 ) ** 2 + ( rectangle_a_y - y2 ) ** 2 )
rectangle_lenght_b = sqrt( ( rectangle_b_x - x2 ) ** 2 + ( rectangle_b_y - y2 ) ** 2 )

#Rectangle perimeter and area
rectangle_perimeter = ( rectangle_lenght_a * 2 ) + ( rectangle_lenght_b * 2 )
rectangle_area = rectangle_lenght_a * rectangle_lenght_b

print(f'The line is {lenght:.2f} units long. The middle is in the coordinates x = {middle_x}, y = {middle_y}.\n'
      f'Circle described around a line segment have radius of {radius:.2f} units.\n'
      f'Circle area is {circle_area:.2f} square units\n'
      f'Circle circumference is {circle_circumference:.2f} units\n'
      f'Rectangle described on hypontenuse have sides of size {rectangle_lenght_a:.2f} and {rectangle_lenght_b:.2f} units\n'
      f'The perimeter of rectangle is {rectangle_perimeter:.2f} units \n'
      f'The area of rectangle is {rectangle_area:.2f} units.')