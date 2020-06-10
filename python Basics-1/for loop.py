x=[10,20,30]
total=0
for y in x:
    total+=y
print("total is",total)
n=int(input("enter a value:"))
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print("*",end=" ")
    print(" ")    
