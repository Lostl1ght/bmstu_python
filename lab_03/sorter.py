from tkinter import W, Frame, Tk, Label, Entry, Button
from tkinter.ttk import Treeview, Style

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from random import randint


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


def create_table(tree: 'Treeview', rand: list, up: list, down: list) -> None:
    tree.delete(*tree.get_children())

    text = ['Упорядоченный\nмассив\n', 'Случайный\nмассив\n',
            'Упорядоченный в\nобратном порядке\nмассив\n']

    tree.heading('n1', text='2000', anchor=W)
    tree.heading('n2', text='2500', anchor=W)
    tree.heading('n3', text='3000', anchor=W)

    tree.insert('', 0, values=(text[0], up[0], up[1], up[2]))
    tree.insert('', 1, values=(text[1], rand[0], rand[1], rand[2]))
    tree.insert('', 2, values=(text[2], down[0], down[1], down[2]))

    tree.pack()


def create_blank() -> 'Treeview':
    fig = plt.Figure(figsize=(6, 3), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot()
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    Style().configure('Treeview', rowheight=60)

    tree = Treeview(table_frame, columns=('names', 'n1', 'n2', 'n3'), height=3)

    tree.column('#0', width=0, minwidth=0)
    tree.column('names', width=150, minwidth=150, anchor=W)
    tree.column('n1', width=150, minwidth=150, anchor=W)
    tree.column('n2', width=150, minwidth=150, anchor=W)
    tree.column('n3', width=150, minwidth=150, anchor=W)

    tree.heading('names', text='', anchor=W)
    tree.heading('n1', text='N1', anchor=W)
    tree.heading('n2', text='N2', anchor=W)
    tree.heading('n3', text='N3', anchor=W)

    tree.insert('', 0, values=('Упорядоченный\nмассив\n', '', '', ''))
    tree.insert('', 1, values=('Случайный\nмассив\n', '', '', ''))
    tree.insert('', 2, values=(
        'Упорядоченный в\nобратном порядке\n', '', '', ''))

    tree.pack()

    return tree


def create_graph(graph_frame: 'Frame') -> None:
    graph_frame.pack_forget()
    graph_frame = Frame(window)
    graph_frame.grid(row=2, column=1)

    x = [2000, 2500, 3000]
    y = [1, 10, 3]

    fig = plt.Figure(figsize=(6, 3), dpi=100)

    ax = fig.add_subplot(111)

    ax.plot(x, y)
    ax.set_yticks(y)
    ax.set_xticks(x)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


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


def gettimeofday() -> int:
    return round(time.time() * 1000)


def count_random(n: int, leng: int) -> float:
    a = []
    for i in range(leng):
        a.append(randint(-1000, 1000))

    summ = 0
    for i in range(n):
        start = gettimeofday()
        insertion_bin(a[:])
        end = gettimeofday()
        summ += end - start
    return summ / n


def count_up(n: int, leng: int) -> float:
    a = []
    for i in range(leng):
        a.append(i + 1)

    summ = 0
    for i in range(n):
        start = gettimeofday()
        insertion_bin(a[:])
        end = gettimeofday()
        summ += end - start
    return summ / n


def count_down(n: int, leng: int) -> float:
    a = []
    for i in range(leng, 0, -1):
        a.append(i + 1)

    summ = 0
    for i in range(n):
        start = gettimeofday()
        insertion_bin(a[:])
        end = gettimeofday()
        summ += end - start
    return summ / n


def calculate_for_table(meas: int, n: list) -> None:
    table_status_label['text'] = 'STARTING'
    rand = []
    for i in range(3):
        rand.append(count_random(meas, n[i]))

    up = []
    for i in range(3):
        up.append(count_up(meas, n[i]))

    down = []
    for i in range(3):
        down.append(count_down(meas, n[i]))
    s = 1
    create_table(tree, rand, up, down)
    table_status_label['text'] = 'DONE'


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

tit_label = Label(table_input_frame, text='Num of measurements', width=18)
tit_label.grid(row=0)
tit_entry = Entry(table_input_frame, width=20)
tit_entry.grid(row=1)
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
    int(tit_entry.get()), [int(n1_entry.get()), int(n2_entry.get()), int(n3_entry.get())]))
table_btn.grid(row=8)
# table_status_label = Label(table_input_frame, text='', width=15)
# table_status_label.grid(row=9)

git_label = Label(graph_input_frame, text='Num of measurements', width=18)
git_label.grid(row=0)
git_entry = Entry(graph_input_frame, width=20)
git_entry.grid(row=1)
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
# graph_status_label = Label(graph_input_frame, text='', width=15)
# graph_status_label.grid(row=7)

window.mainloop()
