# Разработать калькулятор.
# Ввод должен осуществляться как с клавиатуры, так и с интерфейса.
# Должно быть меню:
#     1) Очистка полей
#     2) Информация о программе и об авторе
#     3) Сложение, вычитание двоичных чисел без операции перевода.
# Цисла знаковые вещественные.

from tkinter import END, Toplevel, Label, Button, Tk, Entry, CENTER, Menu


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
        c1 = c1[1:]
    len_c2 = len(c2)
    if '-' in c2:
        len_c2 -= 1
        c2 = c2[1:]

    while length < max(len_c1, len_c2):
        length += 1

    bb1 = c1[::-1] + '0' * (length - len_c1)

    bb2 = c2[::-1] + '0' * (length - len_c2)

    return bb1, bb2, length, dot_len


def normalizer(c: str, dot_len: int, minus_after_operation: bool, minus_because_signs: bool) -> str:
    k = 0
    if dot_len > 0:
        c = c[:dot_len] + '.' + c[dot_len:]
        while c[k] == '0':
            k += 1
    c = c[::-1]
    i = 0
    if '1' not in c:
        return '0'
    while c[i] == '0':
        i += 1

    if c[i] == '.':
        i -= 1
    if c[len(c) - k - 1] == '.':
        k += 1
    if minus_after_operation == minus_because_signs:
        return c[i:len(c) - k]
    return '-' + c[i:len(c) - k]


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

    return c, True


def subtractor(b1: str, b2: str, length: int) -> (str, bool):
    minus = True
    if b1[::-1] < b2[::-1]:
        b1, b2 = b2, b1
        minus = False
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
    if a1 == '' or a2 == '':
        error = True
    for i in a1:
        if i not in '01.-':
            error = True
            break
    for i in a2:
        if i not in '01.-':
            error = True
            break
    if a1.count('.') > 1:
        error = True
    if a2.count('.') > 1:
        error = True
    if a1.count('-') > 1:
        error = True
    if a2.count('-') > 1:
        error = True
    if '-' in a1 and a1.index('-') != 0 or '-' in a2 and a2.index('-') != 0:
        error = True

    if error:
        res_label['text'] = 'ОШИБКА'
        return True
    else:
        return False


def signum(a1: str, a2: str) -> (bool, bool):
    sign_a1 = True
    sign_a2 = True
    if a1[0] == '-':
        sign_a1 = False

    if a2[0] == '-':
        sign_a2 = False

    return sign_a1, sign_a2


def calculate(operation: bool) -> None:
    if check(a_entry[0].get(), a_entry[1].get()):
        return
    sign_a1, sign_a2 = signum(a_entry[0].get(), a_entry[1].get())
    b1, b2, length, dot_len = converter(a_entry[0].get(), a_entry[1].get())
    if operation:
        if sign_a1 is True and sign_a2 is True:
            c, minus_after_operation = adder(b1, b2, length)
            minus_because_signs = True
        if sign_a1 is False and sign_a2 is False:
            c, minus_after_operation = adder(b1, b2, length)
            minus_because_signs = False
        if sign_a1 is True and sign_a2 is False:
            c, minus_after_operation = subtractor(b1, b2, length)
            if b1[::-1] >= b2[::-1]:
                minus_because_signs = True
            else:
                minus_because_signs = False
        if sign_a1 is False and sign_a2 is True:
            c, minus_after_operation = subtractor(b1, b2, length)
            if b1[::-1] >= b2[::-1]:
                minus_because_signs = False
            else:
                minus_because_signs = True
    else:
        if sign_a1 is True and sign_a2 is True:
            c, minus_after_operation = subtractor(b1, b2, length)
            minus_because_signs = True
        if sign_a1 is False and sign_a2 is True:
            c, minus_after_operation = adder(b1, b2, length)
            minus_because_signs = False
        if sign_a1 is False and sign_a2 is False:
            c, minus_after_operation = adder(b1, b2, length)
            if b1[::-1] >= b2[::-1]:
                minus_because_signs = False
            else:
                minus_because_signs = True
        if sign_a1 is True and sign_a2 is False:
            c, minus_after_operation = adder(b1, b2, length)
            minus_because_signs = True
    result = normalizer(c, dot_len, minus_after_operation, minus_because_signs)

    res_label['text'] = result


def delete_all() -> None:
    a_entry[0].delete(0, END)
    a_entry[1].delete(0, END)
    res_label.config(text='')


def delete_one(opt: int) -> None:
    a_entry[opt].delete(0, END)
    res_label.config(text='')


def show_about() -> None:
    win = Toplevel(window, width=410, height=200)
    win.title('Информация о программе и её владельце')
    lblwin = Label(win, text='Калькулятор, \nскладывающий или вычитающий числа \nв двоичной системе счисления' +
                   '\nбез перевода в десятичную. \n© Буланый Константин, ИУ7-26Б', font='1')
    lblwin.place(relx=0.5, rely=0.35, anchor='c')
    close_button = Button(win, text='Закрыть', command=lambda: win.destroy())
    close_button.place(relx=0.45, rely=0.7, width=65, height=35)


which = 0


def insert_digit(s: str) -> None:
    a_entry[which].insert(END, s)


def set_focus(i: int) -> None:
    global which
    a_entry[i].focus_set()
    a_entry[i].icursor(END)
    which = i


def focus1(event: 'tkinter.Event') -> None:
    global which
    which = 0


def focus2(event: 'tkinter.Event') -> None:
    global which
    which = 1


def invert(opt: int) -> None:
    num = a_entry[opt].get()
    if num == '':
        return
    if num[0] == '-':
        num = num[1:]
    else:
        num = '-' + num
    a_entry[opt].delete(0, END)
    a_entry[opt].insert(END, num)
    res_label.config(text='')


window = Tk()
window.title('Калькулятор')
window.geometry('280x345')
window.resizable(0, 0)
window.bind('<Return>', calculate)


a_entry = [Entry, Entry]
a_entry[0] = Entry(window, font=20, width=28, justify=CENTER)
a_entry[0].place(x=140, y=15, anchor='c')
a_entry[1] = Entry(window, font=20, width=28, justify=CENTER)
a_entry[1].place(x=140, y=77, anchor='c')
a_entry[0].bind('<Button-1>', focus1)
a_entry[1].bind('<Button-1>', focus2)
a_entry[0].focus_set()

fu_label = Label(window, text='+', font=20)
fu_label.place(x=140, y=47, anchor='c')
eq_label = Label(window, text='=', font=20)
eq_label.place(x=140, y=110, anchor='c')
res_label = Label(window, text='', font=20, width=28, background='#ffffff')
res_label.place(x=140, y=140, anchor='c')

btn_0 = Button(window, text='0', font=20, command=lambda: insert_digit('0'))
btn_0.place(x=40, y=170, width=50, height=50)
btn_1 = Button(window, text='1', font=20, command=lambda: insert_digit('1'))
btn_1.place(x=90, y=170, width=50, height=50)
btn_dot = Button(window, text='.', font=20, command=lambda: insert_digit('.'))
btn_dot.place(x=140, y=170, width=50, height=50)
btn_inv = Button(window, text='INV', command=lambda: invert(which))
btn_inv.place(x=190, y=170, width=50, height=50)

btn_up = Button(window, text='↑', font=20, command=lambda: set_focus(0))
btn_up.place(x=40, y=220, width=50, height=50)
btn_plus = Button(window, text='+', font=20, command=lambda: choose(True))
btn_plus.place(x=90, y=220, width=50, height=50)
btn_minus = Button(window, text='-', font=20, command=lambda: choose(False))
btn_minus.place(x=140, y=220, width=50, height=50)
btn_del = Button(window, text='⇐', font=20, background='#ebb95e', command=lambda: a_entry[which].delete(
    first=len(a_entry[which].get()) - 1, last=len(a_entry[which].get())))
btn_del.place(x=190, y=220, width=50, height=50)

btn_down = Button(window, text='↓', font=20, command=lambda: set_focus(1))
btn_down.place(x=40, y=270, width=50, height=50)
btn_eq = Button(window, text='=', font=20, command=lambda: calculate(
    operation), background='#9ed65e')
btn_eq.place(x=90, y=270, width=100, height=50)
btn_clear = Button(window, text='X', font=20,
                   command=delete_all, background='#eb6c52')
btn_clear.place(x=190, y=270, width=50, height=50)

main_menu = Menu()

del_menu = Menu()
del_menu.add_command(label='Очистить первое поле ввода     ',
                     command=lambda: delete_one(0))
del_menu.add_command(label='Очистить второе поле ввода     ',
                     command=lambda: delete_one(1))
del_menu.add_command(label='Очистить все поля     ', command=delete_all)

calc_menu = Menu()
calc_menu.add_command(label='Сложить числа     ',
                      command=lambda: calculate(True))
calc_menu.add_command(label='Вычесть числа     ',
                      command=lambda: calculate(False))
calc_menu.add_command(
    label='Изменить знак первого числа     ', command=lambda: invert(0))
calc_menu.add_command(
    label='Изменить знак второго числа     ', command=lambda: invert(1))

inf_menu = Menu()
inf_menu.add_command(
    label='Информация о программе и её владельце     ', command=show_about)

main_menu.add_cascade(label='Очистка', menu=del_menu)
main_menu.add_cascade(label='Операции', menu=calc_menu)
main_menu.add_cascade(label='Справка', menu=inf_menu)

window.config(menu=main_menu)

window.mainloop()
