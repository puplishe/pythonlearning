class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1)/(x2 - x1)

coordinate1 = (3, 2)
coordinate2 = (8, 10)
point = Line(coordinate1, coordinate2)

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.pi = 3.14
        self.heigh = height
        self.rad = radius
    def volume(self):
        rad = self.rad
        heigh = self.heigh
        pi = self.pi
        return pi*heigh*rad**2
    
    def surface_area(self):
         
        rad = self.rad
        heigh = self.heigh
        pi = self.pi
        return 2*(pi*rad**2)+2*(pi*rad*heigh) 


c = Cylinder(2,3)


class Account:
    def __init__(self, name, balance = 1):
        self.name = name
        self.money = balance
    def owner(self):
        name = self.name
        return name 
    def balance(self):
        balance = self.money
        return balance 

acct1 = Account('Jose',100)
print(acct1.owner)
