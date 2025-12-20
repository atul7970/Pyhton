from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done with: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type,milk="no"):
    print(f"Brewing {type} chai with milk {milk}")

brew_chai("Coffee")

@log_activity 
def brew_chai2(type,milk="no"):
    print(f"Brewing {type} chai with milk {milk}")

brew_chai2("Coffee")