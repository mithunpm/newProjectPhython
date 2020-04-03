class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"{self.name} is start to talk")


    def talk(self,name):
        print("douplicate")

person=Person("mithun");
person.talk();
person.talk(person);
