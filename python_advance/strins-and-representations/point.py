class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point2D: (x={}, y={})".format(self.x, self.y)
    
    # También podemos definir nuestro __format__
    def __format__(self, f):
        if f == 'r': # Reverse print
            return "Formatted Point2D: (y={}, x={})".format(self.y, self.x)
        return "Formatted Point2D: (x={}, y={})".format(self.x, self.y)
        