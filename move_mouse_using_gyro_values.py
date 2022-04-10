
import serial.tools.list_ports
import mouse as ms
import pyautogui as py
serialinst = serial.Serial()
portname = "COM3"
serialinst.baudrate = 9600
serialinst.port = portname
serialinst.open()
senstive = .5
[hi, we] = py.size()
while True:
    if serialinst.in_waiting:
        packet = serialinst.readline()
        packet = packet.decode('utf')
        print(packet)
        oneline = packet.split(",")
        xvalue = float(oneline[3])
        yvalue = float(oneline[4])
        [Xposition, Yposition] = py.position()
        Xposition += ((hi/180)*(yvalue/15))
        Yposition += ((we/180)*(-xvalue/15))
        ms.move(Xposition, Yposition, duration=.002)


