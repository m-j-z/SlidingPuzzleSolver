import matplotlib.pyplot as plt
from a_star import get_index


def update_grid(c, figure, locations):
    axis = figure.get_axes()

    for x in range(len(axis)):
        index = get_index(locations, str(x))
        title = locations[index[0]][index[1]]
        if title == '0':
            title = ''
        h = -(axis[x].bbox.height / 2)
        axis[index[0] * c + index[1]].set_title(title, y=1, pad=h)


def create_grid(r, c):
    size = r * c

    figure = plt.figure()
    for x in range(1, size + 1):
        axis = figure.add_subplot(r, c, x)
        axis.xaxis.set_visible(False)
        axis.yaxis.set_visible(False)

    plt.subplots_adjust(wspace=0, hspace=0)
    return figure


def visualize_paths(paths, name):
    rows = len(paths[-1])
    cols = len(paths[-1][0])
    plt.ion()
    figure = create_grid(rows, cols)
    figure.suptitle(name + ' Search', fontsize=16)
    for step in paths:
        update_grid(cols, figure, step)
        plt.pause(0.75)
    plt.show()
    plt.pause(2)
    plt.close(figure)
