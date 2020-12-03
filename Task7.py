def temp_celsius_to_fahrenheit(t):
  fahrenheit = (t * 9/5) + 32
  print("%0.0f degrees Fahrenheit" %(fahrenheit))


def temp_fahrenheit_to_celsius(t):
  celsius = (t - 32) * 5/9
  print("%0.0f degrees Celsius" %(celsius))

temp_celsius_to_fahrenheit(0)
temp_fahrenheit_to_celsius(45)