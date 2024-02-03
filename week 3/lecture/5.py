class Person():
    age = 15
    name = "Azamat"
    gender = "M"

    # def __init__(self):
    #     pass

    def __init__(self, name, age, gender):
        self.age = age
        self.gender = gender
        self.name = name

    def __str__(self):
        return f"{self.name} {self.age} {self.gender}"


a = Person(20, "Aisulu", "F")
print(a)
# b = Person()
# print(b)