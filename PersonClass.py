class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hellow, my name is', self.name)

p = Person('Shwetanshu')
p.say_hi()
