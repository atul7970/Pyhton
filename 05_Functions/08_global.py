chai_type = "Masala"

def update_order():
    def kitchen():
        global chai_type
        chai_type = "kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()
print("Outside function", chai_type)