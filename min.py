class eagle:

    species = "eagle"

    def __init__(self,name,age):
        self.name = name
        self.age = age

lulu = eagle("lulu",123)
momo = eagle("momo",456)

print("lulu is an {}".format(lulu.species))
print("momo is an {}".format(momo.species))

print("{} is {} years old".format(lulu.name,lulu.age))
print("{} is {} years old".format(momo.name,momo.age))