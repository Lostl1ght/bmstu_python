def draw_mouse(error_lbl, event, mode, canv, dots, tris, dots_tri):
    error_lbl['text'] = ''
    if mode[0] == 'dot':
        draw_point_mouse(event, canv, dots)
    if mode[0] == 'tri':
        draw_tri_mouse(event, canv, tris, dots_tri)


def delete(error_lbl, mode, canv, dots, tris, dots_tri):
    error_lbl['text'] = ''
    if mode[0] == 'dot':
        if len(dots) - 1 < 0:
            return
        canv.delete(dots[len(dots) - 1]['dot'])
        dots.pop(len(dots) - 1)
    if mode[0] == 'tri':
        if len(dots_tri) > 0:
            canv.delete(dots_tri[len(dots_tri) - 1]['dot'])
            dots_tri.pop(len(dots_tri) - 1)
        elif len(tris) > 0:
            canv.delete(tris[len(tris) - 1]['tri'])
            tris.pop(len(tris) - 1)


def draw_point_mouse(event, canv, dots):
    dot = canv.create_oval(event.x, event.y, event.x + 3,
                           event.y + 3, width=0, fill='white')
    dots.append(dict(dot=dot, x=event.x, y=event.y))
    print(dots)


def draw_tri_mouse(event, canv, tris, dots_tri):
    dot = canv.create_oval(event.x, event.y, event.x + 3,
                           event.y + 3, width=0, fill='white')
    dots_tri.append(dict(dot=dot, x=event.x, y=event.y))
    print(dots_tri)
    if len(dots_tri) % 3 == 0:
        i = len(dots_tri) - 1
        tpl = (dots_tri[i]['x'], dots_tri[i]['y'], dots_tri[i - 1]['x'], dots_tri[i - 1]
               ['y'], dots_tri[i - 2]['x'], dots_tri[i - 2]['y'], dots_tri[i]['x'], dots_tri[i]['y'])
        triangle = canv.create_line(tpl, fill='white')
        tris.append(
            dict(tri=triangle, dot0=dots_tri[i], dot1=dots_tri[i - 1], dot2=dots_tri[i - 2]))
        print(tris)
        for l in range(3):
            canv.delete(dots_tri[i]['dot'])
            i -= 1


def switch_mode(mode, mode_lbl):
    if mode[0] == 'dot':
        mode[0] = 'tri'
        mode_lbl['text'] = 'Triangles mode'
    else:
        mode[0] = 'dot'
        mode_lbl['text'] = 'Dots mode'


def draw_key(error_lbl, x_entry, y_entry, mode, canv, dots, tris, dots_tri):
    if key_check(error_lbl, x_entry, y_entry):
        return
    if mode[0] == 'dot':
        draw_point_key(x_entry, y_entry, canv, dots)
    if mode[0] == 'tri':
        draw_tri_key(x_entry, y_entry, canv, tris, dots_tri)


def draw_point_key(x_entry, y_entry, canv, dots):
    dot = canv.create_oval(int(x_entry.get()), int(y_entry.get()), int(x_entry.get()) + 3,
                           int(y_entry.get()) + 3, width=0, fill='white')
    dots.append(dict(dot=dot, x=int(x_entry.get()), y=int(y_entry.get())))
    print(dots)


def draw_tri_key(x_entry, y_entry, canv, tris, dots_tri):
    dot = canv.create_oval(int(x_entry.get()), int(y_entry.get()), int(x_entry.get()) + 3,
                           int(y_entry.get()) + 3, width=0, fill='white')
    dots_tri.append(dict(dot=dot, x=int(x_entry.get()), y=int(y_entry.get())))
    if len(dots_tri) % 3 == 0:
        i = len(dots_tri) - 1
        tpl = (dots_tri[i]['x'], dots_tri[i]['y'], dots_tri[i - 1]['x'], dots_tri[i - 1]
               ['y'], dots_tri[i - 2]['x'], dots_tri[i - 2]['y'], dots_tri[i]['x'], dots_tri[i]['y'])
        triangle = canv.create_line(tpl, fill='white')
        tris.append(
            dict(tri=triangle, dot0=dots_tri[i], dot1=dots_tri[i - 1], dot2=dots_tri[i - 2]))
        print(tris)
        for l in range(3):
            canv.delete(dots_tri[i]['dot'])
            i -= 1


def key_check(error_lbl, x_entry, y_entry):
    try:
        x_int = int(x_entry.get())
        y_int = int(y_entry.get())
        x_float = float(x_entry.get())
        y_float = float(y_entry.get())
        if x_int < x_float or y_int < y_float:
            error_lbl['text'] = 'ERROR'
            return True
        error_lbl['text'] = ''
        return False
    except:
        error_lbl['text'] = 'ERROR'
        return True
