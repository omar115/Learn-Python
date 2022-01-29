class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def draw(self):
        print("draw")
        print(f"Point {self.x} and {self.y}")

point = Point(1, 2)
point.draw()
print(point.x, " ", point.y)