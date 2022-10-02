
from tkinter import*
from tkinter.simpledialog import *
root=Tk()
root.title("IKpixels Calculator")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 310
height = 450
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
root.config(background="pink")
fa1=Frame(root,bg="lightblue",height=60,width=400)
fa1.place(x=0,y=0)
la1= Label(root,text="IK CALCULATOR",fg="blue",font=('times',25,'bold'),bg="lightblue")
la1.place(x=10,y=5)

text_Input = StringVar()
operator = ""


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btndsply():
    global operator
    operator = ""
    text_Input.set(operator)

def btnequal():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

timed=Entry(root,insertwidth=30, bd=30,width=40,textvariable=text_Input)
timed.place(x=4,y=70)

btn9=Button(root,text='9',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(9))
btn9.place(x=19,y=150)
btn8=Button(root,text='8',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(8))
btn8.place(x=84,y=150)
btn7=Button(root,text='7',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(7))
btn7.place(x=149,y=150)
btnplus=Button(root,text='+',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick("+"))
btnplus.place(x=214,y=150)
btn6=Button(root,text='6',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(6))
btn6.place(x=19,y=210)
btn5=Button(root,text='5',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(5))
btn5.place(x=84,y=210)
btn4=Button(root,text='4',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(4))
btn4.place(x=149,y=210)
btnm=Button(root,text='-',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick("-"))
btnm.place(x=214,y=210)
btn3=Button(root,text='3',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(3))
btn3.place(x=19,y=270)
btn2=Button(root,text='2',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(2))
btn2.place(x=84,y=270)
btn1=Button(root,text='1',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(1))
btn1.place(x=149,y=270)
btnx=Button(root,text='x',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick("*"))
btnx.place(x=214,y=270)
btn0=Button(root,text='0',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick(0))
btn0.place(x=19,y=330)
btnC=Button(root,text='C',bd=5,width="7",height='3',bg='red',font= ('times',0,'bold'),command=btndsply)
btnC.place(x=84,y=330)
btnE=Button(root,text='=',bd=5,width="7",height='3',font= ('times',0,'bold'),command=btnequal)
btnE.place(x=149,y=330)
btnD=Button(root,text='/',bd=5,width="7",height='3',font= ('times',0,'bold'),command=lambda: btnclick("/"))
btnD.place(x=214,y=330)
def closs_root():
    messagebox.showinfo("IK TECH"," NDAKUNYANDIRANI!!!\n    click OK to EXIT.")
    root.destroy()
    exit()
btn00=Button(root,text="EXIT",width="25",bg="white",bd="5",fg="red",font= ('arial',0,'bold'),command=closs_root)
btn00.place(x=23,y=410)

root.mainloop()
