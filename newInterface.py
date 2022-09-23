import cmath
import math
from tkinter import *
from decimal import *
import tkinter
import operations as op

mylist = []


def op_click(button_text):
    numbStr = inputField.get()
    if numbStr != '':
        if mode.get():
            numb = complex(numbStr)
        else:
            numb = Decimal(numbStr)
        if len(mylist)==0:
            mylist.append(numb)
                       
        elif len(mylist)==2:
            result = op.opChoice(mylist[1], mylist[0], numb)
            mylist.clear()
            mylist.append(result)

        mylist.append(button_text)  
        
    else:
        if len(mylist)==1:
            mylist.append(button_text)
            label['text'] = ''
        elif len(mylist)==2:
            mylist[1]=button_text
       
    label_before['text'] = f'{mylist[0]} {mylist[1]}'
    op_C()
        
def op_sqrt():
    numbStr = inputField.get()
    if mode.get():
        sqrt_op = cmath.sqrt
    else:
        sqrt_op = math.sqrt
    if numbStr != '':
        if mode.get():
            numb = complex(numbStr)
        else:
            numb = Decimal(numbStr)
        if len(mylist)==0:
            result = sqrt_op(numb)
            mylist.append(result)
            label_before['text'] = f'√{numb}'
            label['text'] = result
            op_C()
        elif len(mylist)>0:
            number = op.opChoice(mylist[1], mylist[0], numb)
            result = sqrt_op(number)
            label_before['text'] = f'√{number}'
            label['text'] = result
            mylist.clear()
            mylist.append(result)
            op_C()
    else:
        if len(mylist)==1:
            result = sqrt_op(mylist[1])
            label['text'] = result
            mylist.clear()
            mylist.append(result)
            op_C()


def op_equal():
    numbStr = inputField.get()
    if numbStr != '':
        if len(mylist)==2:
            if mode.get():
                numb = complex(numbStr)
            else:
                numb = Decimal(numbStr)
            result = op.opChoice(mylist[1], mylist[0], numb)
            label['text'] = result
            label_before['text'] = ''
            op_C()
            mylist.clear()
            mylist.append(result)

    else:
        label['text'] = 'Введите число'
        if len(mylist)>0:
                label['text'] = 'Введите второе число'


def numb_click(button_text):
    numb = inputField.get()
    if len(mylist)==1:
        op_CE()
    if numb!='' and numb[len(numb)-1]=='j':
        return

    inputField.insert(len(numb), button_text)

def point_click(buttom_text):
    text = inputField.get()
    if text == '':
        text = f'0{buttom_text}'
        inputField.insert(0, text)
    elif 'j' in text or '.' in text:
        return
    else:
        text+=buttom_text
        inputField.insert(len(text), buttom_text)

def op_C():
    inputField.delete(first=0, last=len(inputField.get()))

def op_CE():
    op_C()
    mylist.clear()
    label['text'] = ''
    label_before['text'] = ''

def op_backspace():
    numb = inputField.get()
    if numb != '':
        inputField.delete(first= len(numb)-1)

def add_imag(button_text):
    numb = inputField.get()
    if numb == '':
        numb = f'0{button_text}'
    else:
        numb += button_text
    op_C()
    inputField.insert(0, numb)


def change_mode(mode):
    button_complex_plus = Button()
    button_complex_min = Button()
    button_j = Button()
    if not mode.get():
        button_complex_plus.place_forget()
        button_complex_min.place_forget()
        button_j.place_forget()
        op_CE()
    else:
        button_complex_plus = Button(calcwindow, text = '+imag', command=lambda: add_imag('+'))
        button_complex_min = Button(calcwindow, text = '-imag', command=lambda: add_imag('-'))
        button_j = Button(calcwindow, text='j', command=lambda: numb_click('j'))
        button_complex_plus.place(relx=0.9, rely=0.7)
        button_complex_min.place(relx=0.9, rely=0.85)
        button_j.place(relx = 0.3, rely = 0.25)
        op_CE()
    

def print_Int():
    global calcwindow
    calcwindow = Tk()    
    calcwindow.geometry('500x500')
    
    global inputField
    inputField = Entry(calcwindow, width=20, bd=3)

    global label
    label = Label()
    global label_before
    label_before = Label()

    global mode
    mode = tkinter.IntVar()
    flag_label = Label(calcwindow, text='Работа с комплексными числами')
    flag = Checkbutton(calcwindow ,variable=mode, command=lambda: change_mode(mode))

    button_plus = Button(calcwindow, text='+', command=lambda: op_click('+'))
    button_minus = Button(calcwindow, text='-', command=lambda: op_click('-'))
    button_mult = Button(calcwindow, text='*', command=lambda: op_click('*'))
    button_divid = Button(calcwindow, text='/', command=lambda: op_click('/'))
    button_degree = Button(calcwindow, text='^', command=lambda: op_click('^'))

    button_sqrt = Button(calcwindow, text = '√', command=lambda: op_sqrt())

    button_equal = Button(calcwindow, text='=', command=lambda: op_equal())

    button_1 = Button(calcwindow, text='1', command=lambda: numb_click('1'))
    button_2 = Button(calcwindow, text='2', command=lambda: numb_click('2'))
    button_3 = Button(calcwindow, text='3', command=lambda: numb_click('3'))
    button_4 = Button(calcwindow, text='4', command=lambda: numb_click('4'))
    button_5 = Button(calcwindow, text='5', command=lambda: numb_click('5'))
    button_6 = Button(calcwindow, text='6', command=lambda: numb_click('6'))
    button_7 = Button(calcwindow, text='7', command=lambda: numb_click('7'))
    button_8 = Button(calcwindow, text='8', command=lambda: numb_click('8'))
    button_9 = Button(calcwindow, text='9', command=lambda: numb_click('9'))
    button_0 = Button(calcwindow, text='0', command=lambda: numb_click('0'))


    button_point = Button(calcwindow, text='.', command=lambda: point_click('.'))

    button_C = Button(calcwindow, text = 'C', command=lambda: op_C())
    button_CE = Button(calcwindow, text = 'CE', command=lambda: op_CE())
    button_backspace = Button(calcwindow, text = '<=', command=lambda: op_backspace())

    inputField.place(relx=0.2, rely=0.125)

    label.place(relx = 0.2, rely=0.2)
    label_before.place(relx = 0.2, rely=0.075)
    flag_label.place(relx = 0.01, rely=0.025)
    flag.place(relx = 0.6, rely = 0.025)

    button_plus.place(relx = 0.7, rely = 0.4)
    button_minus.place(relx = 0.7, rely = 0.55)
    button_mult.place(relx=0.7, rely = 0.7)
    button_divid.place(relx = 0.7, rely=0.85)
    button_degree.place(relx = 0.9, rely= 0.4)
    button_sqrt.place(relx = 0.9, rely = 0.55)

    button_equal.place(relx=0.5, rely= 0.85)

    button_1.place(relx = 0.1, rely = 0.4)
    button_2.place(relx = 0.3, rely = 0.4)
    button_3.place(relx = 0.5, rely = 0.4)
    button_4.place(relx = 0.1, rely = 0.55)
    button_5.place(relx = 0.3, rely = 0.55)
    button_6.place(relx = 0.5, rely = 0.55)
    button_7.place(relx = 0.1, rely = 0.7)
    button_8.place(relx = 0.3, rely = 0.7)
    button_9.place(relx = 0.5, rely = 0.7)
    button_0.place(relx = 0.1, rely = 0.85)

    button_point.place(relx = 0.3, rely = 0.85)

    button_backspace.place(relx=0.5, rely=0.25)
    button_C.place(relx=0.7, rely = 0.25)
    button_CE.place(relx=0.9, rely = 0.25)

    calcwindow.mainloop()
