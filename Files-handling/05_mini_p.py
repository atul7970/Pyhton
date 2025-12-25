class InvalidChaiError(Exception):
    """Custom exception for invalid chai errors."""
    pass

def bill(flavors,cups):
    menu = {"masala": 10, "ginger": 12, "tulsi": 15, "lemon": 8}
    try:
        if flavors not in menu:
            raise InvalidChaiError(f"Invalid chai flavor: {flavors}")
        if not isinstance(cups, int) or cups <= 0:
            raise ValueError("Number of cups must be a positive integer.")
        total = menu[flavors] * cups
        return total
    except InvalidChaiError as e:
        return str(e)
    except ValueError as ve:
        return str(ve)
# Test cases
print(bill("masala", 3))        # Valid case
print(bill("chocolate", 2))     # InvalidChaiError case
print(bill("ginger", -1))       # ValueError case
