from tkinter import *
from tkinter import colorchooser
root = Tk()
root.title("Drawing App")
root.geometry("1100x600")

stroke_size = IntVar()
stroke_size.set(1)
stroke_color = StringVar()
stroke_color.set("black")


# frame 1 for tools

frame_1 = Frame(root , height=100 , width=1100)
frame_1.grid(row=0, column=0, sticky=NW)

#tools frame

tool_frame = Frame(frame_1 , height=100 , width=100)
tool_frame.grid(row=0 , column=0)

def use_pencil():
    stroke_color.set("black")
    canvas["cursor"] = "arrow"

def use_erase():
    stroke_color.set("white")
    canvas["cursor"] = DOTBOX


Pencil = Button(tool_frame , text="Pencil" , width=10 , command=use_pencil)
Pencil.grid(row=0 , column=0)

Erase = Button(tool_frame , text="Erase" , width=10 , command=use_erase)
Erase.grid(row=1 , column=0)

Tools = Label(tool_frame , text="Tools" , width=10)
Tools.grid(row=3 , column=0)

# size frame


size_frame = Frame(frame_1 , height=100 , width=100)
size_frame.grid(row=0 , column=1)

#de

bottom_2 = Button(size_frame, text="Defaulf" , width=10 , command=use_pencil)
bottom_2.grid(row=1 , column=0)
options = [1,2,3,4,5,10]
size_list = OptionMenu(size_frame , stroke_size , *options)
size_list.grid(row=3 , column=0)


Tools = Label(size_frame , text="Size" , width=10)
Tools.grid(row=2 , column=0)


#frame 2 for canvas

frame_2 = Frame(root , height=500 , width=1100 , bg="yellow")
frame_2.grid(row=1, column=0)

canvas = Canvas(frame_2 , height=500 , width=1100 , bg="white")
canvas.grid(row=0 , column=0)

#colorframe

def select_color():
    select_color = colorchooser.askcolor("blue" , title="Select color")
    stroke_color.set(select_color[1])

color_frame = Frame(frame_1 , height=100 , width=100)
color_frame.grid(row=0 , column=2)
color_botton = Button(color_frame , text="Select Color" , width=10 , command=select_color)
color_botton.grid(row=0 , column=0)

#save image frame



saveimage_frame = Frame(frame_1 , height=100 , width=100)
saveimage_frame.grid(row=0 , column=4)
save_button = Button(saveimage_frame , text="Save" , width=10 , command=lambda: stroke_color.set("red"))
save_button.grid(row=0 , column=0)


# variables for pencil

prev_point = [0, 0]
current_point = [0,0]

def paint(event):
    global prev_point
    global current_point
    x = event.x
    y = event.y
    current_point = [x,y]
    # canvas.create_oval(x , y , x + 5 , y + 5 , fill="black")

    if prev_point != [0,0] :
        canvas.create_line(prev_point[0] , prev_point [1] , current_point[0] , current_point[1], fill=stroke_color.get() , width=stroke_size.get())
    
    prev_point = current_point


    if event.type == "5" :
        prev_point = [0,0]


canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>" , paint)

root.resizable(False, False)
root.mainloop()