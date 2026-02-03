import math
class Point:
    def __init__(self,x,y):
        self.x_coordinate=x
        self.y_coordinate=y
    def __str__(self):
        return "<{},{}>\n<{},{}>".format(self.f,self.s,self.fy,self.sy)
    def distance_formula(self,value):
        f=math.sqrt(((value.x_coordinate-self.x_coordinate)**2)+((value.y_coordinate-self.y_coordinate)**2))
        return "%.3f" % f
obj=Point(5,4)
print(obj.distance_formula(2,3))

