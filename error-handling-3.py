#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

filename = "/root/testfile"

try:
   fh = open(filename, "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print ("File has been written and close the file")
      fh.close()
except IOError:
   print ("Error: " + str(filename) + " No such File or Directory")
   print ("{}",format(filename))
