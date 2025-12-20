from functools import wraps
def my_decorator(fun):
    @wraps(fun)
    def wrapper():
        print("Before function runs")
        fun()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("hello") 

greet()
print(greet.__name__)