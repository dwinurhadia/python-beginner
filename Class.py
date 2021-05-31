class Point:
    def move(self):
        print("move")
    def draw(self):
        print("self")

point1 = Point()
point1.draw()
point1.move()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 40
print(point2.x)