def time_convert(x):
  #x = 71

  hour = x // 60
  minutes = x % 60
  time = str(x) + " will be \"" + str(hour) + " hours, " + str(minutes) + " minutes\"." 

  print(time)

time_convert(133)