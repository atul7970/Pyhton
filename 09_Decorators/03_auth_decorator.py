from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user):
        if not user.get("is_admin", False):
            print("User is not an admin. Access denied.")
            return None
        return func(user)
    return wrapper

@require_admin
def access_admin_panel(user):
    print("Welcome to the admin panel!")
access_admin_panel({"username": "john_doe", "is_admin": True})
access_admin_panel({"username": "vuane_doe", "is_admin": False}) 