from matplotlib import pyplot

class PlotGraphic:

    def __init__(self, days, fast_hamsters, slow_hamsters):
        self.days = days
        self.fast_hamsters = fast_hamsters
        self.slow_hamsters = slow_hamsters

    def show_graphics(self):
        figure, axis = pyplot.subplots()

        pyplot.plot(self.days, self.fast_hamsters)
        pyplot.plot(self.days, self.slow_hamsters)

        axis.set_title('Total hamsters')
        axis.set_xlabel('Days')

        pyplot.show()