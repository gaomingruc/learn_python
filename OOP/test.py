class Person(object):
    people_number = 0

    def __init__(self, name):
        self.name = name
        # self.__class__.people_number += 1
        Person.people_number += 1
    
    def say_hello(self):
        print("你好，我是%s" % self.name)

    @staticmethod
    def say_something():
        print("blabla")

    @classmethod
    def get_people_number(cls):
        print(cls.people_number)


if __name__ == "__main__":
    laowang = Person("老王")
    laowang.say_hello()
    laowang = Person("老王")
    laowang.say_hello()
    Person.say_something()
    Person.get_people_number()