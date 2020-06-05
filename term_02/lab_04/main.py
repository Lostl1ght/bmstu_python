from tkinter import Tk, Frame, Canvas, Label, Entry, Button, CENTER
from cnvs import *
from mth import *


def main():
    minimum = 400
    if size < minimum:
        print('Fuck you!')
        return
    window = Tk()
    window.resizable(0, 0)
    window.title('Dots and triangles')

    canv_frame = Frame(window, height=size, width=size)
    input_frame = Frame(window, height=size, width=100)
    input_frame.grid(row=0, column=0)
    canv_frame.grid(row=0, column=1)

    mode = ['tri']

    canv = Canvas(canv_frame, height=size, width=size, bg='green')
    canv.grid()
    canv.bind('<Button-1>', lambda event: draw_mouse(error_lbl,
                                                     event, mode, canv, dots, tris, dots_tri, lines))
    canv.bind('<Button-3>', lambda event: delete(error_lbl,
                                                 mode, canv, dots, tris, dots_tri, lines))

    mode_lbl = Label(input_frame, text='Triangles mode')
    mode_lbl.place(x=50, y=25, anchor=CENTER, width=85)

    error_lbl = Label(input_frame, text='')
    error_lbl.place(x=50, y=375, anchor=CENTER, width=85)

    x_lbl = Label(input_frame, text='Input X')
    x_lbl.place(x=50, y=75, anchor=CENTER, width=75)
    x_entry = Entry(input_frame, justify=CENTER)
    x_entry.place(x=50, y=100, anchor=CENTER, width=75)

    y_lbl = Label(input_frame, text='Input Y')
    y_lbl.place(x=50, y=125, anchor=CENTER, width=75)
    y_entry = Entry(input_frame, justify=CENTER)
    y_entry.place(x=50, y=150, anchor=CENTER, width=75)

    inpt_btn = Button(input_frame, text='Input', command=lambda: draw_key(
        error_lbl, x_entry, y_entry, mode, canv, dots, tris, dots_tri, size, lines))
    inpt_btn.place(x=50, y=175, anchor=CENTER, width=50)

    mode_btn = Button(input_frame, text='Switch mode',
                      command=lambda: switch_mode(mode, mode_lbl))
    mode_btn.place(x=50, y=225, anchor=CENTER, width=80)

    comp_btn = Button(input_frame, text='Compute',
                      command=lambda: compute(dots, tris, lines, canv, size))
    comp_btn.place(x=50, y=250, anchor=CENTER, width=80)

    del_btn = Button(input_frame, text='Delete last', command=lambda: delete(
        error_lbl, mode, canv, dots, tris, dots_tri, lines))
    del_btn.place(x=50, y=300, anchor=CENTER, width=80)

    clear_btn = Button(input_frame, text='Clear', command=lambda: clear(
        canv, dots, tris, dots_tri, lines, error_lbl))
    clear_btn.place(x=50, y=325, anchor=CENTER, width=80)

    window.mainloop()


if __name__ == '__main__':
    dots = []
    tris = []
    dots_tri = []
    size = 800  # Not less than 400.
    lines = []
    main()
