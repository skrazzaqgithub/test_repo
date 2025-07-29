#single inheritance
class person:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def walk(self):
        print("He is walking")
cobj = person("razzaq", 35)
print(cobj.name, cobj.age)
print(cobj.walk())