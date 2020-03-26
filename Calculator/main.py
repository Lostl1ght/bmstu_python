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
            if flag:
                c += '1'
                flag = True
            else:
                c += '0'
                flag = False

    return c, minus


operation = True
def choose(b: bool) -> None:
    global operation
    operation = b
    if b:
        fu_label['text'] = '+'
    else:
        fu_label['text'] = '-'


def check(a1: str, a2: str) -> bool:
    error = False
    if a_entry[0].get() == '' or a_entry[1].get() == '':
        error = True
    for i in a_entry[0].get():
        if i not in '01.':
            error = True
            break
    for i in a_entry[1].get():
        if i not in '01.':
            error = True
            break
    if a_entry[0].get().count('.') > 1:
        error = True
    if a_entry[1].get().count('.') > 1:
        error = True
    if error:
        mb.showerror('Ошибка ввода', 'Введите верные числа!')
        res_label['text'] = 'ОШИБКА'
        return True
    else:
        return False
    

def calculate(operation) -> None:
    if check(a_entry[0].get(), a_entry[1].get()):
        return
    b1, b2, length, dot_len = converter(a_entry[0].get(), a_entry[1].get())
    if operation:
        fu_label['text'] = '+'
        c, minus = adder(b1, b2, length)
    else:
        c, minus = subtractor(b1, b2, length)
        fu_label['text'] = '-'
    res = normalize(c, dot_len, minus)

    res_label['text'] = res


def delete_all() -> None:
    a_entry[0].delete(0, END)
    a_entry[1].delete(0, END)
    res_label.config(text = '')


def delete_one(opt: int) -> None:
    a_entry[opt].delete(0, END)
    res_label.config(text = '')


def showabout() -> None:
    win = Toplevel(window, width=410, height=150)
    win.title('Информация о программе и её владельце')
    lblwin = Label(win, text = 'Калькулятор, \nскладывающий или вычитающий числа \nв двоичной системе счисления' +
                                '\nбез перевода в десятичную. \n© Буланый Константин, ИУ7-26Б', font  = '8')
    lblwin.place(relx=0.5, rely=0.35, anchor='c')
    close_button = Button(win, text='Закрыть', command = lambda: win.destroy())
    close_button.place(relx = 0.45, rely = 0.7, width = 65, height = 35)

which = 0
def insert_digit(s: str) -> None:
    a_entry[which].insert(END, s)


def set_focus(i: int) -> None:
    global which
    a_entry[i].focus_set()
    a_entry[i].icursor(END)
    which = i


def callback1(event: 'tkinter.Event') -> None:
    global which
    which = 0


def callback2(event: 'tkinter.Event') -> None:
    global which
    which = 1


window = Tk()
window.title('Калькулятор')
window.geometry('280x345')
window.bind('<Return>', calculate)


a_entry = [Entry, Entry]
a_entry[0] = Entry(window, font = 20, width=28, justify=RIGHT)
a_entry[0].place(x=140, y=15, anchor='c')
a_entry[1] = Entry(window, font = 20, width=28, justify=RIGHT)
a_entry[1].place(x=140, y=77, anchor='c')
a_entry[0].bind('<Button-1>', callback1)
a_entry[1].bind('<Button-1>', callback2)
a_entry[0].focus_set()

fu_label = Label(window, text='+', font = 20)
fu_label.place(x=140, y=47, anchor='c')
eq_label = Label(window, text='=', font = 20)
eq_label.place(x=140, y=110, anchor='c')
res_label = Label(window, text='', font = 20, width=28, background='#ffffff')
res_label.place(x=140, y=140, anchor='c')

btn_0 = Button(window, text='0', font = 20, command=lambda: insert_digit('0'))
btn_0.place(x=40, y=170, width = 50, height = 50)
btn_1 = Button(window, text='1', font = 20, command=lambda: insert_digit('1'))
btn_1.place(x=90, y=170, width = 50, height = 50)
btn_dot = Button(window, text='.', font = 20, command=lambda: insert_digit('.'))
btn_dot.place(x=140, y=170, width = 50, height = 50)
btn_plus = Button(window, text='+', font = 20, command=lambda: choose(True))
btn_plus.place(x=190, y=170, width = 50, height = 50)

btn_up = Button(window, text='↑', font = 20, command=lambda: set_focus(0))
btn_up.place(x=40, y=220, width = 50, height = 50)
btn_down = Button(window, text='↓', font = 20, command=lambda: set_focus(1))
btn_down.place(x=90, y=220, width = 50, height = 50)
btn_del = Button(window, text='⇐', font = 20, background='#ebb95e', command=lambda: a_entry[which].delete(first = len(a_entry[which].get()) - 1, last = len(a_entry[which].get())))
btn_del.place(x=140, y=220, width = 50, height = 50)
btn_minus = Button(window, text='-', font = 20, command=lambda: choose(False))
btn_minus.place(x=190, y=220, width = 50, height = 50)

btn_eq = Button(window, text='=', font = 20, command=lambda: calculate(operation), background='#9ed65e')
btn_eq.place(x=40, y=270, width = 100, height = 50) 
btn_clear = Button(window, text='X', font = 20, command=delete_all, background='#eb6c52')
btn_clear.place(x=140, y=270, width = 50, height = 50)

main_menu = Menu()

del_menu = Menu()
del_menu.add_command(label='Очистить первое поле ввода', command=lambda: delete_one(0))
del_menu.add_command(label='Очистить второе поле ввода', command=lambda: delete_one(1))
del_menu.add_command(label='Очистить все поля', command=delete_all)

calc_menu = Menu()
calc_menu.add_command(label='Сложить числа', command=lambda: calculate(True))
calc_menu.add_command(label='Вычесть числа', command=lambda: calculate(False))

inf_menu = Menu()
inf_menu.add_command(label = 'Информация о программе и её владельце', command=showabout)

main_menu.add_cascade(label='Очистка', menu=del_menu)
main_menu.add_cascade(label='Операции', menu=calc_menu)
main_menu.add_cascade(label='Справка', menu=inf_menu)

window.config(menu=main_menu)

window.mainloop()