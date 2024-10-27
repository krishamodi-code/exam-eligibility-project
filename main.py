n= int(input("Enter the total number of working days: "))
a= int(input("Number of days absent: "))

per= (n-a)/n*100

if per<70: 
  print("You are eligible for writing the exam")
else:
  print("You are not eligible for writing the exam")