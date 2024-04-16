from tkinter import *
import math 
import numpy as np
import matplotlib.pyplot as plt
global D,t,graf
from cProfile import label
from msilib.schema import RadioButton
k=0
def vajuta():
    global k 
    k+=1 
    nupp.configure(text=k)
def vajuta_(event):
    global k
    k-=1
    nupp.configure(text=k)

def valik():
    arv=var.get()
    textbox.insert(END,arv) 


def otsus(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = round((-1*b+math.sqrt(D))/(2*a),2)
        x2 = round((-1*b+math.sqrt(D))/(2*a),2)
        t=f"X1={x1}, \nX2={x2}"
        graf=True
    elif D == 0:
        x1=round((-1*b)/(2*a),2)
        t=f"X1={x1}"
        graf=True
    else:
        t="Pole juuri!"
        graf=False
    return (t,graf)

def calculate(a,b,c):
    a=float(a) 
    b=float(b) 
    c=float(c)
    x0 = -b / (2*a)
    y0 = a*x0**2 + b*x0 + c
    x1 = np.arange(x0 - 10, x0 + 10, 0.5)
    y1 = a*x1**2 + b*x1 + c
    plt.plot(x1, y1, "m-s")
    plt.title("Ruudu võrrand")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show(x0,y0,x1,y1)

def graafik(graf:bool,D: float):
    if graf==True:
        a=float(a.get())
        b=float(b.get())
        c=float(c.get())
        x0=(-b)/(2*a)
        y0=a*x0**2+b*x0+c
        x1= np.arange(x0-10, x0+10, 0.5) #min max step [min,max]
        y1=a*x1**2+b*x1+c
        plt.plot(x1, y1,"m-s")
        plt.title("Ruudu võrrand")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.figure()
        plt.plot(x1, y1, label=f"D={D}\n{t}\n{text}")
        plt.grid(True)
        plt.show()
        text=f"Parabooli tüpp ({x0},{y0})"
    else:
        text=f"Graafik ei ole võimalik ehitada"

#def grafik():
#    try:
#        a, b, c = float(_a.get()), float(_b.get()), float(_c.get())
#        result_text, can_draw = otsus(a, b, c)
#        out.delete(1.0, END)
#        out.insert(END, result_text)
#        if can_draw:
#            calculate(a, b, c)
#    except ValueError:
#        out.delete(1.0, END)
#        out.insert(END, "Vigane sisend!")

aken=Tk()         #root
aken.geometry("800x600")   #razmek okna
aken.iconbitmap('shell.ico')
aken.title("Tkinteri kasutamine")
tekst="Pealkiri\n"

_a = Entry(aken, 
           width=5, 
           font=("Arial", 20), 
           justify="center", 
           bg="#cc3366")
_b = Entry(aken,
           width=5,
           font=("Arial", 20), 
           justify="center",
           bg="#db7093")
_c = Entry(aken, 
           width=5, 
           font=("Arial", 20), 
           justify="center", 
           bg="#ffb6c1")
pealkiri=Label(aken,
               text=tekst,
               bg="#b9f2ff",
               fg="#000000",
               font="Algerian 20",
               height=3,width=len(tekst),
               cursor="watch")
text1 = Label(aken, text="x^2 +", font=("Arial", 30))
text2 = Label(aken, text="x +", font=("Arial", 30)) 
text3 = Label(aken, text="= 0", font=("Arial", 30))
out = Text(aken, height=2, width=20, font=("Arial", 15))
arvutada_nupp = Button(aken, text="Calculate", font=("Arial", 15), command=calculate)
graafiku_nupp = Button(aken, text="Kuva graafik", font=("Arial", 15), command=graafik)
graafiku_nupp.grid(row=4, column=3, columnspan=2)

_a.grid(row=1, column=1)
text1.grid(row=1, column=2)
_b.grid(row=1, column=3)
text2.grid(row=1, column=4)
_c.grid(row=1, column=5)
text3.grid(row=1, column=6)
arvutada_nupp.grid(row=2, column=3, columnspan=2)
out.grid(row=3, column=2, columnspan=4) 

textbox=Entry(aken,
              bg="#e0ffff",
              fg="#000000",
              font="Algerian 20",
              width=20,
              justify=CENTER) #show="*"

nupp=Button(aken,
            text="Vajuta mind!",
            font="Arial 20",
            height=3,width=10,
            relief=RAISED, #SUNKEN, GROOVE
            bg="darkred",
            command=vajuta)  
f=Frame(aken)
var=IntVar()   #StringVar(), BoolVar()
e=Radiobutton(f,text="KALA",variable=var,value=1,font="Arial 20",command=valik)
t=Radiobutton(f,text="Teine",variable=var,value=2,font="Arial 20",command=valik)
ko=Radiobutton(f,text="Kolmas",variable=var,value=3,font="Arial 20",command=valik)
nupp.bind("<Button-3>",vajuta_)    #pkm
#textbox.bind("<Return>",tst_psse)  #enter

obj=[pealkiri,textbox,nupp,f] 
for i in obj:
    #i.pack() 
    obj2=[e,t,ko]
for i in range(len(obj2)):
    obj2[i].grid(row=0,column=i)




def kala_(event):
    kala_.post(event.x_root, event.y_root)

f.bind("<Button-3>", kala_)

f.grid(row=4, columnspan=3)
e.grid(row=0, column=0)
t.grid(row=0, column=1)
ko.grid(row=0, column=2)
 
def kala():
    x1 = np. arange(0, 9.5, 0.5)#min max step
    y1=(2/27)*x1*x1-3
    x2 = np. arange(-10, 0.5, 0.5)#min max step
    y2=0.04*x2*x2-3
    x3 = np. arange(-9, -2.5, 0.5)#min max step
    y3=(2/9)*(x3+6)**2+1
    x4 = np. arange(-3, 9.5, 0.5)#min max step
    y4=(-1/12)*(x4-3)**2+6
    x5 = np. arange(5, 9, 0.5)#min max step
    y5=(1/9)*(x5-5)**2+2
    x6 = np. arange(5, 8.5, 0.5)#min max step
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np. arange(-13, -8.5, 0.5)#min max step
    y7=(-0.75)*(x7+11)**2+6
    x8 = np. arange(-15, -12.5, 0.5)#min max step
    y8=(-0.5)*(x8+13)**2+3
    x9 = np. arange(-15, -10, 0.5)#min max step
    y9=[1]*len(x9)
    x10 = np. arange (3, 4, 0.5)#min max step
    y10=[3]*len(x10)
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,)



aken.mainloop()
