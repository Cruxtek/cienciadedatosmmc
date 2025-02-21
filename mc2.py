import numpy as np
N = 100000
X = np.random.uniform(size = N, low = 0, high = 1)

Y = [x * (2 * x) for x in X]
E = [(x * x) * (2 * x) for x in X]



Y = X * (2 * X)
E = (X * X) * (2 * X)

N = 100000
X = np.sqrt(np.random.uniform(size = N))

import matplotlib.pyplot as plt

plt.hist(X, bins = 100, density = True)
plt.show()

print(np.mean(X), np.var(X))
import functools
#definimos el gif de como varia
import matplotlib.animation as animation

HIST_BINS = np.linspace(-4, 4, 100)

def animate(frame_number, bar_container):
    # Simulate new data coming in.
    X = rng.standard_normal(1000)
    N, _ = np.histogram(X, HIST_BINS)
    for count, rect in zip(N, bar_container.patches):
        rect.set_height(count)

    return bar_container.patches



fig, ax = plt.subplots()
_, _, bar_container = ax.hist(X, HIST_BINS, lw=1,
                              ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=55)  # set safe limit to ensure that all data is visible.

anim = functools.partial(animate, bar_container=bar_container)
ani = animation.FuncAnimation(fig, anim, 50, repeat=False, blit=True)
plt.show()

v#margen de monte carlo errorar = np.var(X)
print(np.mean(X), var, 1.96 * np.sqrt(var / N))

U = np.random.uniform(size = N // 2)
antithetic_avg = (np.sqrt(U) + np.sqrt(1.0 - U)) / 2
anti_var = np.var(antithetic_avg)
print(np.mean(antithetic_avg), anti_var, 1.96*np.sqrt(anti_var / (N / 2)))


