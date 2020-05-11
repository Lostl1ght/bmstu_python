def draw_mouse(event, mode, canv, dots, tris, dots_tri):
    if mode[0] == 'dot':
        draw_point_mouse(event, canv, dots)
    if mode[0] == 'tri':
        draw_tri_mouse(event, canv, tris, dots_tri)


def delete(mode, canv, dots, tris, dots_tri):
    if mode[0] == 'dot':
        if len(dots) - 1 < 0:
            return
        canv.delete(dots[len(dots) - 1]['dot'])
        dots.pop(len(dots) - 1)
    if mode[0] == 'tri':
        if len(dots_tri) > 0:
            canv.delete(dots_tri[len(dots_tri) - 1][0])
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
    dots_tri.append(list((dot, event.x, event.y)))
    if len(dots_tri) % 3 == 0:
        i = len(dots_tri) - 1
        tpl = (dots_tri[i][1], dots_tri[i][2], dots_tri[i - 1][1], dots_tri[i - 1]
               [2], dots_tri[i - 2][1], dots_tri[i - 2][2], dots_tri[i][1], dots_tri[i][2])
        triangle = canv.create_line(tpl, fill='white')
        dot0 = dict(x=dots_tri[0][1], y=dots_tri[0][2])
        dot1 = dict(x=dots_tri[1][1], y=dots_tri[1][2])
        dot2 = dict(x=dots_tri[2][1], y=dots_tri[2][2])
        tris.append(
            dict(tri=triangle, dot0=dot0, dot1=dot1, dot2=dot2))
        print(tris)
        for l in range(3):
            canv.delete(dots_tri[i][0])
            dots_tri.pop(i)
            i -= 1


def switch_mode(mode, lbl):
    if mode[0] == 'dot':
        mode[0] = 'tri'
        lbl['text'] = 'Triangles mode'
    else:
        mode[0] = 'dot'
        lbl['text'] = 'Dots mode'
