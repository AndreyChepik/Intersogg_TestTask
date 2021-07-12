from dataclasses import dataclass


class Human:
    def __init__(self, name, surname, age, gender, profession, country, is_married, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self._profession = profession
        self.country = country
        self.is_married = is_married
        self.properties = []
        self.address = None

    def _simple_decorator(funk):
        """This is decorator that prints statements around the function"""

        def wrap(self):
            print('This is simple decorator')
            funk(self)
            print('Decorator ends')

        return wrap

    @_simple_decorator
    def eat(self):
        print(f'{self.name} is  eating')

    @property
    def profession(self):
        """Getter method for profession"""
        return self._profession

    @profession.setter
    def profession(self, new_profession):
        """Setter method for profession"""
        self._profession = new_profession

    def birthday(self):
        """Method that adds one year due to birthday"""
        self.age += 1
        return f'Happy birthday, {self.name}, now you are {self.age} years old'

    def marry(self):
        """Human may get married"""
        if self.is_married:
            return 'You can`t marry once again'
        self.is_married = True
        return 'Congratulations, you are married'

    def divorce(self):
        """Human gets divorce"""
        if self.is_married:
            self.is_married = False
            return 'You have divorced'
        return 'You can`t divorce, cos you ain`t married'

    def location(self, city, house, flat):
        """Here is composition with Address class"""
        a = Address(city, house, flat)
        self.address = a.get_address()
        return self.address

    def __call__(self, property_name, price):
        """In this method you can add properties that human has due to METACLASS.
        All created properties are added to the list of properties.
        """
        property = type(property_name, (), dict(price=price))
        self.properties.append(property)
        return property

    def __str__(self):
        return f'This is human class, {vars(self)}'

    @staticmethod
    def __doc__():
        return 'This is main human class. Class child is inherited from this class'


class Child(Human):
    def __init__(self, school, **kwargs):
        super().__init__(**kwargs)
        self.school = school

    def __str__(self):
        """Polymorphism"""
        return f'It is child class with attributes: {vars(self)}'

    @staticmethod
    def __doc__():
        """Polymorphism"""
        return 'This is child class that was inherited from Human class'


@dataclass
class Address:
    """This is dataclass that represents address of human"""
    city: str
    house: int
    flat: int

    def get_address(self):
        address = f'city: {self.city}, house: {self.house}, flat: {self.flat}'
        return address


# h = Human('andy', 'chep', 19, 'male', 'programmer', 'ukraine', False)
# c = Child(name='andy', surname='ch', age=20, gender='male', profession='driver',
#           country='USA', is_married=False, school=13)
# a = Address('London', 36, 32)
# print(a.get_address())
# h.eat()
# print(h('house', 100000))
#
