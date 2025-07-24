len = int(input("How many numbers do you want : ")) 
num = [] 
for i in range(0,len): 
    element = int(input("Enter element : ")) 
    num.append(element)
total = sum(num) 
average = total/len 
print(" Average of total elements : ", average)

Shortcut:
-----------------------------------------------------
len = int(input("How many numbers do you want : "))
total = 0
for i in range(0,len):
  element = int(input("Enter element : "))
  total += element
average = total/len
print(" Average of total elements : ", average)
