a = int(input("First Number : "))
b = int(input("Second Number : "))
if (b >= a):
  largest = b
else:
  largest = a
print("Largest Number You entered is :" , largest)

Shortcut:
------------------------------------------------------------
a = int(input("First Number : "))
b = int(input("Second Number : "))
largest_number = max(a , b)
print("Largest Number You entered is : ", largest_number)

Alternative solution:
------------------------------------------------------------
a = int(input("First Number : "))
b = int(input("Second Number : "))
if (a - b > 0):
  print("The largest num is : ", a)
else:
  print("The largest num is : ", b)
