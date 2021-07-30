from matplotlib import pyplot

# Total days (x axis)
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Variables
slow_hamsters = [0, 0, 0, 2, 4, 6, 8, 14, 16]
fast_hamsters = [5, 6, 3, 4, 8, 10, 8, 11, 12]

pyplot.plot(x, slow_hamsters)
pyplot.plot(x, fast_hamsters)

# Legend (top screen)
pyplot.legend(['Common hamsters', 'Fast hamsters'])
# X axis legend
pyplot.xlabel('Days')
# Y axis legend
pyplot.ylabel('Total hamsters')

pyplot.grid(linestyle='-', linewidth=0.5)

pyplot.show()