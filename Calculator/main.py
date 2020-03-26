from tkinter import *
from tkinter import messagebox as mb


def converter(a1: str, a2: str) -> (str, str, int, int):
    c1 = ''
    for i in a1:
        if i == '.':
            continue
        c1 += i
    c2 = ''
    for i in a2:
        if i == '.':
            continue
        c2 += i

    dot_len_a1 = 0
    if '.' in a1:
        dot_len_a1 = len(a1[a1.index('.'):]) - 1
    dot_len_a2 = 0
    if '.' in a2:
        dot_len_a2 = len(a2[a2.index('.'):]) - 1

    if dot_len_a1 > dot_len_a2:
        c2 += '0' * (dot_len_a1 - dot_len_a2)
        dot_len = dot_len_a1
    elif dot_len_a1 < dot_len_a2:
        c1 += '0' * (dot_len_a2 - dot_len_a1)
        dot_len = dot_len_a2
    else:
        dot_len = dot_len_a2

    length = 0
    len_c1 = len(c1)
    if '-' in c1:
        len_c1 -= 1
    len_c2 = len(c2)
    if '-' in c2:
        len_c2 -= 1

    while length < max(len_c1, len_c2):
        length += 1

    bb1 = c1[::-1] + '0' * (length - len_c1)

    bb2 = c2[::-1] + '0' * (length - len_c2)

    return bb1, bb2, length, dot_len


def normalize(c: str, dot_len: int, minus: bool) -> str:
    k = 0
    if dot_len > 0:
        c = c[:dot_len] + '.' + c[dot_len:]
        while c[k] == '0':
            k += 1
    c = c[::-1]
    i = 0
    while c[i] == '0':
        i += 1
    if minus:
        return '-' + c[i:len(c) - k]
    
    return c[i:len(c) - k]


def adder(b1: str, b2: str, length: int) -> (str, bool):
    c = ''
    flag = False
    for i in range(length):
        if b1[i] == '0' and b2[i] == '0':
            if flag:
                c += '1'
            else:
                c += '0'
            flag = False

        if b1[i] == '1' and b2[i] == '0' or b1[i] == '0' and b2[i] == '1':
            if flag:
                c += '0'
                flag = True
            else:
                c += '1'
                flag = False
        if b1[i] == '1' and b2[i] == '1':
            if flag:
                c += '1'
            else:
                c += '0'
            flag = True
    if flag:
        c += '1'

    return c, False


def subtractor(b1: str, b2: str, length: int) -> (str, bool):
    minus = False
    if b1[::-1] < b2[::-1]:
        b1, b2 = b2, b1
        minus = True
    c = ''
    flag = False
    for i in range(length):        
        if b1[i] == '0' and b2[i] == '0':            
            if flag:
                c += '1'
                flag = True
            else:
                c += '0'
                flag = False

        if b1[i] == '1' and b2[i] == '0':
            if flag:
                c += '0'
                
            else:
                c += '1'
            flag = False

        if b1[i] == '0' and b2[i] == '1':
            if flag:
                c += '0'
            else:
                c += '1'
            flag = True
        
        if b1[i] == '1' and b2[i] == '1':
            c += '0'

    return c, minus


operation = True
def choose(b: bool) -> None:
    global operation
    operation = b
    if b:
        fu_label['text'] = '+'
    else:
        fu_label['text'] = '-'


def calculate(operation) -> None:
    b1, b2, length, dot_len = converter(a_entry1.get(), a_entry2.get())
    if operation:
        c, minus = adder(b1, b2, length)
    else:
        c, minus = subtractor(b1, b2, length)
    res = normalize(c, dot_len, minus)

    res_label['text'] = res

window = Tk()
window.title("Калькулятор")
window.geometry('280x345')


a_entry1 = Entry(window, font = 20)
a_entry1.place(x=145, y=15, anchor='c')
a_entry2 = Entry(window, font = 20)
a_entry2.place(x=145, y=77, anchor='c')

fu_label = Label(window, text='+', font = 20)
fu_label.place(x=145, y=47, anchor='c')
eq_label = Label(window, text='=', font = 20)
eq_label.place(x=145, y=110, anchor='c')
res_label = Label(window, text='asd', font = 20)
res_label.place(x=145, y=140, anchor='c')

btn_0 = Button(window, text='0', font = 20)
btn_0.place(x=40, y=170, width = 50, height = 50)
btn_1 = Button(window, text='1', font = 20)
btn_1.place(x=90, y=170, width = 50, height = 50)
btn_dot = Button(window, text='.', font = 20)
btn_dot.place(x=140, y=170, width = 50, height = 50)
btn_plus = Button(window, text='+', font = 20, command=lambda: choose(True))
btn_plus.place(x=190, y=170, width = 50, height = 50)

btn_up = Button(window, text='↑', font = 20)
btn_up.place(x=40, y=220, width = 50, height = 50)
btn_down = Button(window, text='↓', font = 20)
btn_down.place(x=90, y=220, width = 50, height = 50)
btn_del = Button(window, text='⇐', font = 20)
btn_del.place(x=140, y=220, width = 50, height = 50)
btn_minus = Button(window, text='-', font = 20, command=lambda: choose(False))
btn_minus.place(x=190, y=220, width = 50, height = 50)

btn_eq = Button(window, text='=', font = 20, command=lambda: calculate(operation))
btn_eq.place(x=40, y=270, width = 100, height = 50) 
btn_clear = Button(window, text='X', font = 20)
btn_clear.place(x=140, y=270, width = 50, height = 50)

window.mainloop()