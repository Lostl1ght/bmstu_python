from tkinter import Tk, Frame, Entry, Label, Button, W, E
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

    results = chord_method(start, interval_end, step, eps)
    create_table(results)

    create_graph(start, interval_end, results)


def f(x):
    return sin(x)
    # return x ** 2 - 4
    # return (x - 1) ** 3 - 2

def d(x):
    return cos(x)
    # return 2 * x
    # return 3 * (x - 1) ** 2

def d2(x):
    return -sin(x)
    # return 2
    # return 6 * (x - 1)


def chord_method(start, ends, step, eps):

    def refinement(start, end, eps):
        iterations = 0
        if d(start) * d2(start) < 0:
            x = start
            def calculate(x): return x - f(x) * (end - x) / (f(end) - f(x))
        else:
            x = end
            def calculate(x): return x - f(x) * (start - x) / (f(start) - f(x))

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
        if abs(f(start)) < eps:
            x, iterations = start, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': end}]
        elif abs(f(end)) < eps:
            x, iterations = end, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': end}]
        elif f(start) * f(end) < 0:
            x, iterations = refinement(start, end, eps)
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': end}]
        start, end = end, end + step
    else:
        if abs(f(start)) < eps:
            x, iterations = start, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': ends}]
        elif abs(f(ends)) < eps:
            x, iterations = ends, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': ends}]
        elif f(start) * f(ends) < 0:
            x, iterations = refinement(start, ends, eps)
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': ends}]

    pack(roots, eps)

    return roots


def bisect(start, ends, step):
    end = start + step
    inflation = []
    eps = 1e-7
    round_to = abs(int(floor(log10(eps))))
    while start < ends:
        if abs(d2(start)) < 1e-3:
            inflation.append(round(start, round_to))
        elif abs(d2(end)) < 1e-3:
            inflation.append(round(end, round_to))
        elif d2(start) * d2(end) < 0:
            x = optimize.bisect(d2, start, end, rtol=eps)
            inflation.append(round(x, round_to))
        start, end = end, end + step
    else:
        if d2(start) * d2(ends) < 0:
            x = optimize.bisect(d2, start, ends, rtol=1e-3)
            inflation.append(round(x, round_to))

    return inflation


def create_table(results):
    global created, tree
    if created:
        tree.pack_forget()
    tree = Treeview(table_frame, columns=(
        'start', 'end', 'root', 'itrs'), height=15)

    tree.column('#0', width=160, minwidth=160, anchor=E)
    tree.column('start', width=160, minwidth=160, anchor=E)
    tree.column('end', width=160, minwidth=160, anchor=E)
    tree.column('root', width=160, minwidth=160, anchor=E)
    tree.column('itrs', width=160, minwidth=160, anchor=E)

    tree.heading('#0', text='Root number', anchor=W)
    tree.heading('start', text='Segment start', anchor=E)
    tree.heading('end', text='Segment end', anchor=E)
    tree.heading('root', text='Root X', anchor=E)
    tree.heading('itrs', text='It-n number', anchor=E)

    for line, n in zip(results, range(len(results))):
        tree.insert('', n, text=str(n + 1),
                    values=(results[n]['start'], results[n]['end'], results[n]['root'], results[n]['iterations']))

    tree.pack()
    created = True





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


def create_graph(start, interval_end, results):
    global graph_frame

    graph_frame.pack_forget()
    graph_frame = Frame(window)
    graph_frame.grid(row=1, column=1)

    root_x = []
    root_y = []
    for i in results:
        root_x.append((i['root']))
        root_y.append(0)

    x = np.arange(start, interval_end, 0.01)
    y = []
    for i in x:
        y.append(f(i))

    scat_x = np.array(bisect(start, interval_end, 0.1))
    scat_y = []
    for i in scat_x:
        scat_y.append(f(i))

    fig = plt.Figure(figsize=(8, 4), dpi=100)

    ax = fig.add_subplot(111)

    ax.plot(x, y)

    ax.set_title('y = f(x)')
    ax.set_ylabel('y')
    ax.set_xlabel('x')

    ax.hlines(0, start, interval_end, colors='black')
    ax.vlines(0, min(y), max(y), colors='black')
    line1 = mlines.Line2D([], [], color='blue')
    # line2 = ax.scatter(scat_x, scat_y, color='g')    line2,                                  'Inflection points'
    line3 = ax.scatter(root_x, root_y, color='r')
    ax.legend((line1,  line3), ('Function', 'Root points'))

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, graph_frame)
    toolbar.update()


window = Tk()
window.title('Root refinement with Chord method')
window.resizable(0, 0)

input_frame = Frame(window)
table_frame = Frame(window)
graph_frame = Frame(window)

created = False
create_table([])
create_blank()

start_label = Label(input_frame, text='Start', width=20)
end_label = Label(input_frame, text='End', width=20)
step_label = Label(input_frame, text='Step', width=20)
eps_label = Label(input_frame, text='Eps', width=20)
maxi_label = Label(input_frame, text='Max iterations', width=20)

start_entry = Entry(input_frame, width=20)
end_entry = Entry(input_frame, width=20)
step_entry = Entry(input_frame, width=20)
eps_entry = Entry(input_frame, width=20)
maxi_entry = Entry(input_frame, width=20)

btn = Button(input_frame, text='Input', width=15, command=do)

input_frame.grid(row=0, column=0)
table_frame.grid(row=0, column=1)
graph_frame.grid(row=1, column=1)

start_label.grid(row=1)
end_label.grid(row=3)
step_label.grid(row=5)
eps_label.grid(row=7)
# maxi_label.grid(row=9)

start_entry.grid(row=2)
end_entry.grid(row=4)
step_entry.grid(row=6)
eps_entry.grid(row=8)
# maxi_entry.grid(row=10)

btn.grid(row=11, column=0, columnspan=4)

window.mainloop()
