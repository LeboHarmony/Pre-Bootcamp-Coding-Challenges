def check_max(x, y, z):
  if(x > y and x > z):
    print(x)
  elif(y > x and y > z):
    print(y)
  else:
    print(z)
  
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

check_max(a, b, c)