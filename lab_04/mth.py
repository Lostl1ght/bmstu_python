def compute(dots, tris, lines, canv, size):
    max_count = find_max(dots, tris)
    print('max_count =', max_count)
    ks_bs = all_maxs(dots, tris, max_count)
    print(ks_bs)


def all_maxs(dots, tris, max_count):
    ks_bs = []
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            if dots[i]['x'] - dots[j]['x'] == 0:
                count = find_if_0(dots[i]['x'], tris)
            else:
                k = (dots[i]['y'] - dots[j]['y']) / \
                    (dots[i]['x'] - dots[j]['x'])
                b = dots[i]['y'] - k * dots[i]['x']
                count = find(k, b, tris)
            if count == max_count:
                ks_bs.append(dict(k=k, b=b))
    return ks_bs


def find_max(dots, tris):
    max_count = 0
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            if dots[i]['x'] - dots[j]['x'] == 0:
                count = find_if_0(dots[i]['x'], tris)
            else:
                k = (dots[i]['y'] - dots[j]['y']) / \
                    (dots[i]['x'] - dots[j]['x'])
                b = dots[i]['y'] - k * dots[i]['x']
                count = find(k, b, tris)
                print('count =', count)
            if count > max_count:
                max_count = count

    return max_count


def find(k, b, tris):
    eps = 1e-7
    count = 0
    for i in range(len(tris)):
        if abs(tris[i]['dot0']['y'] - k * tris[i]['dot0']['x'] - b) < eps:
            count += 1
            continue
        if abs(tris[i]['dot1']['y'] - k * tris[i]['dot1']['x'] - b) < eps:
            count += 1
            continue
        if abs(tris[i]['dot2']['y'] - k * tris[i]['dot2']['x'] - b) < eps:
            count += 1
            continue

        if (higher_lower(tris[i], k, b)):
            count += 1

    return count


def higher_lower(tri, k, b):
    higher = 0
    lower = 0
    if tri['dot0']['y'] > k * tri['dot0']['x'] + b:
        higher += 1
    if tri['dot1']['y'] > k * tri['dot1']['x'] + b:
        higher += 1
    if tri['dot2']['y'] > k * tri['dot2']['x'] + b:
        higher += 1

    if tri['dot0']['y'] < k * tri['dot0']['x'] + b:
        lower += 1
    if tri['dot1']['y'] < k * tri['dot1']['x'] + b:
        lower += 1
    if tri['dot2']['y'] < k * tri['dot2']['x'] + b:
        lower += 1

    return higher == 2 and lower == 1 or higher == 1 and lower == 2


def find_if_0(x, tris):
    count = 0
    for i in range(len(tris)):
        if tris[i]['dot0']['x'] == x:
            count += 1
            continue
        if tris[i]['dot1']['x'] == x:
            count += 1
            continue
        if tris[i]['dot2']['x'] == x:
            count += 1
            continue

        if (right_left(tris[i], x)):
            count += 1

    return count


def right_left(tri, x):
    right = 0
    left = 0

    if tri['dot0']['x'] > x:
        right += 1
    if tri['dot1']['x'] > x:
        right += 1
    if tri['dot2']['x'] > x:
        right += 1

    if tri['dot0']['x'] < x:
        left += 1
    if tri['dot1']['x'] < x:
        left += 1
    if tri['dot2']['x'] < x:
        left += 1

    return right == 2 and left == 1 or right == 1 and left == 2


tris = [{'tri': 7, 'dot0': {'dot': 6, 'x': 247, 'y': 91}, 'dot1': {'dot': 5, 'x': 206, 'y': 128}, 'dot2': {'dot': 4, 'x': 158, 'y': 102}}, {'tri': 11, 'dot0': {'dot': 10, 'x': 217, 'y': 146}, 'dot1': {'dot': 9, 'x': 153, 'y': 182}, 'dot2': {'dot': 8, 'x': 116, 'y': 140}}, {
    'tri': 15, 'dot0': {'dot': 14, 'x': 106, 'y': 113}, 'dot1': {'dot': 13, 'x': 111, 'y': 86}, 'dot2': {'dot': 12, 'x': 50, 'y': 113}}, {'tri': 19, 'dot0': {'dot': 18, 'x': 111, 'y': 195}, 'dot1': {'dot': 17, 'x': 108, 'y': 167}, 'dot2': {'dot': 16, 'x': 61, 'y': 179}}]

dots = [{'dot': 1, 'x': 90, 'y': 254}, {
    'dot': 2, 'x': 76, 'y': 64}, {'dot': 3, 'x': 215, 'y': 65}]


lines = []

canv = 1
size = 3

compute(dots, tris, lines, canv, size)
