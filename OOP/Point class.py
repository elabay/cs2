import math
class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance_to_point(self, other):
        "Calculates the distance between two points with the distance formula with an absolute value for the things in the square root "
        value = math.fabs((self.x - other.x) + (self.y - other.y))
        dis_val = math.sqrt(value)
        return dis_val

    def reflect_x(self):
        "reflects a given point over the x axis"
        new_x = self.x
        new_y = ((self.y)* -1)
        return "(" + str(new_x)+ "," + str(new_y) + ")"

    def get_line_to(self, other):



    def __str__(self):
        return "(" + str(self.x)+ "," + str(self.y) + ")"

p = Point(0,0)
other = Point(1,1)

print(p)
print(other)

dis = p.distance_to_point(other)

#print(dis)

print (other.reflect_x())
