import cv2
import numpy as np
import pyautogui

instr=[]
control=[]
(sx,sy)=pyautogui.size()
(camx,camy)=(360,240)
gLB=[60,40,80]
gUB=[102,255,255]
rLB=[150,80,80]
rUB=[190,255,255]
red=(0,0,255)
green=(0,255,0)
colors=[green,red]
contsg=[]
contsr=[]
Functions=["Accelerate","Back","Left","Right","Brake","Nitro"]
Press=["up","down","left","right","space","x"]

kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

pFlag=0
spFlag=0

def call(*controls):
    for i in range(len(controls[0])):
        instr.append(controls[0][i])
        control.append(controls[1][i])
    for i in instr:
        if i in Functions:
            Press[Functions.index(i)]=control[instr.index(i)]
    cam= cv2.VideoCapture(0)
    while True:
        ret, img=cam.read()
        img=cv2.resize(img,(360,220))

        #convert BGR to HSV
        imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        for i in colors:
            if i==green:
                lowerBound=np.array(gLB)
                upperBound=np.array(gUB)
            else:
                lowerBound=np.array(rLB)
                upperBound=np.array(rUB)
            # create the Mask
            mask=cv2.inRange(imgHSV,lowerBound,upperBound)
            #morphology
            maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
            maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
            maskFinal=maskClose
            
            conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            if i==green:
                contsg=conts
            else:
                contsr=conts
            cv2.drawContours(img,conts,-1,(255,0,0),3)
            
            for c in range(len(conts)):
                x,y,w,h=cv2.boundingRect(conts[c])
                cv2.rectangle(img,(x,y),(x+w,y+h),i, 2)
        g=len(contsg)
        r=len(contsr)
        
        if g:
            pos=0
            for i in contsg:
                x,y,w,h=cv2.boundingRect(contsg[0])
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cx=x+w//2
                cy=y+h//2
                cv2.circle(img,(cx,cy),(w+h)//4,(0,0,255),2)
                pos=pos+sx-(cx*sx/camx)
            pos=int(pos/g)
            if pos<456:
                if pFlag!=1:
                    pFlag=1
                    pyautogui.keyUp(Press[3])
                    pyautogui.keyDown(Press[2])
            elif pos>911:
                if pFlag!=0:
                    pFlag=0
                    pyautogui.keyUp(Press[2])
                    pyautogui.keyDown(Press[3])
            else:
                pyautogui.keyUp(Press[3])
                pyautogui.keyUp(Press[2])
                pyautogui.press(Press[0])
        if r:
            if r>=3:
                if spFlag!=1:
                    spFlag=1
                    pyautogui.keyUp(Press[1])
                    pyautogui.keyDown(Press[4])
                    
            elif r==2:
                if spFlag!=0:
                    spFlag=0
                    pyautogui.keyUp(Press[4])
                    pyautogui.keyDown(Press[1])
            else:
                pyautogui.keyUp(Press[1])
                pyautogui.keyUp(Press[4])
                pyautogui.press(Press[5])
        
        cv2.imshow("cam",img)
        key=cv2.waitKey(1)
        if key==27:
            break
    cam.release()
    cv2.destroyAllWindows()
def __init__(self,*controls):
    print("Enjoy your ride")

