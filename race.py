import cv2
import numpy as np
import pyautogui

def distance(p1,p2):
    return((((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))**0.5)
def drag(p):
    pyautogui.mouseDown()
    pyautogui.moveTo(p[0],p[1])
    pos=pyautogui.position()
    while pos!=p:
        pass
def move(p):
    global rCount
    rCount=0
    pyautogui.moveTo(p[0],p[1])
    pos=pyautogui.position()
    while pos!=p:
        pass   

(sx,sy)=pyautogui.size()
(camx,camy)=(360,240)
#lowerBound=np.array([35,40,80])
#upperBound=np.array([102,255,255])
gLB=[60,40,80]
gUB=[102,255,255]
rLB=[150,80,80]
rUB=[190,255,255]
red=(0,0,255)
green=(0,255,0)
colors=[green,red]
contsg=[]
contsr=[]

cam= cv2.VideoCapture(0)

kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

pFlag=0
spFlag=0

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
            #loc=(int(sx-(cx*sx/camx)),int(cy*sy/camy))
            pos=pos+sx-(cx*sx/camx)
        pos=pos//g
        if pos<456:
            if pFlag!=1:
                pFlag=1
                pyautogui.keyUp("right")
                pyautogui.keyDown("left")
        elif pos>911:
            if pFlag!=0:
                pFlag=0
                pyautogui.keyUp("left")
                pyautogui.keyDown("right")
        else:
            pyautogui.keyUp("left")
            pyautogui.keyUp("right")
            pyautogui.press("up")#keyDown for up
    if r:
        if r>=3:
            if spFlag!=1:
                spFlag=1
                pyautogui.keyUp("down")
                pyautogui.keyDown("space")
                
        elif r==2:
            if spFlag!=0:
                spFlag=0
                pyautogui.keyUp("space")
                pyautogui.keyDown("down")
        else:
            pyautogui.keyUp("space")
            pyautogui.keyUp("down")
            pyautogui.press("x")
    
    cv2.imshow("cam",img)
    key=cv2.waitKey(1)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()

    
