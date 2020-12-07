def time_convert(x):
  #x = 71

  hour = x // 60
  minutes = x % 60
  
  if (hour >  1):
    time_h = str(hour) + " hours"
  else:
    time_h = str(hour) + " hour"

  if(minutes > 1):
    time_m = str(minutes) + " minutes"
  else:
    time_m = str(minutes) + " minute"

  time = f"{x} will be \"{time_h}, {time_m}\"."
  print(time)

time_convert(71)