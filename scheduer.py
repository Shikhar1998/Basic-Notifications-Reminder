import time
import schedule
import arduino
import os
def call(): 
    arduino.run()
def call1():
    try:
        os.remove("log.txt")
    except IOError:
        pass
call1()
call()
call()
schedule.every(30).minutes.do(call)
while True:
    schedule.run_pending()
    time.sleep(0)

