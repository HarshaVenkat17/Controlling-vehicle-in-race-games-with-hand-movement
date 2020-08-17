
import cv2
import tkinter as tk
from PIL import Image,ImageTk
import race
class Gaming(object):
    def __init__(self, master, **kwargs):
        l1=tk.Label(text="Game Controls",font=("Helvetica",60,"bold"),activeforeground="white",fg="white",bg="black")
        l1.place(x=415,y=50)
        
        textArr=["Accelerate","Back","Left","Right","Brake","Nitro"]
        op1=tk.Label(text="Accelerate",font=("Helvetica",22,"bold"),width=11,activeforeground="black",activebackground="white",bg="white",fg="black")
        op1.place(x=110,y=200)
        op2=tk.Label(text="Back",font=("Helvetica",22,"bold"),width=11,activeforeground="black",activebackground="white",bg="white",fg="black")
        op2.place(x=110,y=260)
        op3=tk.Label(text="Left",font=("Helvetica",22,"bold"),width=11,activeforeground="black",activebackground="white",bg="white",fg="black")
        op3.place(x=110,y=320)
        op4=tk.Label(text="Right",font=("Helvetica",22,"bold"),width=11,activeforeground="black",activebackground="white",bg="white",fg="black")
        op4.place(x=110,y=380)
        op5=tk.Label(text="Brake",font=("Helvetica",22,"bold"),width=11,activeforeground="black",activebackground="white",bg="white",fg="black")
        op5.place(x=110,y=440)
        op6=tk.Label(text="Nitro",font=("Helvetica",22,"bold"),width=11,activeforeground="black",activebackground="white",bg="white",fg="black")
        op6.place(x=110,y=500)

        choices = ['a','s','d','w','left','down','right','up','space','x']
        
        Var1 = tk.StringVar()
        Var2 = tk.StringVar()
        Var3 = tk.StringVar()
        Var4 = tk.StringVar()
        Var5 = tk.StringVar()
        Var6 = tk.StringVar()
        Var1.set("select")
        Var2.set("select")
        Var3.set("select")
        Var4.set("select")
        Var5.set("select")
        Var6.set("select")
        # Create a option menu
        option1 = tk.OptionMenu(root,Var1,*choices)
        option1.place(x=800,y=200)     
        option2 = tk.OptionMenu(root,Var2,*choices)
        option2.place(x=800,y=260)
        option3 = tk.OptionMenu(root,Var3,*choices)
        option3.place(x=800,y=320)
        option4 = tk.OptionMenu(root,Var4,*choices)
        option4.place(x=800,y=380)
        option5 = tk.OptionMenu(root,Var5,*choices)
        option5.place(x=800,y=440)
        option6 = tk.OptionMenu(root,Var6,*choices)
        option6.place(x=800,y=500)  
                   
        btn4 = tk.Button(text="Submit", bd=8,activeforeground="white",activebackground="black",
                         fg="white",bg="black",width=12, height=1,font=("verdana",15,'bold'),
                         command=lambda:self.perform("Accelerate","Back","Left","Right","Brake","Nitro",Var1,Var2,Var3,Var4,Var5,Var6))
        btn4.place(x=1110,y=620)
        
    def perform(self,*var):
        instr=[]
        control=[]
        for i in range(6):
            cnt=var[i+6].get()
            if cnt!="select":
                instr.append(var[i])
                control.append(cnt)
        race.call(instr,control)
        
root=tk.Tk()
root.title("Game Controls")
pad=10
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo
    
image = Image.open('race1.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image = photo)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-pad,root.winfo_screenheight()-pad))
label.bind('<Configure>', resize_image)
label.pack(fill="both", expand ="yes")
app=Gaming(root)
root.mainloop()

