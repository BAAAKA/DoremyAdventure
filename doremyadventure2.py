from tkinter import *
from BigStuff.DoremyAdventure.myconfig import *


#Global Variable of pic
isinworld=1
doremyposX=500
doremyposY=100
remiliaposX=1600
remiliaposY=100
yuyukoposX=300
yuyukoposY=500
teleportposX=900
teleportposY=900
global wpresseddown
wpresseddown=False

doremymoveRange=100

mainStage = Tk()
mainStage.title(title1)

global frame
frame = Canvas(mainStage, width=1900, height=1000)
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
    print("Left CLick")

def rightClick(event):
    global doremyposX
    print("right CLick")

def middleClick(event):
    print("middle CLick")


def keyp(event):
    global doremymoveRange

    if event.keysym == 'w':
        moveXY(0, -doremymoveRange)
    elif event.keysym == 'a':
        moveXY(-doremymoveRange, 0)
    elif event.keysym == 's':
        moveXY(0, doremymoveRange)
    elif event.keysym == 'd':
        moveXY(doremymoveRange, 0)
    elif event.keysym == 'e':
        playerPosSpecial()
    if event.keysym == 'W':
        print("CAPS!!!!!")


def moveXY(x, y):
    fx=frame.winfo_width()
    fy=frame.winfo_height()
    global doremyposX
    global doremyposY
    global doremyimgpath
    global doremyimg
    if(doremyposX+x<fx-77 and doremyposX+x>77 and doremyposY+y>0 and doremyposY+y<fy-77): #-77 because of image size / 2
        doremyposX=doremyposX+x
        doremyposY=doremyposY+y
        frame.move(doremyimg, x, y)
        print("doremyX: ", doremyposX)
        print("doremyY: ", doremyposY)
        playerPosSpecial()
    else:
        print("not allowed, outside map")
def playerPosSpecial():
    global doremyposX
    global doremyposY
    global remiliaposX
    global remiliaposY
    global frame
    if(isinworld==1):
        if(doremyposX==remiliaposX and doremyposY==remiliaposY):
            chatwithremilia()  # create the chat window
        elif(doremyposX==teleportposX and doremyposY==teleportposY):
            frame.delete("all")
            doremyposX=200
            doremyposY=900
            loadworld2()
        elif(doremyposX==yuyukoposX and doremyposY==yuyukoposY):
            chatwithyuyuko()


    elif(isinworld==2):
        if(doremyposX==1500 and doremyposY==100):
            doremyposX=200
            doremyposY=900
            loadworld1()


def createDoremy(doremyposX, doremyposY):
    global doremyimgpath
    global doremyimg
    doremyimg = frame.create_image(doremyposX, doremyposY, image=doremyimgpath)


def chatwithremilia(): #chatwindow with remilia
    global chat
    global chatfield
    chat = Toplevel(mainStage, width=10, height=4)
    # T = Text(chat, height=6, width=10) #Texfield

    chatfield=Label(chat)
    chatfield.config(font=("Courier", 34))
    chatfield.grid(row=0, columnspan=3)

    frame1 = Frame(chat, bg="orange")
    frame2 = Frame(chat, bg="blue")
    frame3 = Frame(chat, bg="green")

    frame1.grid(row=1, column=1)
    frame2.grid(row=1, column=2)
    frame3.grid(row=1, column=3)

    button1 = Button(frame1, text="Good", width = 30, command=Remilianicedef)
    button2 = Button(frame2, text="Bad", width = 30, command=Remiliasaddef)
    button3 = Button(frame3, text="Sawwy, Im in a hurry", width = 30, command=Remiliabyedef)
    button1.grid()
    button2.grid()
    button3.grid()

    chat.title("Chat")
    chat.attributes("-topmost", True)
    setchatfieldtext(chatfield, RemiliaHello)
    chat.mainloop()


def chatwithyuyuko():
    global chatfield
    global chat
    chat = Toplevel(mainStage)
    # T = Text(chat, height=6, width=10) #Texfield
    chatfield=Label(chat, text="Hello, I Sell Stuff :3")
    chatfield.config(font=("Courier", 34))
    chatfield.pack(side=TOP)
    button3 = Button(chat, text="Ok, I will remember that :3", command=Remiliabyedef)
    button3.pack(side=BOTTOM)


def Remilianicedef():
    global chatfield
    setchatfieldtext(chatfield, Remilianice)
def Remiliasaddef():
    global chatfield
    setchatfieldtext(chatfield, Remiliasad)
def Remiliabyedef():
    global chatfield
    setchatfieldtext(chatfield, Remiliabye)
    chat.destroy()



def setchatfieldtext(chatfield, text):
    print("ay")
    chatfield.config(text=text)

def loadworld1():
    global isinworld
    isinworld = 1
    frame.create_image(960, 540, image=backgroundImage1)
    remiliaimg = frame.create_image(remiliaposX, remiliaposY, image=Remiliaimgpath)
    yuyukoimg = frame.create_image(yuyukoposX, yuyukoposY, image=yuyukoimgpath)
    createDoremy(doremyposX, doremyposY)

def loadworld2():
    global isinworld
    isinworld = 2
    frame.create_image(960, 540, image=backgroundImage2)
    createDoremy(doremyposX, doremyposY)

frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", rightClick)
frame.bind("<Button-2>", middleClick)
mainStage.bind_all('<KeyPress>', keyp)

frame.pack()

yuyukoimgpath = PhotoImage(file="yuyuko.png")
doremyimgpath = PhotoImage(file="doremy.png")
backgroundImage1 = PhotoImage(file="backgorundImg1.png")
backgroundImage2 = PhotoImage(file="backgorundImg2.png")
Remiliaimgpath = PhotoImage(file="remilia.png")


loadworld1()



# doremyimgpath = doremyimgpath.zoom(2)  #resizing image
# doremyimgpath = doremyimgpath.subsample(3)




mainStage.mainloop()