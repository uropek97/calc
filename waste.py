# from tkinter import *
# from decimal import *
# import operations as op

# mylist = []

# def op_click(button_text, number):
#     result = Decimal(number)
#     mylist.append(result)
#     mylist.append(button_text)
#     if len(mylist)==4:
#         result = op.opChoice(button_text, mylist[0], result)
#         mylist.clear()
#         mylist.append(result)
#         mylist.append(button_text)

#     return result


# def op_equal(secondnumbStr):
#     if len(mylist)==2:
#         secondnumb = Decimal(secondnumbStr)
#         result = op.opChoice(mylist[1], mylist[0], secondnumb)
#         mylist.clear()
#         mylist.append(result)
#         return result
        

# def numb_click(button_text):
#     a = inputField.get()

#     inputField.insert(len(a), button_text)

# def op_click1(button_text):
#     number = inputField.get()
#     if number != '':
#         result = commands.op_click(button_text, number)
#         label['text'] = result  
#         inputField.delete(first=0, last=len(inputField.get()))        
#     else:
#         messagebox.showinfo('Ошибка', 'Введите число')

# def op_equal1():
#     secondnumbStr = inputField.get()
#     if secondnumbStr == '':
#         messagebox.showinfo('Ошибка', 'Введите число')
#     result = commands.op_equal(secondnumbStr)
#     if(type(result)==Decimal):
#         label['text'] = result
#     else:
#         messagebox.showinfo('Ошибка', 'Введите число')
#     inputField.delete(first=0, last=len(inputField.get()))


    # button_complex_plus = Button(calcwindow, text = '+imag',command=lambda: add_imag())
    # button_complex_min = Button(calcwindow, text = '-imag', command=lambda: add_imag())

    # if mode.get():
    #     button_complex_plus.place_forget()
    #     button_complex_min.place_forget()
    #     messagebox.showinfo(mode.get())
    #     op_CE()
    # else:
    #     button_complex_plus.place(relx=0.9, rely=0.7)
    #     button_complex_min.place(relx=0.9, rely=0.85)
    #     messagebox.showinfo(mode.get())
    #     op_CE()


    # def op_sqrt():
    # numbStr = inputField.get()
    # if numbStr != '':
    #     if mode:
    #         numb = complex(numbStr)
    #         if len(mylist)==0:            
    #             mylist.append(result)
    #             result = cmath.sqrt(numb)
    #             label_before['text'] = f'√{numb}'
    #             label['text'] = result
    #             op_C()
    #     else:
    #         numb = Decimal(numbStr)
    #         if len(mylist)==0: 
    #             result = math.sqrt(numb)           
    #             mylist.append(result)
    #             label_before['text'] = f'√{numb}'
    #             label['text'] = result
    #             op_C()