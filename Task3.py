def check_65(x, y):
  if(x == 65 or y == 65 or (x + y == 65)):
    return True
  else :
    return False

n = int(input("Please enter first valid number: "))
m = int(input("Please enter second valid number: "))

print(check_65(n, m))