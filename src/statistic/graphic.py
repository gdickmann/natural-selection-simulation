from matplotlib import pyplot

class Graphic:
    # Total days (x axis)
    x = []

    # Variables
    slow_hamsters = []
    fast_hamsters = []

    green_hamsters = []

    pyplot.plot(x, fast_hamsters)
    pyplot.plot(x, slow_hamsters)
    pyplot.plot(x, green_hamsters)

    # Legend (top screen)
    pyplot.legend(['Fast hamsters', 'Common hamsters', 'Green hamsters'])
    # X axis legend
    pyplot.xlabel('Days')
    # Y axis legend
    pyplot.ylabel('Total hamsters')

    pyplot.grid(linestyle='-', linewidth=0.5)

    pyplot.show()