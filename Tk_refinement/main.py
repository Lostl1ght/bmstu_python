from tkinter import Tk, Frame, Entry, Label, Button, CENTER, W, StringVar, OptionMenu, END
from tkinter.ttk import Treeview

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

from math import log10, floor, sin, cos
import scipy.optimize as optimize


def do():
    start = float(start_entry.get())
    interval_end = float(end_entry.get())
    step = float(step_entry.get())
    eps = float(eps_entry.get())

    results = chord_method(key, start, interval_end, step, eps)
    create_table(results, tree)

    create_graph(start, interval_end, results, graph_frame)


def f(key, x):
    if key == 'sin(x)':
        return sin(x)
    elif key == 'x ** 2 - 4':
        return x ** 2 - 4
    elif key == '(x - 1) ** 3 - 2':
        return (x - 1) ** 3 - 2

def d(key, x):
    if key == 'sin(x)':
        return cos(x)
    elif key == 'x ** 2 - 4':
        return 2 * x
    elif key == '(x - 1) ** 3 - 2':
        return 3 * (x - 1) ** 2

def d2(key, x):
    if key == 'sin(x)':
        return -sin(x)
    elif key == 'x ** 2 - 4':
        return 2
    elif key == '(x - 1) ** 3 - 2':
        return 6 * (x - 1)


def chord_method(key, start, ends, step, eps):

    def refinement(key, start, end, eps):
        iterations = 0
        if d(key, start) * d2(key, start) < 0:
            x = start
            def calculate(x): return x - f(key, x) * (end - x) / (f(key, end) - f(key, x))
        else:
            x = end
            def calculate(x): return x - f(key, x) * (start - x) / (f(key, start) - f(key, x))

        x_prev, x = x, calculate(x)
        while abs(x - x_prev) >= eps:
            x_prev, x = x, calculate(x)
            iterations += 1

        return x, iterations

    def pack(roots, eps):
        r = str(abs(int(floor(log10(eps)))))
        form = '{:.' + str(r) + 'f}'

        for i in range(len(roots)):
            if abs(roots[i]['root']) < eps:
                roots[i]['root'] = abs(roots[i]['root'])
            roots[i]['root'] = form.format(roots[i]['root'])

        i = 1
        n = len(roots)
        while i < n:
            if roots[i]['root'][:len(roots[i]['root']) - 2] == roots[i - 1]['root'][:len(roots[i - 1]['root']) - 2]:
                roots.pop(i - 1)
                n -= 1
            i += 1

        max_len_root = 0
        max_len_it = 0
        max_len_start = 0
        max_len_end = 0
        for i in roots:
            if len(i['root']) > max_len_root:
                max_len_root = len(i['root'])
            if len(str(i['iterations'])) > max_len_it:
                max_len_it = len(str(i['iterations']))
            if len(str(i['start'])) > max_len_start:
                max_len_start = len(str(i['start']))
            if len(str(i['end'])) > max_len_end:
                max_len_end = len(str(i['end']))

        for i in range(len(roots)):
            roots[i]['root'] = ' ' * (max_len_root - len(roots[i]['root'])) + roots[i]['root']
            roots[i]['iterations'] = ' ' * (max_len_it - len(str(roots[i]['iterations']))) + str(roots[i]['iterations'])
            roots[i]['start'] = ' ' * (max_len_start - len(str(roots[i]['start']))) + str(roots[i]['start'])
            roots[i]['end'] = ' ' * (max_len_end - len(str(roots[i]['end']))) + str(roots[i]['end'])

    roots = []

    end = start + step
    while end < ends:
        if abs(f(key, start)) < eps:
            x, iterations = start, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': end}]
        elif abs(f(key, end)) < eps:
            x, iterations = end, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': end}]
        elif f(key, start) * f(key, end) < 0:
            x, iterations = refinement(key, start, end, eps)
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': end}]
        start, end = end, end + step
    else:
        if abs(f(key, start)) < eps:
            x, iterations = start, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': ends}]
        elif abs(f(key, ends)) < eps:
            x, iterations = ends, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': ends}]
        elif f(key, start) * f(key, ends) < 0:
            x, iterations = refinement(key, start, ends, eps)
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': ends}]

    pack(roots, eps)

    return roots


def bisect(key, start, ends, step):
    if key == 'sin(x)':
        def d22(x): return -sin(x)
    elif key == 'x ** 2 - 4':
        def d22(x): return 2
    elif key == '(x - 1) ** 3 - 2':
        def d22(x): return 6 * (x - 1)
    end = start + step
    inflation = []
    eps = 1e-7
    round_to = abs(int(floor(log10(eps))))
    while start < ends:
        if abs(d2(key, start)) < 1e-3:
            inflation.append(round(start, round_to))
        elif abs(d2(key, end)) < 1e-3:
            inflation.append(round(end, round_to))
        elif d2(key, start) * d2(key, end) < 0:
            x = optimize.bisect(d22, start, end, rtol=eps)
            inflation.append(round(x, round_to))
        start, end = end, end + step
    else:
        if d2(key, start) * d2(key, ends) < 0:
            x = optimize.bisect(d22, start, ends, rtol=1e-3)
            inflation.append(round(x, round_to))

    return inflation


def create_table(results, tree):
    tree.delete(*tree.get_children())

    for line, n in zip(results, range(len(results))):
        tree.insert('', n, values=(str(n + 1), results[n]['start'], results[n]['end'], results[n]['root'], results[n]['iterations']))

    tree.pack()


def create_blank():
    fig = plt.Figure(figsize=(8, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot()
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, graph_frame)
    toolbar.update()

    tree = Treeview(table_frame, columns=('num', 'start', 'end', 'root', 'itrs'), height=15)

    tree.column('#0', width=0, minwidth=0)
    tree.column('num', width=160, minwidth=160, anchor=CENTER)
    tree.column('start', width=160, minwidth=160, anchor=CENTER)
    tree.column('end', width=160, minwidth=160, anchor=CENTER)
    tree.column('root', width=160, minwidth=160, anchor=CENTER)
    tree.column('itrs', width=160, minwidth=160, anchor=CENTER)

    tree.heading('num', text='Root number', anchor=CENTER)
    tree.heading('start', text='Segment start', anchor=CENTER)
    tree.heading('end', text='Segment end', anchor=CENTER)
    tree.heading('root', text='Root X', anchor=CENTER)
    tree.heading('itrs', text='It-n number', anchor=CENTER)

    tree.pack()

    return tree


def create_graph(start, interval_end, results, graph_frame):
    graph_frame.pack_forget()
    graph_frame = Frame(window)
    graph_frame.grid(row=1, column=1)

    x = np.arange(start, interval_end, 0.01)
    y = []
    for i in x:
        y.append(f(key, i))

    root_x = []
    root_y = []
    for dic in results:
        root_x.append(float(dic['root']))
        root_y.append(0)           

    inf_x = np.array(bisect(key, start, interval_end, 0.1))
    inf_y = []
    for i in inf_x:
        inf_y.append(f(key, i))

    fig = plt.Figure(figsize=(8, 4), dpi=100)

    ax = fig.add_subplot(111)

    ax.plot(x, y)

    ax.set_title('y = f(x)')
    ax.set_ylabel('y')
    ax.set_xlabel('x')

    ax.hlines(0, start, interval_end, colors='black')
    ax.vlines(0, min(y), max(y), colors='black')
    line1 = mlines.Line2D([], [], color='blue')
    line2 = ax.scatter(inf_x, inf_y, color='g')                                      
    line3 = ax.scatter(root_x, root_y, color='r')
    ax.legend((line1, line2, line3), ('Function', 'Root points', 'Inflection points'))

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, graph_frame)
    toolbar.update()

def change_key(*args):
    global key, start_entry, end_entry, step_entry
    key = tkvar.get()
    start_entry.delete(0, END)
    end_entry.delete(0, END)
    step_entry.delete(0, END)


window = Tk()
window.title('Root refinement with Chord method')
window.resizable(0, 0)

input_frame = Frame(window)
table_frame = Frame(window)
graph_frame = Frame(window)

tree = create_blank()
tkvar = StringVar(window)
choices = {'sin(x)', 'x ** 2 - 4', '(x - 1) ** 3 - 2'}
tkvar.set('sin(x)')
key = 'sin(x)'
popupMenu = OptionMenu(input_frame, tkvar, *choices)
popupMenu['width'] = 12
tkvar.trace('w', change_key)

func_label = Label(input_frame, text='Function')
start_label = Label(input_frame, text='Start', width=20)
end_label = Label(input_frame, text='End', width=20)
step_label = Label(input_frame, text='Step', width=20)
eps_label = Label(input_frame, text='Eps', width=20)

start_entry = Entry(input_frame, width=20)
end_entry = Entry(input_frame, width=20)
step_entry = Entry(input_frame, width=20)
eps_entry = Entry(input_frame, width=20)
eps_entry.insert(0, '1e-4')

btn = Button(input_frame, text='Input', width=15, command=do)

input_frame.grid(row=0, column=0)
table_frame.grid(row=0, column=1)
graph_frame.grid(row=1, column=1)

func_label.grid(row = 0)
start_label.grid(row=2)
end_label.grid(row=4)
step_label.grid(row=6)
eps_label.grid(row=8)

popupMenu.grid(row = 1, columnspan=4)
start_entry.grid(row=3)
end_entry.grid(row=5)
step_entry.grid(row=7)
eps_entry.grid(row=9)

btn.grid(row=11, column=0, columnspan=4)

window.mainloop()
