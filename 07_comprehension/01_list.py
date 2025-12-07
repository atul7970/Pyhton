masala = [
    "Masala tea",
    "Masala dosa", 
    "Masala chai",
    "Masala curry",
    "Masala popcorn"
]

masala= [item for item in masala if "tea" in item or "chai" in item]
print(masala)