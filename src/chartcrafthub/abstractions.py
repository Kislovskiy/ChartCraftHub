from matplotlib import pyplot as plt


class Plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def add(self, objs, param_dict=None):
        # https://github.com/mwaskom/seaborn/blob/9bdfc7484c15894dd35d58d3f16475389dfe4fe5/seaborn/_core/plot.py#L484
        # https://matplotlib.org/stable/users/explain/quick_start.html#making-a-helper-functions
        if param_dict is None:
            param_dict = {}
        if not isinstance(objs, (list, tuple)):
            objs = [objs]  # Convert single object to a list with single element
        for obj in objs:
            obj.plot(self.ax, param_dict)
        return self

    def get_figure(self):
        return self.fig, self.ax


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def plot(self, ax, kwargs):
        # Use default Matplotlib arguments if kwargs is not provided
        default_kwargs = {"marker": "o", "linestyle": "None", "color": "b"}
        for key, value in default_kwargs.items():
            kwargs.setdefault(key, value)

        ax.plot(self.x, self.y, **kwargs)

    def add_vector(self, vector):
        new_x = self.x + vector.end.x - vector.start.x
        new_y = self.y + vector.end.y - vector.start.y
        return Point(new_x, new_y)


class Vector:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self):
        return f"Vector({self.start}, {self.end})"

    def plot(self, ax, kwargs):
        ax.arrow(
            self.start.x,
            self.start.y,
            self.end.x - self.start.x,
            self.end.y - self.start.y,
            **kwargs,
        )

    def add(self, other_vector):
        new_start = Point(
            self.start.x + other_vector.start.x, self.start.y + other_vector.start.y
        )
        new_end = Point(
            self.end.x + other_vector.end.x, self.end.y + other_vector.end.y
        )
        return Vector(new_start, new_end)


class Polygon:
    def __init__(self, points):
        self.points = points

    def __str__(self):
        return f"Polygon({self.points})"

    def plot(self, ax, kwargs):
        xs = [point.x for point in self.points]
        ys = [point.y for point in self.points]
        ax.fill(xs, ys, **kwargs)
