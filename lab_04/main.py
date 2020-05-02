import matplotlib.pyplot as plt

plt.axes()

def kek():

    line = plt.Line2D((10, 5), (10, 0), lw=2.5)
    plt.gca().add_line(line)
    line = plt.Line2D((5, 0), (0, 0), lw=2.5)
    plt.gca().add_line(line)
    line = plt.Line2D((0, 10), (0, 10), lw=2.5)
    plt.gca().add_line(line)

def kek2():

    line = plt.Line2D((-10, -5), (-10, 0), lw=2.5)
    plt.gca().add_line(line)
    line = plt.Line2D((-5, 0), (0, 0), lw=2.5)
    plt.gca().add_line(line)
    line = plt.Line2D((0, -10), (0, -10), lw=2.5)
    plt.gca().add_line(line)

kek()


plt.axis('scaled')
plt.show()