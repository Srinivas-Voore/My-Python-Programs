#Exception Handling
'''
def divide(x,y):
    try:
        result=x//y;
        print('neeku kavalsindi naadeggara undi anduko oo jithu :',result)
    except ZeroDivisionError:
        print('dengey naa deggara ledu answer 0 tho divide chesi chacchav')

divide(3,0);
'''

        
        
#Else clause:

'''
def divide(x,y):
    try:
        result=x//y;
        print('neeku kavalsindi naadeggara undi anduko oo jithu :',result)
    except ZeroDivisionError:
        print('dengey naa deggara ledu answer 0 tho divide chesi chacchav')
    else:
        print('try sakkanga execute ayinadi rajaaa')

divide(3,2);
'''

#Raising Exceptions


try:
    raise NameError("hii");
except NameError:
    print("An exception");
    raise
