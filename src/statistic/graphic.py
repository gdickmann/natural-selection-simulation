from matplotlib import pyplot

# Total days (x axis)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Variables
slow_hamsters = [5,
6,
4,
5,
4,
2,
1,
1,
0,
0,
0,
0,
0,
0]
fast_hamsters = [0,
1,
1,
2,
3,
4,
5,
6,
7,
9,
13,
13,
16,
14]

pyplot.plot(x, slow_hamsters)
pyplot.plot(x, fast_hamsters)

# Legend (top screen)
pyplot.legend(['Common hamsters', 'Fast hamsters'])
# X axis legend
pyplot.xlabel('Days')
# Y axis legend
pyplot.ylabel('Total hamsters')

pyplot.grid(linestyle='-', linewidth=0.4)

pyplot.show()