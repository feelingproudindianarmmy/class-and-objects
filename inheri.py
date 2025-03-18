class dad:
    def __init__(self,eyes,face):
        self.eyes = eyes
        self.face = face
    def display(self):
        print("Your eye colour is",self.eyes)
        print("Your face colour is",self.face)
class son(dad):
    def __init__(self,name,age,eyes,face):
        self.name = name
        self.age = age
        super().__init__(eyes,face)
c=son("pranshu",9,"black","skin")
c.display()
print(issubclass(son,dad))