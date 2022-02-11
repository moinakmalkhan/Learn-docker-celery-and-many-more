from abc import abstractclassmethod, ABCMeta


class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def get_name(self):
        pass

    @abstractclassmethod
    def get_age(self):
        pass


class PersonSignleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSignleton.__instance is None:
            raise Exception("PersonSignleton is not initialized")
        return PersonSignleton.__instance

    def __init__(self, name, age):
        if PersonSignleton.__instance is not None:
            raise Exception("PersonSignleton is already initialized")
        self.name = name
        self.age = age
        PersonSignleton.__instance = self

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


p = PersonSignleton("John", 30)
print(p.name)
print(p.age)
