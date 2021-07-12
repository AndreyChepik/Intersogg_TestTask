from main import Human, Child, Address


def to_bool(phrase):
    if phrase.lower() in ('да', 'yes', 'y', '+', True, 't'):
        return True
    return False


h = Human(name=input('Введите ваше имя'),
      surname=input('Введите вашу фамилию'),
      age=input('Введите ваш возраст'),
      gender=input('Введите ваш гендер'),
      profession=input('Введите вашу профессию'),
      country=input('Введите вашу страну'),
      is_married=to_bool(input('Вы женаты/замужем?')))

print(h)