from matplotlib import pyplot as plt


class Plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def add(self, objs, kwargs=None):
        if not isinstance(objs, (list, tuple)):
            objs = [objs]  # Convert single object to a list with single element
        for obj in objs:
            obj.plot(self.ax, **kwargs)
        return self

    def get_figure(self):
        return self.fig, self.ax


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self, ax, **kwargs):
        ax.plot(self.x, self.y, **kwargs)


class Vector:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def plot(self, ax, **kwargs):
        ax.arrow(
            self.start.x,
            self.start.y,
            self.end.x - self.start.x,
            self.end.y - self.start.y,
            **kwargs,
        )


class Polygon:
    def __init__(self, points):
        self.points = points

    def plot(self, ax, **kwargs):
        xs = [point.x for point in self.points]
        ys = [point.y for point in self.points]
        ax.fill(xs, ys, **kwargs)
