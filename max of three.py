a = int(input("First Number : "))
b = int(input("Second Number : "))
c = int(input("Third Number : "))
largest = a
if (b >= a) and (b >= c):
    largest = b
elif (c >= a) and (c >= b):
    largest = c
else:
    largest = a
print("Largest Number You entered is : ", largest)

Shortcut:
----------------------------------------------------
a = int(input("First Number : "))
b = int(input("Second Number : "))
c = int(input("Third Number : "))
largest_num = max(a, b, c)
print("Largest Number You entered is : ")
