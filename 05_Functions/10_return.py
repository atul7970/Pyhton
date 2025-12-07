def make_chai():
    #return "Masala Chai"
    print("Making Masala Chai")

return_value = make_chai()
print("Return value:", return_value)    


#One Value
def sold_cups():
    return 10
cups = sold_cups()
print("Cups sold:", cups)


#Multiple Value
def chai_report():
    return 100,20
sold, remaining = chai_report()
print("Cups sold:", sold)
print("Cups remaining:", remaining) 



#Early from function
def chai_status(cups_left):
    if cups_left == 0:
        return "Running Low"
    return "Sufficient"
print("Chai status:", chai_status(0))
print("Chai status:", chai_status(5))


def idle_chaiwala():
    pass

print("Idle chaiwala return:", idle_chaiwala())