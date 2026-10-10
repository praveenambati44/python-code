
num1 = int(input("Enter a range: "))
num2 = int(input("Enter a end num: "))
for k in range(num1, num2 + 1):
    for i in range(1, k + 1):
        if(i * i == k):
            print("Perfect square: ", k)
            break