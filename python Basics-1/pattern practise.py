n=int(input("Enter n value:")) 
x=65
for i in range(0,n,1):
    for j in range(0,i+1,1):
        ch=chr(x)
        print(ch,end=" ")
    x=x+1
    print(" ")    
