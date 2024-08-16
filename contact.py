from tkinter import *

m =Tk()
m.geometry('400x600')
m.config(bg='SlateGray3')
m.title("Contact Book")
m.resizable(0,0)

data=[
    ['Arjun Kumar','9876203046'],
    ['Bhavana','7634901278'],
    ['Divya','8690227651'],
    ['Hansu','6723803843'],
    ['Jenny','7645821904'],
    ['Jack','9367823409'],
    ['Moni','7080174301'],
    ['nivish','9450732164'],
    ['Ram','8302839821'],
    ['Yash','2638394721'],
    ['Suriya','8029463983'],
    ['Shankar','8563472863'],
    ['Sam','9567953750']
]

name=StringVar()
phone=StringVar()

f=Frame(m)
f.pack(side=RIGHT)

sb=Scrollbar(f, orient=VERTICAL)
lbNames = Listbox(f,yscrollcommand= sb.set,height=12)
sb.config(command=lbNames.yview)
sb.pack(side=RIGHT,fill=Y)
lbNames.pack(side=LEFT,fill=BOTH,expand=5)

def selected():
    return int(lbNames.curselection()[0])

def add_contact():
    data.append([name.get(),phone.get()])
    select_set()

def edit():
    data[selected()]=[name.get(),phone.get()]
    select_set()

def delete():
    del data[selected()]
    select_set()

def view():
    NAME,PHONE=data[selected()]
    name.set(name)
    phone.set(phone)

def exit():
    m.destroy()
    
def clear():
    name.set('')
    phone.set('')

def select_set():
    data.sort()
    lbNames.delete(0,END)
    for name,phone in data:
        lbNames.insert(END,name)
select_set()

Label(m,text='NAME',font='arial 12 bold',bg='black',fg='white').place(x=30,y=30)
Entry(m,textvariable=name,font='arial 12 bold').place(x=30,y=60)
Label(m,text='PHONE NO',font='arial 12 bold',bg='black',fg='white').place(x=30,y=90)
Entry(m,textvariable=phone,font='arial 12 bold').place(x=30,y=120)
Button(m,text='ADD',font='arial 12 bold',bg='black',fg='white',command=add_contact).place(x=50,y=170,width=100)
Button(m,text='EDIT',font='arial 12 bold',bg='black',fg='white',command=edit).place(x=50,y=220,width=100)
Button(m,text='DELETE',font='arial 12 bold',bg='black',fg='white',command=delete).place(x=50,y=270,width=100)
Button(m,text='EXIT',font='arial 12 bold',bg='black',fg='white',command=exit).place(x=50,y=320,width=100)
Button(m,text='RESET',font='arial 12 bold',bg='black',fg='white',command=clear).place(x=50,y=370,width=100)

m.mainloop()