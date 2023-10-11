n = 9
num1 = 0
num2 = 1
next_number = num2  
flag = 1
 
while flag <= n:
    print(next_number, end=" ")
    flag += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
