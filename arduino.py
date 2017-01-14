#install using Pyserial
import serial
import time
import main
def run():
    s = serial.Serial("11", 9600) #port is 11 (for COM12), and baud rate is 9600
    time.sleep(0.5)    #wait for the Serial to initialize"""
    #s.write('Ready...')
    a,b,c = main.main()
    """s.write"""
    if type(a) == str and b == 0 and c == 0:
         s.write(a)
    else:
        s.write("Number of New Posts : " + str(a) + " The Most Recent Post was : <" + b + "> made by : " + c)

