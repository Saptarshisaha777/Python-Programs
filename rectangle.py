class rectangle:
    length=0;
    breadth=0;
    def __init__(self,l,b):
        self.length=l;
        self.breadth=b;

    def area(self):
        are = ((self.length)*(self.breadth))
        return (are)


length=float(input("The length is:"))
breadth=float(input("The Breadth is:"))
rect1=rectangle(length,breadth)
print("The area is",rect1.area())
