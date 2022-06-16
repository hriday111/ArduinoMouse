
import serial
import pyautogui, sys
import time
from pynput.mouse import Button, Controller
c = not True
left,right=0,0
x,y=0,0
l,r=0,0
line =""
mouse = Controller()
ser = serial.Serial('COM3', 9600)
print("connected to: " + ser.portstr)
play=True
def delay(milliseconds):
    time.sleep(milliseconds/1000)
def conf():
    global line,x,y,left,right
    line =str(ser.readline()) 
    line = line.rstrip()
    line = line.replace("'", "")
    line = line.replace("b", "")
    line = line.replace(" ", "")
    line = line.replace("\\r\\n","")
    line=line.split(':')
def ms():
    conf()
    l,r=0,0
    x=-(int(line[0]))*10
    y=-(int(line[1]))*10
    left=(int(line[2]))
    right=(int(line[3]))
    print(line)
    if left==0 and right==1:
        mouse.press(Button.left)
        while l==0:
            conf()
            lTemp=(int(line[2]))
            print(lTemp)
            if lTemp==0:
                mouse.release(Button.left)
                l=1
    if right==0 and left==1:
        mouse.press(Button.right)
        while r==0:
            conf()
            rTemp=(int(line[3]))
            if rTemp==0:
                mouse.release(Button.right)
                r=1
    if right==1 and left==1:
        conf()
        leftT=(int(line[2]))
        rightT=(int(line[3]))
        xT=line[0].replace('-','')
        
        delay(3000)
        if rightT==1 and leftT==1 and xT>'3':
           
            if y>0:
                mouse.scroll(0, 1)
            if y<0:
                mouse.scroll(0, -1)
            x,y=0,0
    mouse.move(x, y)
def control():
    conf()
    #l,r=0,0
    x=-(int(line[0]))
    y=-(int(line[1]))
    left=(int(line[2]))
    right=(int(line[3]))
    #print(line)
    if left==0 and right==1:
        print("prev")
    if right==0 and left==1:
        print("right")
    if right==1 and left==1:
        conf()
        leftT=(int(line[2]))
        rightT=(int(line[3]))
        x=-(int(line[0]))
        delay(1000)
        if rightT==1 and leftT==1 and x>3:
            c=False
        else:
            c=True
        if c==True:
            global play
            if play==True:
                #play=False
                print("Pause")
            elif play==False:
                #play=True
                print("Play")
            play=not play
   
while True:
    ms()
