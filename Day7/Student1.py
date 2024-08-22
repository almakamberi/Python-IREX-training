class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    #we deal with age here
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age


studenti1=Student("Alma", 18)
studenti2=Student("Agon", 18)
print(studenti1.age)
print(studenti2.age)

