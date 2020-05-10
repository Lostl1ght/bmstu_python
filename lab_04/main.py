from tkinter import *


def get_point(event, canv):
    canv.create_oval(event.x, event.y, event.x + 3,
                     event.y + 3, width=0, fill='white')
    print(event.x, event.y)


def main() -> None:
    window = Tk()
    window.resizable(0, 0)

    canv_frame = Frame(window, height=400, width=400)
    input_frame = Frame(window, height=400, width=100)
    input_frame.grid(row=0, column=0)
    canv_frame.grid(row=0, column=1)

    canv = Canvas(canv_frame, height=400, width=400, bg='green')
    canv.grid()
    canv.bind('<Button-1>', lambda event: get_point(event, canv))

    window.mainloop()


if __name__ == '__main__':
    main()
