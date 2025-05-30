class trains:
    def __init__(self,name,day,enginetype):
        self.name=name
        self.day=day
        self.enginetype=enginetype

train1=trains("Satabdhi", 1, "Diesel")
print(train1.name, "is running on", train1.day, "with", train1.enginetype)
train2=trains("GT", 2, "Electric")
print(train2.name)


