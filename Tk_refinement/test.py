from math import sin, floor, log10

def f(x):
    return sin(x)


def derivative2(x):
    return -sin(x)


def iterations(start, interval_end, step, eps):
    def refinement(a, b, eps):
        nonlocal segment, itrs, round_to
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
        # if abs(f(end)) < eps:
        #     segment += 1
        #     flag = True
        #     results += [{'number': segment, 'start': round(start, round_to + 1),
        #                 'end': round(end, round_to + 1), 'root': end,
        #                 'itrs': itrs}]
        # if abs(f(start)) < eps:
        #     segment += 1
        #     flag = True
        #     results += [{'number': segment, 'start': round(start, round_to + 1),
        #                 'end': round(end, round_to + 1), 'root': start,
        #                 'itrs': itrs}]
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


# start = float(input("Start: "))
# interval_end = float(input("End: "))
# step = float(input("Step: "))
# eps = float(input("Eps: "))

start = -10
interval_end = 10
step = 2
eps = 1e-3

results = iterations(start, interval_end, step, eps)

for i in results:
    print(i)
