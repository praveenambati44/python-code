n = int(input("enter a val of n: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
 #   values in the rectangle

#n = int(input("enter a val of n: "))
#for i in range(1,n):
#    for j in range(1,n):
#        if i==1 or i==n-1 or j==1 or j==n-1:
#            print(j,end=" ")
#        else:#
#            print(" ",end=" ")    
#    print()           


#make values in the equilateral triangular shape
#n = int(input("enter a val of n: "))
#for i in range(1,n+1):
#    for j in range(1,n-i+1):
#        print(" ",end=" ")
#    for k in range(1,i+1):
#        print(k,end=" ")
#     print()



# n = int(input("enter a val of n: "))
# for i in range(n):
#     print(" "*(n-i-1),end=" ")
#     print("*"*(2*i-1))