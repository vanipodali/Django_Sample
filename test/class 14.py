import logging

logging.basicConfig(filename='wrapper.log', level=logging.INFO)

def decorator_function(original_function):
    logging.INFO(original_function)
    def wrapper_function(*args,**kwargs):
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display(name,age):
    logging.INFO('display func ran with name {} and age {}'.format(name,age))

@decorator_function
def display_info():
    logging.INFO('display info func ran')

decorated_display=display('kartik',20)
decorated_display_simple=display_info()

logging.INFO(print(wrapper))
logging.INFO(print(wrapper())