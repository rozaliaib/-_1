class Animals:

    color = ''
    age = 0

    def eating(self):
        print('I can eat')

    def moving(self):
        print('I can move')

    def sleeping(self):
        print('I can sleep')


class Mammals(Animals):
    legs = 4

    def feeding_by_milk(self):
        print('Eat my MILK')

    def walk(self):
        print('I can walk')

dude = Mammals()

class Dogs(Mammals):

    def __init__(self, name):
        self.name = name


    def bark(self):
        print('Гав')

dog1 = Dogs('Prosha')
print('Собаку зовут', dog1.name)
dog1.bark()

dog2 = Dogs('Sharik')
print('Собаку зовут', dog2.name)
dog2.bark()

dog3 = Dogs('Dog')
print('Собаку зовут', dog3.name)
dog3.bark()

class Cats(Mammals):


    def __init__(self, name):
        self.name = name

    def meow(self):
        print('meooow')

cat1 = Cats('Kuzya')
print('Кошку зовут', cat1.name)
cat1.meow()

cat2 = Cats('Oskar')
print('Кошку зовут', cat2.name)
cat2.meow()

cat3 = Cats('Seva')
print('Кошку зовут', cat3.name)
cat3.meow()
class Birds(Animals):
    wings = 2

    def fly(self):
        print('I can fly!')

class Sparrow(Birds):
    def __init__(self, name):
        self.name = name

    def tweet(self):
        print('tweet-tweet-tweet')

sparrow1 = Sparrow('Olya')
print('Воробья зовут', sparrow1.name)
sparrow1.tweet()





