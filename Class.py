class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("self")

point = Point(20,30)
print(point.x)