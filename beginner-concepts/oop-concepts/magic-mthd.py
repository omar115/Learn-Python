class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} and {self.y}"
    
    def draw(self):
        print("draw")
        print(f"Point {self.x} and {self.y}")

point = Point(1, 2)
print(str(point))