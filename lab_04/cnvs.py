def get_point(event, canv, dots):
    dot = canv.create_oval(event.x, event.y, event.x + 3,
                     event.y + 3, width=0, fill='white')
    dots.append(dict(dot=dot, x=event.x, y=event.y))

def delete(event, canv, dots):
    if len(dots) - 1 < 0:
        return
    canv.delete(dots[len(dots) - 1]['dot'])
    dots.pop(len(dots) - 1)
