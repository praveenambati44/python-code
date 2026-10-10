num = int(input("Enter a num: "))
s=0
for i in range(1, num):
        if (num % i == 0):
            s=s+i
if(num==s ):
    print(num," Perfect number")
else:
    print(num," Not a perfect number")
# for positive integer
num = int(input("Enter a num: "))
s=0
for i in range(1, num):
        if (num % i == 0):
            s=s+i
if(num==s and num>0 ):
    print(num," Perfect number")
else:
    print(num," Not a perfect number")