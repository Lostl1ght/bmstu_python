from tkinter import Tk, Frame, Entry, Label, Button
from tkinter.ttk import Treeview

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

from math import log10, floor, sin


def do():
    start = float(start_entry.get())
    interval_end = float(end_entry.get())
    step = float(step_entry.get())
    eps = float(eps_entry.get())

    results = iterations(start, interval_end, step, eps)
    create_table(results)

    create_graph(start, interval_end, results)


def f(x):
    return sin(x)#x**2-4#


def d2(x):
    return -sin(x)#2#


def d4(x):
    return sin(x)#0#


def iterations(start, interval_end, step, eps):
    def refinement(a, b, eps):
        def error(a, b):
            c = b - eps
            if f(a) * d2(a) < 0.0:
                x = a
            elif f(b) * d2(b) < 0.0:
                x = b
            delta = eps + 1.0
            itrs = 0
            while abs(delta) > eps:
                itrs += 1
                delta = f(x) * (x - c) / (f(x) - f(c))
                x -= delta
            return x, itrs

        if abs(f(a)) < eps:
            return a, 0
        if abs(f(b)) < eps:
            return b, 0

        if f(a) * d2(a) > 0.0:
            c = a
        elif f(b) * d2(b) > 0.0:
            c = b
        else:
            c = (a + b) / 2

        if f(a) * d2(a) < 0.0:
            x = a
        elif f(b) * d2(b) < 0.0:
            x = b

        delta = eps + 1.0
        itrs = 0
        while abs(delta) > eps:
            itrs += 1
            delta = f(x) * (x - c) / (f(x) - f(c))
            x -= delta
            if itrs > 100:
                return error(a, b)
        return x, itrs

    end = start + step
    results = []
    round_to = abs(int(floor(log10(eps))))

    while end < interval_end:
        if f(start) * f(end) <= 0.0:
            root, itrs = refinement(start, end, eps)
            if abs(root) < eps:
                root = 0.0
            results += [{'start': round(start, round_to + 1), 'end': round(
                end, round_to + 1), 'root': round(root, round_to), 'itrs': itrs, }]

        start = end
        end += step
    root, itrs = refinement(start, end, eps)
    if abs(root) < eps:
        root = 0.0
    results += [{'start': round(start, round_to + 1), 'end': round(
        end, round_to + 1), 'root': round(root, round_to), 'itrs': itrs, }]

    i = 0
    length = len(results)
    while i < length - 1:
        if abs(results[i]['root'] - results[i + 1]['root']) < eps:
            results.pop(i + 1)
            length -= 1
        i += 1
    return results


def create_table(results):
    global created, tree
    if created:
        tree.pack_forget()
    tree = Treeview(table_frame, columns=(
        'start', 'end', 'root', 'itrs'), height=15)

    tree.column('#0', width=160, minwidth=160)
    tree.column('start', width=160, minwidth=160)
    tree.column('end', width=160, minwidth=160)
    tree.column('root', width=160, minwidth=160)
    tree.column('itrs', width=160, minwidth=160)

    tree.heading('#0', text='Root number')
    tree.heading('start', text='Segment start')
    tree.heading('end', text='Segment end')
    tree.heading('root', text='Root X')
    tree.heading('itrs', text='It-n number')

    for line, n in zip(results, range(len(results))):
        tree.insert('', n, text=str(n),
                    values=(results[n]['start'], results[n]['end'], results[n]['root'], results[n]['itrs']))

    tree.pack()
    created = True


def iterations_for_d(start, interval_end, step, eps):
    def refinement_for_d(a, b, eps):
        def error_for_d(a, b):
            c = b - eps
            if d2(a) * d4(a) < 0.0:
                x = a
            elif d2(b) * d4(b) < 0.0:
                x = b
            delta = eps + 1.0
            itrs = 0
            while abs(delta) > eps:
                itrs += 1
                delta = d2(x) * (x - c) / (d2(x) - d2(c))
                x -= delta
            return x, itrs

        if abs(d2(a)) < eps:
            return a
        if abs(d2(b)) < eps:
            return b

        if d2(a) * d4(a) > 0.0:
            c = a
        elif d2(b) * d4(b) > 0.0:
            c = b
        else:
            c = (a + b) / 2

        if d2(a) * d4(a) < 0.0:
            x = a
        elif d2(b) * d4(b) < 0.0:
            x = b
        else:
            return None

        delta = eps + 1.0
        itrs = 0
        while abs(delta) > eps:
            itrs += 1
            delta = d2(x) * (x - c) / (d2(x) - d2(c))
            x -= delta
            if itrs > 100:
                return error_for_d(a, b)
        return x

    end = start + step
    results = []
    round_to = abs(int(floor(log10(eps))))

    while end < interval_end:
        if f(start) * f(end) <= 0.0:
            root = refinement_for_d(start, end, eps)
            if root is not None:
                if abs(root) < eps:
                    root = 0.0
                results += [round(root, round_to)]

        start = end
        end += step
    # root = refinement_for_d(start, end, 1e-5)
    # if abs(root) < eps:
    #     root = 0.0
    # results += [round(root, round_to)]

    i = 0
    length = len(results)
    while i < length - 1:
        if abs(results[i] - results[i + 1]) < eps:
            results.pop(i + 1)
            length -= 1
        i += 1
    return results


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

    scat_x = np.array(iterations_for_d(start, interval_end, 0.01, 1e-4))
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
    line2 = ax.scatter(scat_x, scat_y, color='g')
    line3 = ax.scatter(root_x, root_y, color='r')
    ax.legend((line1, line2, line3), ('Function',
                                      'Inflection points', 'Root points'))

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
