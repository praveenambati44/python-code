n= int(input("Enter a number: "))
i=1
s=0
c=0
while(i<=n):
    if(i%2==0):
        s += i
        c += 1
    i += 1
print("Average ", s/c)
