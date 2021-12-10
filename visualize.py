import matplotlib.pyplot as plt
from a_star import get_index


# c is the columns
# figure is the plot to be worked on
# locations of the tiles in the current step
def update_grid(c, figure, locations):
    # get all subplots
    axis = figure.get_axes()

    # for each subplot
    for x in range(len(axis)):
        # get the index of tile x
        index = get_index(locations, str(x))

        # update the title of the subplot
        title = locations[index[0]][index[1]]
        if title == '0':
            title = ''
        h = -(axis[x].bbox.height / 2)
        axis[index[0] * c + index[1]].set_title(title, y=1, pad=h)


# r is the rows
# c is the columns
# creates a grid of size r x c
def create_grid(r, c):
    size = r * c

    # creates the plot
    figure = plt.figure()

    # r * c number of subplots
    for x in range(1, size + 1):
        axis = figure.add_subplot(r, c, x)
        axis.xaxis.set_visible(False)
        axis.yaxis.set_visible(False)

    # remove whitespace between subplots
    plt.subplots_adjust(wspace=0, hspace=0)
    return figure


# paths is the path to reach the goal state from the initial state
# name is the name of the search
def visualize_paths(paths, name):
    # get # of rows and columns
    rows = len(paths[-1])
    cols = len(paths[-1][0])

    # make it updatable
    plt.ion()

    # create the figure
    figure = create_grid(rows, cols)
    figure.suptitle(name + ' Search', fontsize=16)

    # for each step in reaching goal state, update the graph
    for step in paths:
        update_grid(cols, figure, step)
        plt.pause(0.75)

    # show the graph
    plt.show()

    # close the graph
    plt.pause(2)
    plt.close(figure)
