
from matplotlib import pyplot as plt

x = list(range(1, 9))
y = [1800, 1200, 750, 400, 350, 320, 310, 300]

plt.plot(x, y)
plt.xlabel("k")
plt.ylabel("SSE")
plt.show()