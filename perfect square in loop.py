n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if(i*i==n):
        print("Perfect square")
        break
else:
    print("Not a perfect square")