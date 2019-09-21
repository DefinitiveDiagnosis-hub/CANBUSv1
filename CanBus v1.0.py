from tkinter import *
import tkinter
import tkinter as tk
import time
import os
import sys
import webbrowser


import glenn01_support

def resource_path(relative_path):   
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.2, height*0.2))
image_file = resource_path("one.gif")
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.5, width=width*0.5, bg="black")
canvas.create_image(width*0.5/2, height*0.5/2, image=image)
canvas.pack()
root.after(5000, root.destroy)
root.mainloop()
def webPage():
    webbrowser.open("https://en.wikipedia.org/wiki/CAN_bus")
def youTube():
    webbrowser.open("https://www.youtube.com/channel/UCyZxb9mtrkIakqtIv2WpFnw")
def howThisWorks():
    webbrowser.open("https://www.youtube.com/channel/UCyZxb9mtrkIakqtIv2WpFnw")
def button1():
   
    imagelist = ["oh01.gif","oh02.gif","oh03.gif",
             "oh04.gif","oh05.gif","oh06.gif","oh07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button2():
   
    imagelist = ["sp01.gif","sp02.gif","sp03.gif",
             "sp04.gif","sp05.gif","sp06.gif","sp07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button3():
   
    imagelist = ["sgl01.gif","sgl02.gif","sgl03.gif",
             "sgl04.gif","sgl05.gif","sgl06.gif","sgl07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button4():
   
    imagelist = ["lth01.gif","lth02.gif","lth03.gif",
             "lth04.gif","lth05.gif","lth06.gif","lth07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button5():
   
    imagelist = ["term01.gif","term02.gif","term03.gif",
             "term04.gif","term05.gif","term06.gif","term07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 1000):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
def button6():
   
    imagelist = ["hr01.gif","hr02.gif","hr03.gif",
             "hr04.gif","hr05.gif","hr06.gif","hr07.gif"]
    
    r = Toplevel()
    canvas4 = Canvas(r, width = 1280, height = 720)
    photo = PhotoImage(file=resource_path(imagelist[0]))   
    width = photo.width()
    height = photo.height()
    
    canvas4.pack(expand = YES, fill = BOTH)

    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=resource_path(imagefile))
        giflist.append(photo)


    for k in range(0, 7):
        for gif in giflist:
            canvas4.delete(ALL)
            canvas4.create_image(width/2.0, height/2.0, image=gif)
            canvas4.update()
            time.sleep(0.1)
 

def vp_start_gui():
    
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    glenn01_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    glenn01_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
g = 0
class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 

        fname =file=resource_path("1225.png")#"1225.png"
        bg_image = tk.PhotoImage(file=fname)
        self.Canvas1 = tk.Canvas(top)
        startframe = tk.Frame(root)
        tk.Canvas(startframe, width=1280, height=800)
        startframe.pack()
        self.Canvas1.pack()
        root.bg_image = bg_image  
        self.Canvas1.create_image((0, 0), image=bg_image, anchor='nw')
        w = bg_image.width()
        h = bg_image.height()
        top.geometry('%dx%d+0+10' % (w,h))        
        top.overrideredirect(True)
        top.title("New Toplevel")
        top.configure(background="#000000")
        self.Canvas1.place(relx=-0.004, rely=-0.006, relheight=1.016, relwidth=1.003)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=1203)

        self.Canvas1.create_text(540, 215, fill="#42f5d7", text=" °C", font=("Arial", 9))
        self.Canvas1.create_text(530, 335, fill="#42f5d7", text="GEAR", font=("Arial", 9))
        self.Canvas1.create_text(480, 375, fill="#42f5d7", text="Coolant", font=("Arial", 9))
        self.Canvas1.create_text(580, 375, fill="#42f5d7", text="Oil", font=("Arial", 9))
        self.Canvas1.create_text(290, 320, fill="#42f5d7", text="MPH", font=("Arial", 12))
        self.Canvas1.create_text(750, 320, fill="#42f5d7", text="RPM", font=("Arial", 12))
     
        def coolant(coolant_: int = 0):
            coolant_ = int(coolant_) 
            self.Canvas1.delete("tag1")      
            self.Canvas1.create_text (465, 345, text=coolant_, fill="#42f5d7", anchor='nw', font=("Arial", 16),tag="tag1")
            self.Canvas1.create_text(1090, 120, fill="#42f5d7", text="0x6E 0xC 0x1F        0x00 0x00 0x00 0x00", font=("Arial", 10),tag="tag1")     
            self.Canvas1.create_text(1074, 127, fill="white", text=hex(coolant_), anchor='s', font=("Arial Bold", 10), tag="tag1")

        self.Scale1 = tk.Scale(top,command=coolant, from_=0.0, to=99.0)
        self.Scale1.place(relx=0.008, rely=0.861, relwidth=0.08, relheight=0.0
                , height=41, bordermode='ignore')
        self.Scale1.configure(activebackground="#39ede1")
        self.Scale1.configure(background="#000000")
        self.Scale1.configure(borderwidth="0")
        self.Scale1.configure(font="TkTextFont")
        self.Scale1.configure(foreground="#ffffff")
        self.Scale1.configure(highlightbackground="#000000")
        self.Scale1.configure(highlightcolor="black")
        self.Scale1.configure(highlightthickness="0")
        self.Scale1.configure(orient="horizontal")
        self.Scale1.configure(troughcolor="#200fbc")
        self.Scale1.configure(width=8)
        coolant_:object = self.Scale1.get()

        def oil(oil_: int = 0):
            oil_ = int(oil_) 
            self.Canvas1.delete("tag2")
            self.Canvas1.create_text (570, 345, text=oil_, fill="#42f5d7", anchor='nw', font=("Arial", 16),tag="tag2")
            self.Canvas1.create_text(1090, 150, fill="#42f5d7", text="0x6E 0xC 0x C        0x00 0x00 0x00 0x00", font=("Arial", 10),tag="tag2")
            self.Canvas1.create_text(1074, 157, fill="white", text=hex(oil_), anchor='s', font=("Arial Bold", 10), tag="tag2")
        
        self.Scale2 = tk.Scale(top,command=oil, from_=0.0, to=99.0)
        self.Scale2.place(relx=0.008, rely=0.917, relwidth=0.08, relheight=0.0
                , height=41, bordermode='ignore')
        self.Scale2.configure(activebackground="#39ede1")
        self.Scale2.configure(background="#000000")
        self.Scale2.configure(borderwidth="0")
        self.Scale2.configure(font="TkTextFont")
        self.Scale2.configure(foreground="#ffffff")
        self.Scale2.configure(highlightbackground="#d9d9d9")
        self.Scale2.configure(highlightcolor="black")
        self.Scale2.configure(highlightthickness="0")
        self.Scale2.configure(orient="horizontal")
        self.Scale2.configure(troughcolor="#200fbc")
        self.Scale2.configure(width=8)
        oil_:object = self.Scale2.get()

        def rpm(rpm_: int = 0):
            rpm_ = int(rpm_) 
            self.Canvas1.delete("tag3")
            self.Canvas1.create_text (710, 260, text=rpm_, fill="#42f5d7", anchor='nw', font=("Arial", 40),tag="tag3")
            self.Canvas1.create_text(1095, 180, fill="#42f5d7", text="0x6E 0xC 0x44           0x00 0x00 0x00 0x00", font=("Arial", 10),tag="tag3")
            self.Canvas1.create_text(1076, 187, fill="white", text=hex(rpm_), anchor='s', font=("Arial Bold", 10), tag="tag3")
                
        self.Scale3 = tk.Scale(top,command=rpm, from_=0.0, to=9000.0)
        self.Scale3.place(relx=0.008, rely=0.813, relwidth=0.078, relheight=0.0
                , height=37, bordermode='ignore')
        self.Scale3.configure(activebackground="#39ede1")
        self.Scale3.configure(background="#000000")
        self.Scale3.configure(borderwidth="0")
        self.Scale3.configure(font="TkTextFont")
        self.Scale3.configure(foreground="#ffffff")
        self.Scale3.configure(highlightbackground="#000000")
        self.Scale3.configure(highlightcolor="black")
        self.Scale3.configure(highlightthickness="0")
        self.Scale3.configure(orient="horizontal")
        self.Scale3.configure(troughcolor="#200fbc")
        self.Scale3.configure(width=8)
        rpm_:object = self.Scale3.get()

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.09, rely=0.826, height=31, width=119)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''CRANK SPEED''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.09, rely=0.882, height=31, width=136)
        self.Label2.configure(background="#000000")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''COOLANT TEMP''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.098, rely=0.931, height=31, width=82)
        self.Label3.configure(background="#000000")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''OIL TEMP''')

        def mph(mph_: int = 0):
            mph_ = int(mph_) 
            self.Canvas1.delete("tag4")
            self.Canvas1.create_text (260, 260, text=mph_, fill="#42f5d7", anchor='nw', font=("Arial", 40),tag="tag4")
            self.Canvas1.create_text(1092, 210, fill="#42f5d7", text="0x1F 0xC 0x33         0x00 0x00 0x00 0x00", font=("Arial", 10),tag="tag4")
            self.Canvas1.create_text(1076, 217, fill="white", text=hex(mph_), anchor='s', font=("Arial Bold", 10), tag="tag4")

        self.Scale3_1 = tk.Scale(top,command=mph, from_=0.0, to=210.0)
        self.Scale3_1.place(relx=0.273, rely=0.813, relwidth=0.078, relheight=0.0, height=37, bordermode='ignore')
        self.Scale3_1.configure(activebackground="#39ede1")
        self.Scale3_1.configure(background="#000000")
        self.Scale3_1.configure(borderwidth="0")
        self.Scale3_1.configure(font="TkTextFont")
        self.Scale3_1.configure(foreground="#ffffff")
        self.Scale3_1.configure(highlightbackground="#000000")
        self.Scale3_1.configure(highlightcolor="black")
        self.Scale3_1.configure(highlightthickness="0")
        self.Scale3_1.configure(orient="horizontal")
        self.Scale3_1.configure(troughcolor="#200fbc")
        self.Scale3_1.configure(width=8)
        mph_:object = self.Scale3_1.get()

        def amb(amb_: int = 0):
            amb_ = int(amb_) 
            self.Canvas1.delete("amb")
            self.Canvas1.create_text (515, 205, text=amb_, fill="#42f5d7", anchor='nw', font=("Arial", 12),tag="amb")
            self.Canvas1.create_text(1092, 330, fill="#42f5d7", text="0x64 0xC 0x44         0x00 0x00 0x00 0x00", font=("Arial", 10),tag="amb")
            self.Canvas1.create_text(1076, 337, fill="white", text=hex(amb_), anchor='s', font=("Arial Bold", 10), tag="amb")
        
        self.Scale3_2 = tk.Scale(top,command=amb, from_=0.0, to=50.0)
        self.Scale3_2.place(relx=0.523, rely=0.813, relwidth=0.078, relheight=0.0
                , height=37, bordermode='ignore')
        self.Scale3_2.configure(activebackground="#39ede1")
        self.Scale3_2.configure(background="#000000")
        self.Scale3_2.configure(borderwidth="0")
        self.Scale3_2.configure(font="TkTextFont")
        self.Scale3_2.configure(foreground="#ffffff")
        self.Scale3_2.configure(highlightbackground="#000000")
        self.Scale3_2.configure(highlightcolor="black")
        self.Scale3_2.configure(highlightthickness="0")
        self.Scale3_2.configure(orient="horizontal")
        self.Scale3_2.configure(troughcolor="#200fbc")
        self.Scale3_2.configure(width=8)
        amb_:object = self.Scale3_2.get()

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.355, rely=0.833, height=31, width=139)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#000000")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(foreground="#ffffff")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''VEHICLE SPEED''')
        self.Label1_3.configure(width=139)
       
        def gearUp():
            global  g
            if g<6:
                g=g+1
                self.Canvas1.delete("gearUp")
                self.Canvas1.create_text(530, 337, fill="#42f5d7", text=g, anchor='s', font=("Arial", 45),tag="gearUp")
                self.Canvas1.create_text(1092, 300, fill="#42f5d7", text="0x1F 0xC 0x03         0x00 0x00 0x00 0x00", font=("Arial", 10),tag="gearUp")
                self.Canvas1.create_text(1076, 307, fill="white", text=hex(g), anchor='s', font=("Arial Bold", 10), tag="gearUp")
                
        self.Button1 = tk.Button(top,command=gearUp)
        self.Button1.place(relx=0.273, rely=0.882, height=32, width=38)
        self.Button1.configure(activebackground="#39ede1")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#092bd8")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''+''')
        self.Button1.configure(width=38)

        def gearDn():
            global  g
            if g>1:
                g=g-1
                self.Canvas1.delete("gearUp")
                self.Canvas1.create_text(530, 337, fill="#42f5d7", text=g, anchor='s', font=("Arial", 45),tag="gearUp")
                self.Canvas1.create_text(1092, 300, fill="#42f5d7", text="0x1F 0xC 0x03         0x00 0x00 0x00 0x00", font=("Arial", 10),tag="gearUp")
                self.Canvas1.create_text(1076, 307, fill="white", text=hex(g), anchor='s', font=("Arial Bold", 10), tag="gearUp")
                
        self.Button1_5 = tk.Button(top,command=gearDn)
        self.Button1_5.place(relx=0.316, rely=0.882, height=32, width=38)
        self.Button1_5.configure(activebackground="#39ede1")
        self.Button1_5.configure(activeforeground="#000000")
        self.Button1_5.configure(background="#092bd8")
        self.Button1_5.configure(disabledforeground="#a3a3a3")
        self.Button1_5.configure(foreground="#ffffff")
        self.Button1_5.configure(highlightbackground="#d9d9d9")
        self.Button1_5.configure(highlightcolor="black")
        self.Button1_5.configure(pady="0")
        self.Button1_5.configure(text='''-''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.355, rely=0.889, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''GEAR SELECTOR''')
        self.Label1_4.configure(width=139)

        def parkOn():
            self.Canvas1.delete("parkOff")
            self.Canvas1.create_text(1092, 270, fill="#42f5d7", text="0x64 0xF 0x00         0x00 0x00 0x00 0x00", font=("Arial", 10),tag="parkOn")
            self.Canvas1.create_text(1076, 277, fill="white", text="0x01", anchor='s', font=("Arial Bold", 10), tag="parkOn")

        self.Button1_6 = tk.Button(top,command = parkOn)
        self.Button1_6.place(relx=0.523, rely=0.882, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''ON''')
        self.Button1_6.configure(width=98)

        def parkOff():
            self.Canvas1.delete("parkOn")
            self.Canvas1.create_rectangle(510, 410, 555, 435, fill='black',tag="parkOff")
            self.Canvas1.create_text(1092, 270, fill="#42f5d7", text="0x64 0xF 0x00         0x00 0x00 0x00 0x00", font=("Arial", 10),tag="parkOff")
            self.Canvas1.create_text(1076, 277, fill="white", text="0x00", anchor='s', font=("Arial Bold", 10), tag="parkOff")
            
        self.Button1_6 = tk.Button(top,command = parkOff)
        self.Button1_6.place(relx=0.57, rely=0.882, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''OFF''')
        self.Button1_6.configure(width=98)

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.609, rely=0.833, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''AMBIENT TEMP''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.609, rely=0.889, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''PARKING BRAKE''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.605, rely=0.938, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''DOOR LOCKS''')

        doorOpen = ('Doors Unlocked')
        def DoorOpen(do_: int = 50):
            rpm_ = int(do_) 
            self.Canvas1.delete("tagclosed","tagopen")
            self.Canvas1.create_text(530, 250, fill="#42f5d7", text=doorOpen, font=("Arial", 12),tag="tagopen")
            self.Canvas1.create_text(1092, 240, fill="#42f5d7", text="0x64 0xF 0x11         0x00 0x00 0x00 0x00", font=("Arial", 10),tag="tagopen")
            self.Canvas1.create_text(1076, 247, fill="white", text=hex(do_), anchor='s', font=("Arial Bold", 10), tag="tagopen")
        
        self.Button1_6 = tk.Button(top,command=DoorOpen)
        self.Button1_6.place(relx=0.523, rely=0.938, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''O''')
        
        doorClosed = ('Doors Locked')
        def DoorClosed(dc_: int = 12):
            rpm_ = int(dc_) 
            self.Canvas1.delete("tagopen","tagclosed")
            self.Canvas1.create_text(530, 250, fill="#42f5d7", text=doorClosed, font=("Arial", 12),tag="tagclosed")
            self.Canvas1.create_text(1092, 240, fill="#42f5d7", text="0x64 0xF 0x11         0x00 0x00 0x00 0x00", font=("Arial", 10),tag="tagclosed")
            self.Canvas1.create_text(1076, 247, fill="white", text=hex(dc_), anchor='s', font=("Arial Bold", 10), tag="tagclosed")
            
        self.Button1_6 = tk.Button(top,command=DoorClosed)
        self.Button1_6.place(relx=0.57, rely=0.938, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''C''')

        self.Button1_7 = tk.Button(top,command=button5)
        self.Button1_7.place(relx=0.742, rely=0.889, height=32, width=98)
        self.Button1_7.configure(activebackground="#39ede1")
        self.Button1_7.configure(activeforeground="#000000")
        self.Button1_7.configure(background="#092bd8")
        self.Button1_7.configure(disabledforeground="#a3a3a3")
        self.Button1_7.configure(foreground="#ffffff")
        self.Button1_7.configure(highlightbackground="#d9d9d9")
        self.Button1_7.configure(highlightcolor="black")
        self.Button1_7.configure(pady="0")
        self.Button1_7.configure(text='''5''')

        self.Button1_8 = tk.Button(top,command=button4)
        self.Button1_8.place(relx=0.742, rely=0.833, height=32, width=98)
        self.Button1_8.configure(activebackground="#39ede1")
        self.Button1_8.configure(activeforeground="#000000")
        self.Button1_8.configure(background="#092bd8")
        self.Button1_8.configure(disabledforeground="#a3a3a3")
        self.Button1_8.configure(foreground="#ffffff")
        self.Button1_8.configure(highlightbackground="#d9d9d9")
        self.Button1_8.configure(highlightcolor="black")
        self.Button1_8.configure(pady="0")
        self.Button1_8.configure(text='''4''')

        self.Button1_8 = tk.Button(top,command=button3)
        self.Button1_8.place(relx=0.742, rely=0.778, height=32, width=98)
        self.Button1_8.configure(activebackground="#39ede1")
        self.Button1_8.configure(activeforeground="#000000")
        self.Button1_8.configure(background="#092bd8")
        self.Button1_8.configure(disabledforeground="#a3a3a3")
        self.Button1_8.configure(foreground="#ffffff")
        self.Button1_8.configure(highlightbackground="#d9d9d9")
        self.Button1_8.configure(highlightcolor="black")
        self.Button1_8.configure(pady="0")
        self.Button1_8.configure(text='''3''')

        self.Button1_8 = tk.Button(top,command=button2)
        self.Button1_8.place(relx=0.742, rely=0.722, height=32, width=98)
        self.Button1_8.configure(activebackground="#39ede1")
        self.Button1_8.configure(activeforeground="#000000")
        self.Button1_8.configure(background="#092bd8")
        self.Button1_8.configure(disabledforeground="#a3a3a3")
        self.Button1_8.configure(foreground="#ffffff")
        self.Button1_8.configure(highlightbackground="#d9d9d9")
        self.Button1_8.configure(highlightcolor="black")
        self.Button1_8.configure(pady="0")
        self.Button1_8.configure(text='''2''')

        self.Button1_8 = tk.Button(top,command=button1)
        self.Button1_8.place(relx=0.742, rely=0.667, height=32, width=98)
        self.Button1_8.configure(activebackground="#39ede1")
        self.Button1_8.configure(activeforeground="#000000")
        self.Button1_8.configure(background="#092bd8")
        self.Button1_8.configure(disabledforeground="#a3a3a3")
        self.Button1_8.configure(foreground="#ffffff")
        self.Button1_8.configure(highlightbackground="#d9d9d9")
        self.Button1_8.configure(highlightcolor="black")
        self.Button1_8.configure(pady="0")
        self.Button1_8.configure(text='''1''')

        self.Button1_8 = tk.Button(top,command=button6)
        self.Button1_8.place(relx=0.742, rely=0.944, height=32, width=98)
        self.Button1_8.configure(activebackground="#39ede1")
        self.Button1_8.configure(activeforeground="#000000")
        self.Button1_8.configure(background="#092bd8")
        self.Button1_8.configure(disabledforeground="#a3a3a3")
        self.Button1_8.configure(foreground="#ffffff")
        self.Button1_8.configure(highlightbackground="#d9d9d9")
        self.Button1_8.configure(highlightcolor="black")
        self.Button1_8.configure(pady="0")
        self.Button1_8.configure(text='''6''')

        self.Button1_9 = tk.Button(top,command=webPage)
        self.Button1_9.place(relx=0.814, rely=0.014, height=32, width=98)
        self.Button1_9.configure(activebackground="#39ede1")
        self.Button1_9.configure(activeforeground="#000000")
        self.Button1_9.configure(background="#092bd8")
        self.Button1_9.configure(disabledforeground="#a3a3a3")
        self.Button1_9.configure(foreground="#ffffff")
        self.Button1_9.configure(highlightbackground="#d9d9d9")
        self.Button1_9.configure(highlightcolor="black")
        self.Button1_9.configure(pady="0")
        self.Button1_9.configure(text='''Info''')

        self.Button2_9 = tk.Button(top,command=youTube)
        self.Button2_9.place(relx=0.714, rely=0.014, height=32, width=98)
        self.Button2_9.configure(activebackground="#39ede1")
        self.Button2_9.configure(activeforeground="#000000")
        self.Button2_9.configure(background="#092bd8")
        self.Button2_9.configure(disabledforeground="#a3a3a3")
        self.Button2_9.configure(foreground="#ffffff")
        self.Button2_9.configure(highlightbackground="#d9d9d9")
        self.Button2_9.configure(highlightcolor="black")
        self.Button2_9.configure(pady="0")
        self.Button2_9.configure(text='''YouTube''')

        self.Button2_8 = tk.Button(top,command=howThisWorks)
        self.Button2_8.place(relx=0.714, rely=0.014, height=32, width=98)
        self.Button2_8.configure(activebackground="#39ede1")
        self.Button2_8.configure(activeforeground="#000000")
        self.Button2_8.configure(background="#092bd8")
        self.Button2_8.configure(disabledforeground="#a3a3a3")
        self.Button2_8.configure(foreground="#ffffff")
        self.Button2_8.configure(highlightbackground="#d9d9d9")
        self.Button2_8.configure(highlightcolor="black")
        self.Button2_8.configure(pady="0")
        self.Button2_8.configure(text='''How it works''')

        self.Label1_5 = tk.Label(top)
        self.Label1_5.place(relx=0.828, rely=0.667, height=31, width=199)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#000000")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(foreground="#ffffff")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''OPEN CIRCUIT CAN H''')
        self.Label1_5.configure(width=199)

        self.Label1_6 = tk.Label(top)
        self.Label1_6.place(relx=0.828, rely=0.722, height=31, width=199)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#000000")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(foreground="#ffffff")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''SHORT TO BATT +''')

        self.Label1_6 = tk.Label(top)
        self.Label1_6.place(relx=0.828, rely=0.778, height=31, width=199)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#000000")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(foreground="#ffffff")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''SHORT TO GND CAN LOW''')

        self.Label1_6 = tk.Label(top)
        self.Label1_6.place(relx=0.828, rely=0.833, height=31, width=199)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#000000")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(foreground="#ffffff")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''SHORT CAN HIGH TO LOW''')

        self.Label1_6 = tk.Label(top)
        self.Label1_6.place(relx=0.828, rely=0.889, height=31, width=199)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#000000")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(foreground="#ffffff")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''MISSING TERMINATED MODULE''')

        self.Label1_6 = tk.Label(top)
        self.Label1_6.place(relx=0.828, rely=0.944, height=31, width=199)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#000000")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(foreground="#ffffff")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''HIGH RESISTANCE CAN HIGH''')

        self.Button1_7 = tk.Button(top, command=root.destroy)
        self.Button1_7.place(relx=0.914, rely=0.014, height=32, width=98)
        self.Button1_7.configure(activebackground="#39ede1")
        self.Button1_7.configure(activeforeground="#000000")
        self.Button1_7.configure(background="#092bd8")
        self.Button1_7.configure(disabledforeground="#a3a3a3")
        self.Button1_7.configure(foreground="#ffffff")
        self.Button1_7.configure(highlightbackground="#79c8d8")
        self.Button1_7.configure(highlightcolor="black")
        self.Button1_7.configure(pady="0")
        self.Button1_7.configure(text='''EXIT''')

if __name__ == '__main__':

    vp_start_gui()





