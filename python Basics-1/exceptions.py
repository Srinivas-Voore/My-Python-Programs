try:    
    age=int(input("enter age:"))
    income=int(input("enter income:"))
    risk=income/age
    print(age)
    print(risk)
    
except ZeroDivisionError:
    print("cant divide by zero")
except ValueError:
    print("enter a proper integer value")
#exit code 0 => success
#exit code 1 or anything => error
#ValueError => anything in place of integer
#we use exceptions to avoid failure of program
