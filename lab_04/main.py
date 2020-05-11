from tkinter import *
from cnvs import *


def main():
    window = Tk()
    window.resizable(0, 0)
    window.title('Dots and triangles')

    canv_frame = Frame(window, height=400, width=400)
    input_frame = Frame(window, height=400, width=100)
    input_frame.grid(row=0, column=0)
    canv_frame.grid(row=0, column=1)

    mode = 'tri'

    canv = Canvas(canv_frame, height=400, width=400, bg='green')
    canv.grid()
    canv.bind('<Button-1>', lambda event: draw_mouse(event,
                                                     mode, canv, dots, tris, dots_tri))
    canv.bind('<Button-3>', lambda event: delete(event,
                                                 mode, canv, dots, tris, dots_tri))

    lbl = Label(input_frame, text='Triangles mode', bg='white')
    lbl.place(x=50, y=25, anchor=CENTER, width=85)

    x_entry = Entry(input_frame)
    x_entry.place(x=50, y=75, anchor=CENTER, width=75)
    x_btn = Button(input_frame, text='Input X')
    x_btn.place(x=50, y=100, anchor=CENTER, width=50)

    y_entry = Entry(input_frame)
    y_entry.place(x=50, y=150, anchor=CENTER, width=75)
    y_btn = Button(input_frame, text='Input Y')
    y_btn.place(x=50, y=175, anchor=CENTER, width=50)

    mode_btn = Button(input_frame, text='Switch mode')
    mode_btn.place(x=50, y=225, anchor=CENTER, width=80)

    mode_btn = Button(input_frame, text='Compute')
    mode_btn.place(x=50, y=275, anchor=CENTER, width=80)

    del_btn = Button(input_frame, text='Delete last')
    del_btn.place(x=50, y=325, anchor=CENTER, width=80)

    window.mainloop()


if __name__ == '__main__':
    dots = []
    tris = []
    dots_tri = []
    main()
