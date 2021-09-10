import numpy as np
from matplotlib import lines
import matplotlib.pyplot as plt

plt.plot([2, 4, 6, 4])
plt.ylabel = ("Numbers")
plt.xlabel('Indices')
plt.title('MyPlot')
plt.grid()
plt.show()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.xlabel = 'numbers'
plt.ylabel = "Squares"
plt.grid()
plt.show()
t = np.arange(0., 5., 0.2)
plt.plot(t, t**2, 'b--', label='^2')
plt.plot(t, t**2.2, 'rs', label='^2.2')
plt.plot(t, t**2.5, 'g^', label='^2.5')
plt.legend()
plt.grid()
plt.show()
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, linewidth=5.0)
plt.show()
x1 = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
x2 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
lines = plt.plot(x1, y1, x2, y2)
plt.setp(lines[0], color='r', linewidth=2.0)
plt.setp(lines[1], 'color', 'g', 'linewidth', 2.0)
plt.show()


def qua(num):
    return np.tan(num)


def sinq(num):
    return np.sin(num)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.grid()
plt.plot(t1, qua(t1), 'b--')
plt.subplot(212)
plt.grid()
plt.plot(t2, qua(t2), 'r-')
plt.show()

plt.figure(1)
plt.subplot(211)
plt.plot([1, 2, 3])
plt.subplot(212)
plt.plot([4, 5, 6])
plt.figure(2)
plt.plot([4, 5, 6])
plt.figure(1)
plt.subplot(212)
plt.title('Easy as 4,5,6')
plt.show()

plt.figure(1)
plt.subplot(121)
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro')
plt.grid()
plt.subplot(122)
plt.plot([1, 2, 3, 4, 5], [1, 8, 27, 64, 125], 'rs')
plt.grid()
plt.show()
