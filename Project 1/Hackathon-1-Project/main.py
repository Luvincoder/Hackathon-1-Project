from tkinter import*
from tkinter import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab
main = Tk()
main.state("zoomed")
main.title("Kids paint")

#variable
erase_color = "white"
pen_color = "black"
#Canvas

canvas = Canvas(main,bg="white",bd=5,relief=GROOVE,height=750,width=1250)
canvas.place(x=250,y=10)

#funtion

def canvas_color():
    global erase_color
    color = colorchooser.askcolor()
    canvas.configure(bg=color[1])
    erase_color=color[1]


def save():
    file_name = filedialog.asksaveasfilename(defaultextension=".jpg")
    x = main.winfo_rootx() + Canvas.winfo_x()
    y = main.winfo_rooty() + canvas.winfo_y()

    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(file_name)
    messagebox.showinfo("Paint Notification","Image is Saved as" + str(file_name))

def erase():
    global pen_color
    pen_color = erase_color

def clear():
    canvas.delete("all")

def paint(event):
    x1,y1 = (event.x-2),(event.y-2)
    x2,y2 = (event.x+2),(event.y+2)
    canvas.create_oval(x1,y1,x2,y2,fill=pen_color,outline=pen_color,width=pen_size.get())

canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>" , paint)

def select_color(col):
    global pen_color
    pen_color = col


#frame
color_frame = LabelFrame(main,text="Color" ,relief=RIDGE,bg="white" ,width=500)
color_frame.place(x=10,y=10,width=215,height=55)

Tools_frame = LabelFrame(main,text="Tools" ,relief=RIDGE,bg="white" ,width=500)
Tools_frame.place(x=10,y=65,width=215,height=55)

pen_size = LabelFrame(main,text="Size" ,relief=RIDGE,bg="white" ,width=500)
pen_size.place(x=10,y=122,width=215,height=67)

#Color
color = ["red" , "Blue" , "yellow" , "Green" , "Black" , "White"]

#button
i=j=0
for color in color:
    Button(color_frame,bd=3, bg=color,relief=RIDGE,width=3,command=lambda col=color:select_color(col)).grid(row=j,column=i,padx=1)
    i=i+1

# Tool_Button

canvas_color_b1 = Button(Tools_frame, text="Canvas", bd=4,bg="white",command=canvas_color,relief=RIDGE)
canvas_color_b1.grid(row=0,column=0)

save_b2 = Button(Tools_frame, text="Save", bd=4,bg="white",command=save,relief=RIDGE)
save_b2.grid(row=0,column=1)

eraser_b3 = Button(Tools_frame, text="Eraser", bd=4,bg="white",command=erase,relief=RIDGE)
eraser_b3.grid(row=0,column=2)

clear_b4 = Button(Tools_frame, text="Clear", bd=4,bg="white",command=clear,relief=RIDGE)
clear_b4.grid(row=0,column=3)

#size for brush

pen_size = Scale(pen_size,orient=HORIZONTAL,from_=0,to=50,length=170)
pen_size.set(1)
pen_size.grid(row=0,column=0)



main.mainloop()