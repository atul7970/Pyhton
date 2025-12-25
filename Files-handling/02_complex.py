def serve(flavour):
    try:
        print(f"Preparing your {flavour} ice cream.")
        if flavour not in ["vanilla", "chocolate", "strawberry"]:
            raise ValueError("We do not have that flavour.")
    except ValueError as e:
        print("Error: Unable to serve the requested flavour.")
        print(f"Details: {e}")
        print("Please choose a different flavour.")
    else:
        print(f"Here is your {flavour} ice cream. Enjoy!")  
    finally:
        print("Thank you for visiting our ice cream shop!") 

# Test the serve function with different flavours
serve("mango")      # This will raise a ValueError 
serve("chocolate")  # This will be served successfully
