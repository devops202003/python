#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp3 = Employee("Kishan", 5000)
emp4 = Employee("Chaithanya", 5000)
emp5 = Employee("Manu", 5000)
emp6 = Employee("vivek", 5000)
emp5.displayEmployee()
emp6.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
