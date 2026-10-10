#keep dividing the given number until it becomes 0 and count the number of digits in the given number
n = int(input("Enter a number: "))  
count = 0
while(n > 0):
    n = n // 10
    count += 1
print("The number of digits in the given number is:", count)