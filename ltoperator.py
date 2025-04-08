class a:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if self.a<other.a:
            return "obj1 is less than obj2"
        else:
            return "obj1 is bigger than obj2"
    def __eq__(self,other):
        if self.a==other.a:
            return "obj1 is equal to obj2"
obj1=a(2)
obj2=a(7)
print("pass value",obj1.a,obj2.a)
print(obj1<obj2)
obj3=a(9)
obj4=a(8)
print("pass value",obj3.a,obj4.a)
print("obj3 is not equal to obj4")