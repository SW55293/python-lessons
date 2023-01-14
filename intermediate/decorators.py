#decorators extend the behaviour of the function without modifying it
#Basically its just a wrapper function
def taylor_decorator(func):

    def decorator_wrapper():
    #Code to run before the function
        print('Can I ask you a question?') 
        func()
    #Code to run after the function
        print('In the middle of the night')

    return decorator_wrapper

@taylor_decorator
def question():
    print('Did you leave your house ')

question()