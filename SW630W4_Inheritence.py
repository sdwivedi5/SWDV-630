#!/usr/bin/python
class Contact:
   'Common base class for all Contact'
   CCount = 0

   def __init__(self, name, email):
      self.name = name
      self.email = email
      
      
      Contact.CCount += 1
   
   def displayCount(self):
     print ("Total Contact %d" % Contact.CCount)

   def displayPerson(self):
      print ("Name : ", self.name,  ", Email: ", self.email )


class Employee(Contact):
   'Sub class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


class Customer(Contact):
   'Sub class for all Customer'
   CusCount = 0

   def __init__(self, name, roomno,email):
      self.name = name
      self.email= email
      self.roomno = '001'
      Customer.CusCount += 1
   
   def displayRoomno(self):
     print ("Room no for Customer %d" % self.roomno)
   
   def displayCount(self):
     print ("Total Customer %d" % Customer.CusCount)

   def displayCustomer(self):
       print ( "Name : ", self.name,  ", Email: ", self.email  )


"This would create first object of Employee class"
emp1 = Employee("San1", 2000)
"This would create second object of Employee class"
emp2 = Employee("San2", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
cus1=Customer("Sandeep",201,"Sandeep.dwivedi@yahoo.com")
cus1.displayCustomer()
print ( "Total Employee %d" % Employee.empCount )