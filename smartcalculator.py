from tkinter import*
from math import sqrt,ceil,floor
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualsInput():
    global  operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

def binary():
    global operator
    kavya=text_input.get()
    bina=bin(int(kavya)).replace("0b","")
    text_input.set(bina)
def binarytonumber():
    global opertor
    reddy=text_input.get()
    ans=0
    for i in range(len(reddy)):
        if int(reddy[i])%2!=0:
            ans+=(1<<(len(reddy)-i-1))
    text_input.set(str(ans))
def addtwobinary():
    global operator
    kavya=text_input.get()
    kk=kavya.split('+')
    ans1=0
    for i in range(len(kk[0])):
        if int(kk[0][i])%2!=0:
            ans1+=(1<<(len(kk[0])-i-1))
    ans2 = 0
    for i in range(len(kk[1])):
        if int(kk[1][i]) % 2 != 0:
            ans2 += (1 << (len(kk[1]) - i - 1))
    ans=ans1+ans2
    text_input.set(str(ans))
def wisheshaha():
    global operator
    text_input.set("WELCOME KAVYA")
def power():
    global operator
    ka=text_input.get()
    ans=eval(ka)
    text_input.set(str(ans))
cal=Tk()
cal.title("KAVYA REDDY CALCULATOR")
operator=""
text_input=StringVar()

txtDisplay=Entry(cal,font=('arial',50,'bold'),textvariable=text_input,bd=20,insertwidth=4,bg="powder blue",justify='right').grid(columnspan=6)

btn7=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",command=lambda : btnClick(7)).grid(row=1,column=0)
btn8=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",command=lambda : btnClick(8)).grid(row=1,column=1)
btn9=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",command=lambda : btnClick(9)).grid(row=1,column=2)
Addition=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",command=lambda : btnClick('+')).grid(row=1,column=3)
btn4=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",command=lambda : btnClick(4)).grid(row=2,column=0)
btn5=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",command=lambda : btnClick(5)).grid(row=2,column=1)
btn6=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="6",bg="powder blue",command=lambda : btnClick(6)).grid(row=2,column=2)
Subtraction=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",command=lambda : btnClick('-')).grid(row=2,column=3)
btn1=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",command=lambda : btnClick(1)).grid(row=3,column=0)
btn2=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",command=lambda : btnClick(2)).grid(row=3,column=1)
btn3=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="3",bg="powder blue",command=lambda : btnClick(3)).grid(row=3,column=2)
Multiplication=Button (cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="*",bg="powder blue",command=lambda : btnClick('*')).grid(row=3,column=3)
btn0=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",command=lambda : btnClick(0)).grid(row=4,column=0)
btnclear=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",bg="powder blue",command=lambda : btnClearDisplay()).grid(row=4,column=1)
btnequals=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text="=",bg="powder blue",command=lambda : btnEqualsInput()).grid(row=4,column=2)
Division=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",command=lambda : btnClick('/')).grid(row=4,column=3)
binari=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="to_bin",bg="powder blue",command=lambda : binary()).grid(row=4,column=4)
bynari=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="tonum",bg="powder blue",command=lambda : binarytonumber()).grid(row=3,column=4)
addbinary=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="(+)_bin",bg="powder blue",command=lambda : addtwobinary()).grid(row=2,column=4)
happy=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="jst_fun",bg="powder blue",command=lambda : wisheshaha()).grid(row=1,column=4)
evaluate=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="evaluate",bg="powder blue",command=lambda : power()).grid(row=4,column=5)
modulus=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="%(mod)",bg="powder blue",command=lambda : btnClick('%')).grid(row=3,column=5)
point=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text=".(point)",bg="powder blue",command=lambda : btnClick('.')).grid(row=2,column=5)
comma=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text=",(com)",bg="powder blue",command=lambda : btnClick(',')).grid(row=1,column=5)


cal.mainloop()
