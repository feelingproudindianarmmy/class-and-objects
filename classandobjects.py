class car:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def intro(self):
        print("My name is",self.name)
Audi=car("Audi","Red")
print(Audi.name)
print(Audi.colour)
p=Audi.intro("BMW","Yellow")
print(p)