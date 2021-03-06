import numpy as np
import matplotlib.pyplot as pyplot


def essai_courbe():
    """ Ceci est un essai de dessin """
    # x-axis values
    roll_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # y-axis values
    marks = [55, 75, 96, 75, 36, 45, 87, 99, 100]

    pyplot.plot(roll_num, marks)

    pyplot.show()


def essai_sinus() -> object:
    """ Dessin de sinus """
    pyplot.style.use('_mpl-gallery')

    # make data
    x = np.linspace(0, 10, 100)
    y = 4 + 2 * np.sin(2 * x)

    # plot
    fig, ax = pyplot.subplots()

    ax.plot(x, y, linewidth=2.0)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    pyplot.show()
