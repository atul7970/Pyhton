def process_order(item, quantity):
    try:
        price = {"apple": 1.0, "banana": 0.5, "orange": 0.75}[item] # May raise KeyError
        total_cost = price * quantity
        print(f"Total cost for {quantity} {item}(s): ${total_cost:.2f}")
    except KeyError:
        print(f"Error: '{item}' is not available in the inventory.")
    except TypeError:
        print("Error: Quantity must be a number.")

# Test cases
process_order("banana", 5)        # Valid case
process_order("grape", 3)        # KeyError case
process_order("banana", "two")   # TypeError case