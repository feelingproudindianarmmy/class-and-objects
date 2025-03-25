class student:
    __schoolname = 'Motherland Secondary School'
    def __init__(self,name,grade,age):
        self.__name = name
        self.__grade = grade
        self.__age = age
    def display(self):
        print("The name of this school is",self.__schoolname)
        print("The name of student is",self.__name)
        print("The age of student is",self.__age)
        print("The grade of student is",self.__grade)
std =student("Pranshu",3,10)
print(std.display())
print(std.__name)