from matplotlib import pyplot

class Graphic:
    # Total days (x axis)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Variables
    slow_hamsters = [5,
    4,
    4,
    4,
    4,
    3,
    3,
    3,
    2,
    2,]
    fast_hamsters = [0,
    0,
    2,
    1,
    1,
    1,
    2,
    2,
    2,
    1,]

    pyplot.plot(x, fast_hamsters)
    pyplot.plot(x, slow_hamsters)

    # Legend (top screen)
    pyplot.legend(['Fast hamsters', 'Common hamsters'])
    # X axis legend
    pyplot.xlabel('Days')
    # Y axis legend
    pyplot.ylabel('Total hamsters')

    pyplot.grid(linestyle='-', linewidth=0.5)

    pyplot.show()