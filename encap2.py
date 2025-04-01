class father:
    def _init_(self,name,age):
        self.name = name
        self.__age = age
    def display(self):
        print("The age of my father is",self.__age)
        print("The name of my father is",self.name)
class son(father):
    def _init_(self,name,age,gender):
        self.gender = gender
        super.__init__(name,age)
info=son("Mukesh",44,"male")
print(info.__age)
print(info.name)
