from multiprocessing import Process
import time

def take_orders(order):
    print(f"Process for taking {order} started.")
    time.sleep(3)
    print(f"Process for taking {order} completed.")

if  __name__ == '__main__':
    make = [
        Process(target=take_orders, args=(f" Order #{i+1}", ))
         for i in range(3)
    ]
    # Start all processes
    for p in make:
        p.start()

    #wait for all processes to complete
    for p in make:
        p.join()    

    print("All orders taken.")
