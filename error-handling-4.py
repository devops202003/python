#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

# Define a function here.
def temp_convert(var):
   try:
      print(var)
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("123")
