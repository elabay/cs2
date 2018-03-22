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
        slope = (self.y - other.y) / (self.x - other.x)
        b = self.y - (slope * self.x)
        return "y = " + str(slope) +"x + " + str(b)

    def move (self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def circle_3(self,x2,y2,x3,y3):
        x1 = self.x
        y1 = self.y
        Tail = (2*(x1*(y2-y3)- y1*(x2-x3) +(x2*y3) - (x3*y2)))
        circle_center =(x1**2 + y1**2)*(y2-y3)+(x2**2+y2**2)*(y3-y1)+(x3**2+y3**2)*(y1-y2)/ Tail

        X = str(circle_center)

        return X

    def __str__(self):
        return "(" + str(self.x)+ "," + str(self.y) + ")"

p = Point(0,-5)
other = Point(1,1)

print(p)
#print(other)

dis = p.distance_to_point(other)
#print(dis)

#print (other.reflect_x())

#print(Point(4,11).get_line_to(Point(6,15)))
#p.move(7, 10)
center_x= p.circle_3(0,5,5,0)
print(center_x)

