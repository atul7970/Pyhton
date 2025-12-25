orders = ["cheese", "bread", "wine"]


try:
    print(orders[3])        # Attempt to access an out-of-range index
except IndexError as e:
    print("Error: Tried to access an index that does not exist in the list.")
    print(f"Details: {e}")  
    # Handle the error gracefully
    print("Please check the index and try again.")
    
print("Continuing with the rest of the program...")
