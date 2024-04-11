from tkinter import *
root=Tk()
root.title("Calculator")
input=Entry(root,width=25,borderwidth=3,border=0,font=55)
input1=Entry(root,width=46,border=0)
input.grid(row=0,column=0,columnspan=4)
input1.grid(row=1,column=0,columnspan=4)

def onclick(num):
    cur=input.get()
    input.delete(0,END)
    input.insert(0,str(cur)+str(num)) 
    return
def add():
    global fnum
    global op
    op='add'
    fnum=input.get()
    input.delete(0,END)
    input1.insert(10,fnum+'+')
    return
def mul():
    global op
    global fnum
    op='mul'
    fnum=input.get()
    input.delete(0,END)
    input1.insert(0,fnum+'*')
    return
def div():
    global op
    global fnum
    op='div'
    fnum=input.get()
    input.delete(0,END)
    input1.insert(0,fnum+'/')
    return
def sub():
    global op
    global fnum
    op='sub'
    fnum=input.get()
    input.delete(0,END)
    input1.insert(0,fnum+'-')
    return
def clear():
    input.delete(0,END)
    input1.delete(0,END)
    return
def equal():
    global snum
    snum=input.get()
    input.delete(0,END)
    input1.delete(0,END)
    if op=='add':
        input.insert(0,int(fnum)+int(snum))
    elif op=='mul':
        input.insert(0,int(fnum)*int(snum))
    elif op=='sub':
        input.insert(0,int(fnum)-int(snum))
    elif op=='div':
        if (int(fnum)%int(snum))==0:
            input.insert(0,int(fnum)//int(snum))
        else:
            input.insert(0,int(fnum)/int(snum))
    return

b1=Button(root,text="1",padx=25,pady=20,command=lambda:onclick(1))
b2=Button(root,text="2",padx=25,pady=20,command=lambda:onclick(2))
b3=Button(root,text="3",padx=25,pady=20,command=lambda:onclick(3))
b4=Button(root,text="4",padx=25,pady=20,command=lambda:onclick(4))
b5=Button(root,text="5",padx=25,pady=20,command=lambda:onclick(5))
b6=Button(root,text="6",padx=25,pady=20,command=lambda:onclick(6))
b7=Button(root,text="7",padx=25,pady=20,command=lambda:onclick(7))
b8=Button(root,text="8",padx=25,pady=20,command=lambda:onclick(8))
b9=Button(root,text="9",padx=25,pady=20,command=lambda:onclick(9))
b0=Button(root,text="0",padx=25,pady=20,command=lambda:onclick(0))
b_add=Button(root,text="+",padx=24,pady=20,command=add)
b_mul=Button(root,text="*",padx=25,pady=20,command=mul)
b_div=Button(root,text="/",padx=25,pady=20,command=div)
b_sub=Button(root,text="-",padx=25,pady=20,command=sub)
b_equal=Button(root,text="=",padx=24,pady=20,command=equal)
b_clear=Button(root,text="AC",padx=20,pady=20,command=clear)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
b_div.grid(row=2,column=3)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b_mul.grid(row=3,column=3)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
b_div.grid(row=2,column=3)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b_mul.grid(row=3,column=3)

b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
b3.grid(row=4,column=2)
b_sub.grid(row=4,column=3)

b_clear.grid(row=5,column=0)
b0.grid(row=5,column=1)
b_equal.grid(row=5,column=2)
b_add.grid(row=5,column=3)

root.mainloop()