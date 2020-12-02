def check_three(x, y):
  if((x == 3 or y == 3) and (x + y == 3)):
    print("True")
  else :
    print("False")

n = int(input("Enter a number: "))
m = int(input("Enter a number: "))

check_three(n, m)