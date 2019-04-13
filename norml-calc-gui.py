from tkinter import *
import tkinter.messagebox
import math as m
root=Tk()
root.title('Calculator')
w = Canvas(root, width=180, height=340) 
w.pack()
def index1():
    a=e1.get()
    l=len(a)
    return l
def in1():
    e1.insert(index1(),'1')
def in2():
    e1.insert(index1(),'2')
def in3():
    e1.insert(index1(),'3')
def in4():
    e1.insert(index1(),'4')
def in5():
    e1.insert(index1(),'5')
def in6():
    e1.insert(index1(),'6')
def in7():
    e1.insert(index1(),'7')
def in8():
    e1.insert(index1(),'8')
def in9():
    e1.insert(index1(),'9')
def indot():
    e1.insert(index1(),'.')
def in0():
    e1.insert(index1(),'0')
def clr():
    e1.delete(0,END)
def plus():
    e1.insert(index1(),'+')
def mul():
    e1.insert(index1(),'*')
def minus():
    e1.insert(index1(),'-')
def div():
    e1.insert(index1(),'/')
def bsin():
    e1.insert(index1(),'sin')
def result():
    b=e1.get()
    for x in b:
        if(x=='+' or x=='-' or x=='*' or x=='/'):
            ans=eval(b)
            e1.delete(0,END)
            e1.insert(0,ans)
b1=Button(root,text=1,width=4,height=3,command=in1).place(x=5,y=47)
b2=Button(root,text=2,width=4,height=3,command=in2).place(x=49,y=47)
b3=Button(root,text=3,width=4,height=3,command=in3).place(x=93,y=47)
b4=Button(root,text=4,width=4,height=3,command=in4).place(x=5,y=110)
b5=Button(root,text=5,width=4,height=3,command=in5).place(x=49,y=110)
b6=Button(root,text=6,width=4,height=3,command=in6).place(x=93,y=110)
b7=Button(root,text=7,width=4,height=3,command=in7).place(x=5,y=173)
b8=Button(root,text=8,width=4,height=3,command=in8).place(x=49,y=173)
b9=Button(root,text=9,width=4,height=3,command=in9).place(x=93,y=173)
b0=Button(root,text=0,width=10,height=3,command=in0).place(x=49,y=236)
bdot=Button(root,text='.',width=4,height=3,command=indot).place(x=5,y=236)
b10=Button(root,text='+',width=4,height=3,command=plus).place(x=137,y=236)
b11=Button(root,text='-',width=4,height=3,command=minus).place(x=137,y=173)
b12=Button(root,text='*',width=4,height=3,command=mul).place(x=137,y=110)
b13=Button(root,text='/',width=4,height=3,command=div).place(x=137,y=47)
b14=Button(root,text='=',width=10,height=2,command=result).place(x=5,y=299)
b15=Button(root,text='Clear',width=10,height=2,command=clr).place(x=93,y=299)
e1=Entry(root)
e1.place(x=30,y=20)
root.mainloop()
