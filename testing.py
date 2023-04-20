import numpy as np
from BeautifulPlots import set_style
import math
import matplotlib.pyplot as plt

set_style("dark_x")
#
x = np.arange(-2 * math.pi, 2 * math.pi, 0.01)
# x= x+np.random.randn(x.shape[0])/2
y = np.vectorize(math.sin)(x) + np.random.randn(x.shape[0]) / 10
y2 = np.vectorize(math.cos)(x)
y3 = np.vectorize(math.exp)(x) / 1000


plt.title("Sinus")
for i in range(1, 11):
    plt.plot(x, y - i, label="sin")
plt.xlabel("x-Werte")
plt.ylabel("y-Werte")
# outside_legend(margin=5)
# plt.legend()
plt.grid()
# plt.savefig("example.png", format='png', dpi=300)
plt.show()


x = 3 * np.random.randn(100) + 5
y = 3 * x + 2 + np.random.randn(100) * 3
plt.scatter(x[:50], y[:50])
plt.scatter(x[50:], y[50:])
plt.show()

x = np.random.standard_normal(20000)
y = np.random.standard_exponential(100)
plt.hist(x, label="ABCDEFG")
plt.legend()
plt.show()

plt.boxplot([x, y])
plt.show()


x = range(6)
y = np.random.poisson(10, 6)

plt.bar(x, y)

plt.show()
