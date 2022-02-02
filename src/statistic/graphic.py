from matplotlib import pyplot

class Graphic:
    # Total days (x axis)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    # Variables
    slow_hamsters = [5,
4,
4,
4,
5,
4,
5,
6,
5,
5,
6,
2,
3,
6,
5,
4,
4,
5,
3,
2,
2,
2,
3,
4,
3,
3,
2,
3,
3,
2]
    fast_hamsters = [0,
1,
4,
8,
10,
11,
14,
12,
14,
12,
13,
10,
11,
13,
14,
14,
16,
17,
17,
12,
12,
12,
10,
14,
17,
18,
17,
17,
25,
23]

    green_hamsters = [0,
1,
1,
1,
2,
3,
3,
2,
4,
4,
4,
4,
5,
6,
8,
7,
7,
6,
6,
6,
6,
5,
5,
4,
5,
6,
3,
3,
3,
3]

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