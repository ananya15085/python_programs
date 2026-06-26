#program with two functions
def add(x,y):#formal  10 25
    """
    This function takes two numbers and find their sum.
    It displays the sum as result.
    """
    print("sum= ", x+y)#35

def message():
    '''
    This function displays a message.
    This is a welcome message to the user.
    '''
    print("welcome to python")

#call the function
x = 10
y = 25
add(x,y) # actual params
message()