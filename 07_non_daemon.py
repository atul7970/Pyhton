import threading
import time

def monitor_tea_temp():
    while True:
        time.sleep(2)
        print("Monitoring tea temperature...")


t= threading.Thread(target=monitor_tea_temp)   # Non-daemon thread
t.start()

print("Preparing tea...")
