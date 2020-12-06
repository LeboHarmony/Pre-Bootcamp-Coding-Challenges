def common_letters(str1, str2):
  result = " "
  for i in str1:
    for j in str2:
      if i == j:
        result = result + ", " + i

  # Used slice to ommit the first comma from result
  print("'Common letters:" + result[1:] + "'") 

# Only caters for same letters, small with small and capital with capital
common_letters("house@45", "computers@56")