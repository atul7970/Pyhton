# file = open("orders.txt", "w")
# try:
#     file.write("OrderID,Product,Quantity,Price\n")
#     file.write("1001,Apple,10,0.50\n")
# finally:
#     file.close()


with open("orders.txt", "w") as file:
    file.write("1001,Apple,10,0.50\n")
    file.write("1002,Banana,5,0.30\n")
    file.write("1003,Orange,8,0.60\n")
    file.write("1004,Grapes,12,0.80\n")
