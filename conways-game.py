#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


# set grid size
N = 6
randomGrid = np.random.randint(0, 2, (N*100, N*100))
newGrid = np.ones(randomGrid.shape)

# set up the animation
size = np.array(randomGrid.shape)
dpi = 30.0
figsize = size[1]/float(dpi), size[0]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
im = plt.imshow(newGrid, interpolation='nearest', cmap=plt.cm.cubehelix, vmin=0, vmax=1)
plt.xticks([]), plt.yticks([])
grid = im.set_data(newGrid)


def main():
    # call the animation
    animation = FuncAnimation(fig, grid, interval=10, frames=2000)
    plt.show()

if __name__ == "__main__":
    main()

