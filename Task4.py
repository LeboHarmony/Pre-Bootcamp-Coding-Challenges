def check_three(x, y):

  sum = x + y 

  for i in str(sum):
    if int(i) == 3:
      z = True
    else:
      z = False

  if((x == 3 or y == 3) and z == True):
    return True
  else:
    return False

n = int(input("Enter a number: "))
m = int(input("Enter a number: "))

print(check_three(n, m))