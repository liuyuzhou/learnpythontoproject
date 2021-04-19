class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def eat(self):
        print('Eating ...')


class Cat(Animal):
    pass


dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
