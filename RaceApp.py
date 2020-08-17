
import cv2
import tkinter as tk
from PIL import Image,ImageTk

class Gaming(object):
    def __init__(self, master, **kwargs):
        l1=tk.Label(text="Game Controls",font=("Helvetica",60,"bold"),activeforeground="white",fg="white",bg="black")
        l1.place(x=415,y=50)
        l2=tk.Label(text="Select to enable",font=("Helvetica",22,"bold"),activeforeground="white",fg="white",bg="black")
        l2.place(x=110,y=150)
        var1=tk.IntVar()
        var2=tk.IntVar()
        var3=tk.IntVar()
        var4=tk.IntVar()
        var5=tk.IntVar()
        var6=tk.IntVar()
        C1 = tk.Checkbutton(text = "Accelerate", variable = var1,font=("Helvetica",22,"bold"),activeforeground="black",
                            activebackground="white",fg="black",bg="white",onvalue = 1, offvalue = 0, height=1,width = 30)
        C1.place(x=110,y=200)
        C2 = tk.Checkbutton(text = "Back", variable = var2,font=("Helvetica",22,"bold"),activeforeground="black",
                            activebackground="white",fg="black",bg="white",onvalue = 1, offvalue = 0, height=1,width = 30)
        C2.place(x=110,y=260)
        C3 = tk.Checkbutton(text = "Left", variable = var3,font=("Helvetica",22,"bold"),activeforeground="black",
                            activebackground="white",fg="black",bg="white",onvalue = 1, offvalue = 0, height=1,width = 30)
        C3.place(x=110,y=320)
        C4 = tk.Checkbutton(text = "Right", variable = var4,font=("Helvetica",22,"bold"),activeforeground="black",
                            activebackground="white",fg="black",bg="white",onvalue = 1, offvalue = 0, height=1,width = 30)
        C4.place(x=110,y=380)
        C5 = tk.Checkbutton(text = "Brake", variable = var5,font=("Helvetica",22,"bold"),activeforeground="black",
                            activebackground="white",fg="black",bg="white",onvalue = 1, offvalue = 0, height=1,width = 30)
        C5.place(x=110,y=440)
        C6 = tk.Checkbutton(text = "Nitro", variable = var6,font=("Helvetica",22,"bold"),activeforeground="black",
                            activebackground="white",fg="black",bg="white",onvalue = 1, offvalue = 0, height=1,width = 30)
        C6.place(x=110,y=500)
    

        choices = ['select','a','s','d','w','left','down','right','up','space','x']
        #tkvar.set('Select a control') # set the default option
        Var1 = tk.StringVar()
        Var2 = tk.StringVar()
        Var3 = tk.StringVar()
        Var4 = tk.StringVar()
        Var5 = tk.StringVar()
        Var6 = tk.StringVar()
        Var1.set("Select a control")
        Var2.set("Select a control")
        Var3.set("Select a control")
        Var4.set("Select a control")
        Var5.set("Select a control")
        Var6.set("Select a control")
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
                         fg="white",bg="black",width=12, height=1,font=("verdana",15,'bold'), command=lambda:self.perform(var1,var2,var3,var4,var5,var6,Var1,Var2,Var3,Var4,Var5,Var6))
        btn4.place(x=1110,y=620)
        
    def perform(self,*var):
        for i in range(6):
            ch=var[i].get()
            if ch:
                print(ch,var[i+6].get())
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

