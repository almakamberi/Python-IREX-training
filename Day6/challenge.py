class klasa:
    def gjuhaprogramitit(self):
        pass

class Student(klasa):
    def __init__(self, name,gjuhaprogramuese):
        self.name = name
        self.gjuhaprogramuese = gjuhaprogramuese
    def gjuhaprogramitit(self):
        return self.gjuhaprogramuese

class Teacher(klasa):
    def __init__(self, name,gjuhaprogramuese, level):
        self.name = name
        self.gjuhaprogramuese = gjuhaprogramuese
        self.level = level
    def gjuhaprogramitit(self):
        return self.gjuhaprogramuese
    def level(self):
        return self.level

alma=Teacher("name",["html","css","python"],"adv")
Olta=Student("Olta",["java","react","python"])
print("Alma: ")
print(alma.gjuhaprogramitit())
print("Olta: ")
print(Olta.gjuhaprogramitit())