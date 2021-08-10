import math
class Circle(object):
    def __init__(self,r):
        self.r=r
    def get_area(self):
        return math.pi*math.pow(self.r,2)
    def get_perimeter(self):
        return math.pi*self.r*2
if __name__=='__main__':
    r=int(input('输入半径'))
    c=Circle(r)
    print(f'面积是{c.get_area()}')
    print(f'周长是{c.get_perimeter()}')
