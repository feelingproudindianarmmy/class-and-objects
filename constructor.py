#object and class
class fruit:
    def __init__(self,colour,name):
        self.colour=colour
        self.name=name
    def _del_(self):
        print("destructor called")
    def intro(self):
        print("My favourite fruit is",self.name)
        print("It is",self.colour)
mango=fruit("yellow","mango")
mango.intro()
banana=fruit("yellow","banana")
banana.intro()
del banana
#enumerated
l1=[1,6,4,9]
ob1=enumerate(l1)
print(list(ob1))