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
    return x ** 2 -4


def derivative2(x):
    return 2


def iterations(start, interval_end, step, eps):
    def refinement(a, b, eps):
        nonlocal segment, itrs, round_to
        delta_x = eps + 1.0
        segment += 1
        if derivative2(a) * f(a) > 0.0:
            x0 = a
            x = x0 + eps
        elif derivative2(b) * f(b) > 0.0:
            x0 = b
            x = x0 - eps
        else:
            x0 = (a + b) / 2
            x = x0 - 0.1

        while abs(delta_x) > eps:
            itrs += 1
            delta_x = f(x) * (x - x0) / (f(x) - f(x0))
            x -= delta_x

        return x

    end = start + step
    results = []
    segment = 0
    round_to = abs(int(floor(log10(eps))))
    flag = False
    while end <= interval_end:
        if flag:
            flag = False
            continue
        itrs = 0
        if abs(f(end)) < eps:
            segment += 1
            flag = True
            results += [{'number': segment, 'start': round(start, round_to + 1),
                        'end': round(end, round_to + 1), 'root': end,
                        'itrs': itrs}]
        if abs(f(start)) < eps:
            segment += 1
            flag = True
            results += [{'number': segment, 'start': round(start, round_to + 1),
                        'end': round(end, round_to + 1), 'root': start,
                        'itrs': itrs}]
        if f(start) * f(end) < 0.0:
            root = refinement(start, end, eps)
            results += [{'number': segment, 'start': round(start, round_to + 1),
                         'end': round(end, round_to + 1), 'root': round(root, round_to),
                         'itrs': itrs}]
        
        start = end
        end += step
        if end > interval_end - step:
            break
    itrs = 0
    if f(start) * f(end) < 0.0:
            root = refinement(end - step, end, eps)
            results += [{'number': segment, 'start': round(start, round_to + 1),
                         'end': round(end, round_to + 1), 'root': round(root, round_to),
                         'itrs': itrs}]
    return results


def create_table(results):
    global created, tree
    if created:
        tree.pack_forget()
    tree = Treeview(table_frame, columns=('start', 'end', 'root', 'itrs'), height=15)

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
        tree.insert('', n, text=results[n]['number'],
                    values=(results[n]['start'], results[n]['end'], results[n]['root'], results[n]['itrs']))

    tree.pack()
    created = True


def iterations_for_d(start, interval_end):
    def refinement_for_d(a, b):
        delta_x = 1e-4 + 1.0
        if derivative2(a) > 0.0:
            x0 = a
            x = b
        else:
            x0 = b
            x = a

        while abs(delta_x) > 1e-4:
            delta_x = derivative2(x) * (x - x0) / (derivative2(x) - derivative2(x0))
            x -= delta_x

        return x

    end = start + 0.1
    results = []
    while end <= interval_end:
        if f(start) * f(end) < 0.0:
            results += [refinement_for_d(start, end)]

        if end == interval_end:
            break

        start = end
        end += 0.1

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

    fig = plt.Figure(figsize=(8, 4), dpi=100)

    ax = fig.add_subplot(111)

    ax.plot(np.arange(start, interval_end, 0.01), f(np.arange(start, interval_end, 0.01)))

    ax.set_title('y = f(x)')
    ax.set_ylabel('y')
    ax.set_xlabel('x')

    ax.hlines(0, min(np.arange(start, interval_end, 0.01)), max(np.arange(start, interval_end, 0.01)), colors='black')
    ax.vlines(0, min(f(np.arange(start, interval_end, 0.01))), max(f(np.arange(start, interval_end, 0.01))),
              colors='black')
    line1 = mlines.Line2D([], [], color='blue')
    line2 = ax.scatter(np.array(iterations_for_d(start, interval_end)),
                       f(np.array(iterations_for_d(start, interval_end))),
                       color='g')
    line3 = ax.scatter(root_x, root_y, color='r')
    ax.legend((line1, line2, line3), ('Function', 'Inflection points', 'Root points'))

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
