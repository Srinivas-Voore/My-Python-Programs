#decision making or conditional satements

#nested if & elif ladder

a=int(input("Enter a integer value: "));
if a%2==0:
    if a%5==0:
        print(f"{a} is div by 2&5");
    else:
        print(f"{a} is not div by 5");

if(a==1):
    print(f"{a} is 1");
elif(a==2):
    print(f"{a} is 2");
elif(a==5):
    print(f"{a} is 5");
else:
    print(f"{a} is someother number");

