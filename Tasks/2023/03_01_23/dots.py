class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def is_on_line(self, k, b):
        return self.y == k * self.x + b


def define_line(p1: Point, p2: Point):
    k = (p1.y - p2.y) / (p1.x - p2.x)
    b = p1.y - p1.x * k

    return k, b


if __name__ == '__main__':

    a = Point(x=2, y=-1)
    b = Point(x=1, y=4)
    c = Point(x=-1, y=0)
    d = Point(x=3, y=-6)

    line = define_line(a, b)
    print(line)
    print(define_line(a,b))
    print(c.is_on_line(*line))
    print(a.is_on_line(*line))
    print(b.is_on_line(*line))
    print(d.is_on_line(*line))



