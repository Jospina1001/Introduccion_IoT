import pycom
import time
from network import WLAN
import machine

from dth import DTH
from machine import Pin
from machine import RTC


wlan=WLAN(mode=WLAN.STA)

wlan.connect(ssid='Redmi 9', auth=(WLAN.WPA2, '68031001'))
while not wlan.isconnected():
    machine.idle()

print("WiFi OK")
print(wlan.ifconfig())

rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
time.timezone(2*60**2)

th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),0)


print("Cesar Andres Mendoza")
print("Juan Sebastian Ospina")

i=0
j=0

f=open("Datos.txt","w")
f.close()

pycom.heartbeat(False)
while True: # stop after 10 cycles
    tiempo=time.localtime()


    tim=("{}/{}/{}  {}:{}:{}".format(str(tiempo[0]),str(tiempo[1]),str(tiempo[2]),str(tiempo[3]-7),str(tiempo[4]),str(tiempo[5])))
    print(tim)

    time.sleep(1)

    if(i==10):
        result = th.read()
        
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        if(j==5):
            f=open("Datos.txt","w")
            f.close()
        else:
            f=open("Datos.txt","a")
            f.write("{}/{}/{}  {}:{}:{} \n".format(str(tiempo[0]),str(tiempo[1]),str(tiempo[2]),str(tiempo[3]),str(tiempo[4]),str(tiempo[5])))
            f.write("Temperature: %d C  \n" % result.temperature)
            f.write("Humidity: %d %% \n " % result.humidity)
            f.write("\n")
            f.close()
            j=j+1
        i=0        
    i=i+1
    
