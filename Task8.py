def time_convert(x):
  #x = 71

  hour = x // 60
  minutes = x % 60
  
  if (hour >  1):
    time_h = str(hour) + " hours"
  elif(hour <=  1):
    time_h = str(hour) + " hour"

  if(minutes > 1):
    time_m = str(minutes) + " minutes"
  elif(minutes <= 1):
    time_m = str(minutes) + " minute"

  time = str(x) + " will be \"" + str(time_h) + ", " + str(time_m) + "\"." 

  print(time)

time_convert(71)