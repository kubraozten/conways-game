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

def update(*args):
    global grid, newGrid

    # calculate the sum of 8-neghbor
    grid =randomGrid
    neghbor = (grid[0:-2, 0:-2] + grid[0:-2, 1:-1] + grid[0:-2, 2:] +
               grid[1:-1, 0:-2]                    + grid[1:-1, 2:] +
               grid[2:  , 0:-2] + grid[2:  , 1:-1] + grid[2:  , 2:])
    # calculating survivors
    birth = (neghbor == 3) & (grid[1:-1, 1:-1] == 0)
    survive = ((neghbor == 2) | (neghbor == 3)) & (grid[1:-1, 1:-1] == 1)
    # reset for update (all set to dead)
    grid[...] = 0
    # update in life
    grid[1:-1, 1:-1][birth | survive] = 1
    newGrid[...] = grid
    im.set_data(newGrid)

def main():
    # call the animation
    animation = FuncAnimation(fig, update, interval=10, frames=2000)
    plt.show()

if __name__ == "__main__":
    main()

