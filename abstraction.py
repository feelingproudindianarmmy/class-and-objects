from abc import ABC, abstractmethod
class as1(ABC):
    def print(self,x):
        print(x)
    @abstractmethod
    def task(self):
        print("We are inside the abstract class")
class test(as1):
    def task(self):
        print("We are inside the test class")
bo=test()
bo.task()