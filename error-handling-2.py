#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print ("Finally Error: can\'t find file or read data")
   fh.close()
