from tkinter import *
import math 
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox as mb 
global D,t
from cProfile import label
from msilib.schema import RadioButton



aken=Tk()      
aken.geometry("900x700")  
aken.iconbitmap('shell.ico')
aken.title("Tkinteri kasutamine")
tekst="Tkinteri kasutamine\n"



pealkiri=Label(aken,
               text=tekst,
               fg="#000000",
               font=("Broadway", 30),
               height=2,width=len(tekst),
               cursor="watch")



def otsus():
    try:
        a=float(_a.get()) 
        b=float(_b.get()) 
        c=float(_c.get())
    except:
        mb.showwarning("Lahenduseks tuleb sisestada numbrid!")
        return
    D = b**2 - 4*a*c
    if D > 0:
        x1 = round((-1*b+math.sqrt(D))/(2*a),2)
        x2 = round((-1*b+math.sqrt(D))/(2*a),2)
        t = f'D = {D}\nx1 = {x1}\nx2 = {x2}'
        graf=True
    elif D == 0:
        x=round((-1*b)/(2*a),2)
        t=f"X={x}"
        graf=True
    else:
        t="Pole juuri!"
        graf=False
    vastus.delete(1.0, END)
    vastus.insert(END, t, "center")



def graafik():
    a=float(_a.get()) 
    b=float(_b.get()) 
    c=float(_c.get())
    D=b**2 - 4*a*c
    if D<0 or D==0 :
        mb.showwarning("Graafiku lahendamiseks tuleb sisestada numbrid!")
        return
    x0=(-b)/(2*a)
    y0=a*x0**2+b*x0+c
    x1= np.arange(x0-10, x0+10, 0.5)
    y1=a*x1**2+b*x1+c
    plt.figure()
    plt.plot(x1, y1,"m-s")
    plt.title("Graafik")
    plt.ylabel("y")
    plt.xlabel("x")
    text=f"Parabooli tüpp ({x0},{y0})"
    plt.grid(True)
    plt.show()

        

_a = Entry(aken, 
           width=5, 
           font=("Cascadia Code", 20), 
           justify="center", 
           bg="#cc3366")
_b = Entry(aken,
           width=5,
           font=("Cascadia Code", 20), 
           justify="center",
           bg="#db7093")
_c = Entry(aken, 
           width=5, 
           font=("Cascadia Code", 20), 
           justify="center", 
           bg="#ffb6c1")

text1 = Label(aken, text="x^2 +", font=("Arial", 30))
text2 = Label(aken, text="x +", font=("Arial", 30)) 
text3 = Label(aken, text="= 0", font=("Arial", 30))

vastus = Text(aken, height=3, width=20, font=("Arial Narrow", 15))
vastus.grid(row=4, column=3, columnspan=4) 

arvutada_nupp = Button(aken, text="Lahendamine", font=("Impact", 20), command=otsus)
arvutada_nupp.grid(row=3, column=3, columnspan=4)

graafiku_nupp = Button(aken, text="Kuva graafik", font=("Impact", 20), command=graafik)
graafiku_nupp.grid(row=6, column=3, columnspan=4)

pealkiri.grid(row=1, column=3, columnspan=4)

_a.grid(row=2, column=2)
text1.grid(row=2, column=3)

_b.grid(row=2, column=4)
text2.grid(row=2, column=5)

_c.grid(row=2, column=6)
text3.grid(row=2, column=7)



def keith():
    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)                                  #c , m , y , r , g , b, w, k
    plt.figure()
    plt.plot(x1,y1,'c-',x2,y2,'m-',x3,y3,'y-',x4,y4,'r-',x5,y5,'g-',x6,y6,'b-',x7,y7,'g-',x8,y8, 'c-',x9,y9, 'm-', x10,y10,'k-')
    plt.title("Keith")
    plt.xlabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
    


def konnakull():
    x1=np.arange(-7,7.5,0.5)
    y1=-(3/49)*x1*x1+8
    x2=np.arange(-7,7.5,0.5)
    y2=(4/49)*x2*x2+1
    x3=np.arange(-6.8,-2.5,0.5)
    y3=-(0.75)*(x3+4)**2+9
    x4=np.arange(2,6.5,0.5)
    y4=-(0.75)*(x4-4)**2+9
    x5=np.arange(-5.8,-2.5,0.5)
    y5=-(x5+4)**2+9
    x6=np.arange(2.8,5.5,0.5)
    y6=-(x6-4)**2+9
    x7=np.arange(-4,4.5,0.5)
    y7=(4/9)*x7*x7-5
    x8=np.arange(-5.2,5.5,0.5)
    y8=(4/9)*x8*x8-9
    x9=np.arange(-7,-2.5,0.5)
    y9=-(1/16)*(x9+3)**2-6
    x10=np.arange(2,7.5,0.5)
    y10=-(1/16)*(x10-3)**2-6
    x11=np.arange(-7,0.5,0.5)
    y11=(1/9)*(x11+4)**2-11
    x12=np.arange(0,7.5,0.5)
    y12=(1/9)*(x12-4)**2-11
    x13=np.arange(-7,-4.5,0.5)
    y13=-(x13+5)**2
    x14=np.arange(4,7.5,0.5)
    y14=-(x14-5)**2
    x15=np.arange(-3,3.5,0.5)
    y15=(2/9)*x15*x15+2
    plt.figure()
    plt.plot(x1,y1,'c-',x2,y2,'m-',x3,y3,'y-',x4,y4,'r-',x5,y5,'g-',x6,y6,'b-',x7,y7,'g-',x8,y8, 'c-',x9,y9, 'm-', x10,y10,'k-',x11,y11, 'm-',x12,y12, 'm-',x13,y13, 'm-',x14,y14, 'm-',x15,y15, 'm-')
    plt.title("Konnakull")
    plt.xlabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()



def vihmavari():
    x1=np.arange(-12,12.5,0.5)
    y1=-(1/18)*x1*x1+12 
    x2=np.arange(-4,4.5,0.5)
    y2=-(1/8)*x2*x2+6 
    x3=np.arange(-12,-4.5,0.5)
    y3=-(1/8)*(x3+8)**2+6
    x4=np.arange(4,12.5,0.5)
    y4=-(1/8)*(x4-8)**2+6
    x5=np.arange(-4,0.5,0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,0.5,0.5)
    y6=1.5*(x6+3)**2-10
    plt.figure()
    plt.plot(x1,y1,'c-',x2,y2,'m-',x3,y3,'y-',x4,y4,'r-',x5,y5,'g-',x6,y6,'b-')
    plt.title("Vihmavari")
    plt.xlabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
    


f=Frame(aken)
var=IntVar()   
keith_=Radiobutton(f,text="KEITH",variable=var,value=1,font="Complex",command=keith)
konnakull_=Radiobutton(f,text="KONNAKULL",variable=var,value=2,font="Complex",command=konnakull)
vihmavari_=Radiobutton(f,text="VIHMAVARI",variable=var,value=3,font="Complex",command=vihmavari)


obj=[pealkiri,f] 
for i in obj:
    obj2=[keith_,konnakull_,vihmavari_] #,t,ko
for i in range(len(obj2)):
    obj2[i].grid(row=0,column=i)



f.bind("<Button-3>",keith)
f.bind("<Button-3>",konnakull)
f.bind("<Button-3>",vihmavari)

f.grid(row=4, columnspan=3)
keith_.grid(row=0, column=0)
konnakull_.grid(row=2, column=0)
vihmavari_.grid(row=4, column=0)
 


aken.mainloop()
