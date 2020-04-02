# Сортировка с бинарным поиском.

from tkinter import Frame, Tk, Label, Entry, Button, Toplevel, HORIZONTAL, CENTER
from tkinter.ttk import Treeview, Style, Progressbar

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from random import randint


# Сортировка с бинарным поиском.
def insertion_bin(array: list) -> None:
    def binsearch(array: list, value: int, start: int, end: int) -> int:
        if start >= end:
            if array[start] > value:
                return start
            else:
                return start + 1

        mid = (start + end) // 2

        if array[mid] > value:
            return binsearch(array, value, start, mid - 1)
        elif array[mid] < value:
            return binsearch(array, value, mid + 1, end)
        else:
            return mid

    for i in range(1, len(array)):
        pos = binsearch(array, array[i], 0, i - 1)
        for j in range(i, pos, -1):
            array[j], array[j - 1] = array[j - 1], array[j]


# Заполнение таблицы.
def create_table(tree: 'Treeview', rand: list, up: list, down: list) -> None:
    tree.delete(*tree.get_children())

    text = ['Ascending array', 'Random array', 'Descending array']

    tree.heading('n1', text=n1_entry.get(), anchor=CENTER)
    tree.heading('n2', text=n2_entry.get(), anchor=CENTER)
    tree.heading('n3', text=n3_entry.get(), anchor=CENTER)

    tree.insert('', 0, values=(text[0], str(
        up[0]) + ' ms', str(up[1]) + ' ms', str(up[2]) + ' ms'))
    tree.insert('', 1, values=(text[1], str(
        rand[0]) + ' ms', str(rand[1]) + ' ms', str(rand[2]) + ' ms'))
    tree.insert('', 2, values=(text[2], str(
        down[0]) + ' ms', str(down[1]) + ' ms', str(down[2]) + ' ms'))

    tree.pack()


# Создание пустых графика и таблицы.
def create_blank() -> 'Treeview':
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot()
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    Style().configure('Treeview', rowheight=60)

    tree = Treeview(table_frame, columns=('names', 'n1', 'n2', 'n3'), height=3)

    tree.column('#0', width=0, minwidth=0)
    tree.column('names', width=150, minwidth=150, anchor=CENTER)
    tree.column('n1', width=150, minwidth=150, anchor=CENTER)
    tree.column('n2', width=150, minwidth=150, anchor=CENTER)
    tree.column('n3', width=150, minwidth=150, anchor=CENTER)

    tree.heading('names', text='', anchor=CENTER)
    tree.heading('n1', text='N1', anchor=CENTER)
    tree.heading('n2', text='N2', anchor=CENTER)
    tree.heading('n3', text='N3', anchor=CENTER)

    text = ['Ascending array', 'Random array', 'Descending array']

    tree.insert('', 0, values=(text[0], '', '', ''))
    tree.insert('', 1, values=(text[1], '', '', ''))
    tree.insert('', 2, values=(text[2], '', '', ''))

    tree.pack()

    return tree


# Рисование графика.
def create_graph(graph_frame: 'Frame') -> None:
    try:
        gerr_label['text'] = ''
        graph_frame.pack_forget()
        graph_frame = Frame(window)
        graph_frame.grid(row=2, column=1)

        x = []
        n = int(n_entry.get())
        step = int(step_entry.get())
        status = 0
        for i in range(10):
            x.append(n)
            graph_progress['value'] = status
            window.update()
            status += 1
            n += step

        status = 10
        y = []
        for i in x:
            y.append(count_random(2, i))
            graph_progress['value'] = status
            window.update()
            status += 9

        fig = plt.Figure(figsize=(6, 4), dpi=100)

        ax = fig.add_subplot(111)

        ax.plot(x, y)
        ax.set_yticks(y)
        ax.set_xticks(x)

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        graph_progress['value'] = 100
        window.update()
    except:
        gerr_label['text'] = 'ERROR'


# Сортировка маленького массива.
def sort_small() -> None:
    try:
        if array_entry.get() == '':
            n_array_label['text'] = 'ERROR'
            return
        n_array = list(int(i) for i in array_entry.get().split())
        ns_array = ', '.join(str(s) for s in n_array)
        n_array_label['text'] = ns_array
        insertion_bin(n_array)
        s_array = ', '.join(str(s) for s in n_array)
        s_array_label['text'] = s_array
    except:
        n_array_label['text'] = 'ERROR'


# Засечение времени.
def gettimeofday() -> int:
    return round(time.time() * 1000)


# Вычисление времени для случайного массива.
def count_random(n: int, leng: int) -> int:
    a = []
    for i in range(leng):
        a.append(randint(-1000, 1000))

    summ = 0
    for i in range(n):
        start = gettimeofday()
        insertion_bin(a[:])
        end = gettimeofday()
        summ += end - start
    return summ // n


# Вычисление времени для ворзрастающего массива.
def count_up(n: int, leng: int) -> int:
    a = []
    for i in range(leng):
        a.append(i + 1)

    summ = 0
    for i in range(n):
        start = gettimeofday()
        insertion_bin(a[:])
        end = gettimeofday()
        summ += end - start
    return summ // n


# Вычисление времени для убывющего массива.
def count_down(n: int, leng: int) -> int:
    a = []
    for i in range(leng, 0, -1):
        a.append(i + 1)

    summ = 0
    for i in range(n):
        start = gettimeofday()
        insertion_bin(a[:])
        end = gettimeofday()
        summ += end - start
    return summ // n


# Вычисление времени и заполнение таблицы.
def calculate_for_table(meas: int, n: list) -> None:
    try:
        n = [int(i) for i in n]
        terr_label['text'] = ''
        table_progress['value'] = 5
        window.update()
        status = 0

        up = []
        for i in range(3):
            status += 10
            table_progress['value'] = status
            window.update()
            up.append(count_up(meas, n[i]))

        rand = []
        for i in range(3):
            status += 10
            table_progress['value'] = status
            window.update()
            rand.append(count_random(meas, n[i]))

        down = []
        for i in range(3):
            status += 10
            table_progress['value'] = status
            window.update()
            down.append(count_down(meas, n[i]))

        create_table(tree, rand, up, down)
        table_progress['value'] = 100
        window.update()
    except:
        terr_label['text'] = 'ERROR'


window = Tk()
window.title('Sorting methods research')
window.resizable(0, 0)

array_frame = Frame(window)
array_frame.grid(row=0, columnspan=2)
table_input_frame = Frame(window)
table_input_frame.grid(row=1, column=0)
table_frame = Frame(window)
table_frame.grid(row=1, column=1)
graph_input_frame = Frame(window)
graph_input_frame.grid(row=2, column=0)
graph_frame = Frame(window)
graph_frame.grid(row=2, column=1)

tree = create_blank()

array_label = Label(array_frame, text='Array', width=30)
array_label.grid(row=0, column=0)
array_entry = Entry(array_frame, width=36)
array_entry.grid(row=1, column=0)
array_btn = Button(array_frame, text='Input', width=15, command=sort_small)
array_btn.grid(row=1, column=1, rowspan=3)
n_array_label = Label(array_frame, text='', width=30, background='#ffffff')
n_array_label.grid(row=2, column=0)
s_array_label = Label(array_frame, text='', width=30, background='#ffffff')
s_array_label.grid(row=3, column=0)
blank = Label(array_frame, text='', width=30)
blank.grid(row=4, column=0)

# tit_label = Label(table_input_frame, text='Num of measurements', width=18)
# tit_label.grid(row=0)
# tit_entry = Entry(table_input_frame, width=20)
# tit_entry.grid(row=1)
terr_label = Label(table_input_frame, text='', width=18)
terr_label.grid(row=0)
n1_label = Label(table_input_frame, text='N1', width=15)
n1_label.grid(row=2)
n1_entry = Entry(table_input_frame, width=20)
n1_entry.grid(row=3)
n2_label = Label(table_input_frame, text='N2', width=15)
n2_label.grid(row=4)
n2_entry = Entry(table_input_frame, width=20)
n2_entry.grid(row=5)
n3_label = Label(table_input_frame, text='N3', width=15)
n3_label.grid(row=6)
n3_entry = Entry(table_input_frame, width=20)
n3_entry.grid(row=7)
table_btn = Button(table_input_frame, text='Input', width=15, command=lambda: calculate_for_table(
    2, [n1_entry.get(), n2_entry.get(), n3_entry.get()]))
table_btn.grid(row=8)
table_progress = Progressbar(table_input_frame, orient=HORIZONTAL,
                             length=100, mode='determinate')
table_progress.grid(row=9)

# git_label = Label(graph_input_frame, text='Num of measurements', width=18)
# git_label.grid(row=0)
# git_entry = Entry(graph_input_frame, width=20)
# git_entry.grid(row=1)
gerr_label = Label(graph_input_frame, text='', width=18)
gerr_label.grid(row=0)
n_label = Label(graph_input_frame, text='N', width=15)
n_label.grid(row=2)
n_entry = Entry(graph_input_frame, width=20)
n_entry.grid(row=3)
step_label = Label(graph_input_frame, text='Step', width=15)
step_label.grid(row=4)
step_entry = Entry(graph_input_frame, width=20)
step_entry.grid(row=5)
graph_btn = Button(graph_input_frame, text='Input', width=15,
                   command=lambda: create_graph(graph_frame))
graph_btn.grid(row=6)
graph_progress = Progressbar(graph_input_frame, orient=HORIZONTAL,
                             length=100, mode='determinate')
graph_progress.grid(row=7)

window.mainloop()
