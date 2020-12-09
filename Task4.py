def check_three(x, y):

  sum = x + y 

  for i in str(sum):
    if str(3) in str(sum):
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