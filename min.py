class rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

nr = rectangle(10 , 12)
print("value of length = %d , width = %d"%(nr.length , nr.width))
print("area of rectangle = ", nr.area())