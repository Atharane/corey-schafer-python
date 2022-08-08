# Duck Typing and Easier to ask forgiveness than permission (EAFP)
#  StackOverflow:  https://stackoverflow.com/questions/12265451/ask-forgiveness-not-permission-explain

class Duck:
    @staticmethod
    def quack():
        print('Quack, quack')

    @staticmethod
    def fly():
        print('Flap, Flap!')


class Person:
    @staticmethod
    def quack():
        print("I'm Quacking Like a Duck!")

    @staticmethod
    def fly():
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    # Not Duck-Typed (Non-Pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This is not a Duck!')

    # LBYL (Non-Pythonic)
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()

        try:
            thing.quack()
            thing.fly()
            thing.bark()
        except AttributeError as e:
            print(e)


d = Duck()
p = Person()

quack_and_fly(d)
quack_and_fly(p)
