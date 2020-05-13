#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

try:
   fh = open("testfile1", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()
