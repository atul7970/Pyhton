class OutOfIngredientsError(Exception):
    """Custom exception raised when there are not enough ingredients to prepare a dish."""
    pass

def prepare_dish(ingredients, required_ingredients):
    """
    Prepares a dish if there are enough ingredients.

    :param ingredients: A dictionary with ingredient names as keys and their quantities as values.
    :param required_ingredients: A dictionary with required ingredient names as keys and their required quantities as values.
    :raises OutOfIngredientsError: If there are not enough ingredients to prepare the dish.
    """
    for item, required_quantity in required_ingredients.items():
        if ingredients.get(item, 0) < required_quantity:
            raise OutOfIngredientsError(f"Not enough {item} to prepare the dish.")
    
    # If all ingredients are sufficient, proceed to prepare the dish
    for item, required_quantity in required_ingredients.items():
        ingredients[item] -= required_quantity
    
    print("Dish prepared successfully!")

# Test cases
ingredients_stock = { "tomato": 5, "cheese": 2, "dough": 1}
required_for_pizza = {"tomato": 3, "cheese": 2, "dough": 1}     

try:
    prepare_dish(ingredients_stock, required_for_pizza) 
except OutOfIngredientsError as e:
    print(e)         


           
# Test case with insufficient ingredients
required_for_salad = {"tomato": 4, "cheese": 1}     
try:
    prepare_dish(ingredients_stock, required_for_salad)     
except OutOfIngredientsError as e:
    print(e)
