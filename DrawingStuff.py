from tkinter import *

#Global Variable of pic
global doremyposX
global doremyposY
doremyposX=500
doremyposY=100

global wpresseddown
wpresseddown=False

root = Tk()
root.title("doremys sweety dreemy adventure")
frame = Canvas(root, width=1000, height=500)
frame.pack()


#copy from timon dadduru
# def redraw():
#     global doremyposX
#     global doremyposY
#     print("redrawing... X:{0} and Y:{1}".format(doremyposX, doremyposY))
#     frame.after(10, redraw)
#     frame.update()



def leftClick(event):
    global doremyposX
    print("Left CLick conmfirmed")
    frame.move(doremyimg, -100, 0)

def rightClick(event):
    global doremyposX
    print("right CLick conmfirmed")
    frame.move(doremyimg, 100, 0)

def middleClick(event):
    print("middle CLick conmfirmed")




def wClick(event):
    print("w conmfirmed")
    global wpresseddown
    wpresseddown=True
    frame.move(doremyimg, 0, -100)

def aClick(event):
    print("a conmfirmed")
    frame.move(doremyimg, -100, 0)

def sClick(event):
    print("s conmfirmed")
    frame.move(doremyimg, 0, 100)

def dClick(event):
    print("d conmfirmed")
    frame.move(doremyimg, 100, 0)


frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", rightClick)
frame.bind("<Button-2>", middleClick)

root.bind("<w>", wClick)
root.bind("<a>", aClick)
root.bind("<s>", sClick)
root.bind("<d>", dClick)

frame.pack()

doremyimgpath = PhotoImage(file="doremy.png")
doremyimg = frame.create_image(doremyposX, doremyposY, image=doremyimgpath)



root.mainloop()