from tkinter import *
from tkinter.ttk import Treeview, Style

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

from math import log10, floor, sin, cos
import scipy.optimize as optimize

def do():
    create_table(tree)
    create_graph(graph_frame)


def create_table(tree):
    tree.delete(*tree.get_children())

    un = ['Упорядоченный\nмассив\n', 'Случайный\nмассив\n', 'Упорядоченный в\nобратном порядке\nмассив\n']

    tree.heading('n1', text='2000', anchor=W)
    tree.heading('n2', text='2500', anchor=W)
    tree.heading('n3', text='3000', anchor=W)

    for n in range(3):
        tree.insert('', n, values=(un[n], '1', '2', '3'))

    tree.pack()


def create_blank():
    fig = plt.Figure(figsize=(6, 3), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot()
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    s = Style()
    s.configure('Treeview', rowheight=30)

    tree = Treeview(table_frame, columns=('names', 'n1', 'n2', 'n3'),height=4)

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
    tree.insert('', 2, values=('Упорядоченный в\nобратном порядке\nмассив\n', '', '', ''))

    tree.pack()

    return tree


def create_graph(graph_frame):
    graph_frame.pack_forget()
    graph_frame = Frame(window)
    graph_frame.grid(row=1, column=1)

    x = [2000, 2500, 3000]
    y = [1, 10, 3]

    fig = plt.Figure(figsize=(6, 3), dpi=100)

    ax = fig.add_subplot(111)

    ax.plot(x, y)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


window = Tk()
window.title('Sorting methods research')
window.resizable(0, 0)

input_frame = Frame(window)
table_frame = Frame(window)
graph_frame = Frame(window)

tree = create_blank()

start_label = Label(input_frame, text='N1', width=20)
step_label = Label(input_frame, text='Step', width=20)

start_entry = Entry(input_frame, width=20)
step_entry = Entry(input_frame, width=20)

btn = Button(input_frame, text='Input', width=15, command=do)

input_frame.grid(row=0, column=0)
table_frame.grid(row=0, column=1)
graph_frame.grid(row=1, column=1)


start_label.grid(row=1)
step_label.grid(row=3)
start_entry.grid(row=2)
step_entry.grid(row=4)


btn.grid(row=5, column=0, columnspan=4)

window.mainloop()
