def common_letters(str1, str2):
  for i in str1:
    for j in str2:
      if i == j:
        print(i)

# Only caters for same letters, small with small and capital with capital
common_letters("house@45", "computers@56")