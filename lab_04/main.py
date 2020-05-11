from tkinter import *


def get_point(event, canv):
    dot = canv.create_oval(event.x, event.y, event.x + 3,
                     event.y + 3, width=0, fill='white')
    dots.append(dict(dot=dot, x=event.x, y=event.y))

def delete(event, canv):
    if len(dots) - 1 < 0:
        return
    canv.delete(dots[len(dots) - 1]['dot'])
    dots.pop(len(dots) - 1)


def main():
    window = Tk()
    window.resizable(0, 0)

    canv_frame = Frame(window, height=400, width=400)
    input_frame = Frame(window, height=400, width=100)
    input_frame.grid(row=0, column=0)
    canv_frame.grid(row=0, column=1)

    canv = Canvas(canv_frame, height=400, width=400, bg='green')
    canv.grid()
    canv.bind('<Button-1>', lambda event: get_point(event, canv))
    canv.bind('<Button-3>', lambda event: delete(event, canv))

    lbl = Label(input_frame, text='Finish input', bg='white')
    lbl.place(x=50, y=25, anchor=CENTER, width=75)

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

    del_btn = Button(input_frame, text='Delete last')
    del_btn.place(x=50, y=275, anchor=CENTER, width=80)

    window.mainloop()


if __name__ == '__main__':
    dots = []
    main()
