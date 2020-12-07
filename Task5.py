from math import sqrt

def area_of_triangle(a, b, c):

  # Calculating the semiperimeter of a triangle
  s = 1 /2 * (a + b + c)
  # Calculating basic area without units
  area = sqrt(s * ((s - a) * (s - b) * (s - c)))
  print("%0.2f" %(area))

area_of_triangle(6, 6, 6)