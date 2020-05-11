def draw(event, mode, canv, dots, tris, dots_tri):
    if mode == 'dot':
        draw_point(event, canv, dots)
    if mode == 'tri':
        draw_tri(event, canv, tris, dots_tri)


def delete(event, mode, canv, dots, tris, dots_tri):
    if len(dots) - 1 < 0:
        return
    canv.delete(dots[len(dots) - 1]['dot'])
    dots.pop(len(dots) - 1)


def draw_point(event, canv, dots):
    dot = canv.create_oval(event.x, event.y, event.x + 3,
                           event.y + 3, width=0, fill='white')
    dots.append(dict(dot=dot, x=event.x, y=event.y))


def draw_tri(event, canv, tris, dots_tri):
    dot = canv.create_oval(event.x, event.y, event.x + 3,
                           event.y + 3, width=0, fill='white')
    dots_tri.append(dict(dot=dot, x=event.x, y=event.y))
    if len(dots_tri) % 3 == 0:
        i = len(dots_tri) - 1
        tpl = (dots_tri[i]['x'], dots_tri[i]['y'], dots_tri[i - 1]['x'], dots_tri[i - 1]
               ['y'], dots_tri[i - 2]['x'], dots_tri[i - 2]['y'], dots_tri[i]['x'], dots_tri[i]['y'])
        triangle = canv.create_line(tpl, fill='white')
        tris.append(
            dict(tri=triangle, dot0=dots_tri[0], dot1=dots_tri[1], dot2=dots_tri[2]))
        print(tris)
        for l in range(3):
            canv.delete(dots_tri[i]['dot'])
            dots_tri.pop(i)
            i -= 1
