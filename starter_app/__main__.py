from starter_app.colorize.colorize import colorize
from starter_app.helper.Greeter import Greeter


def say_hello():
    greeter = Greeter('World')

    print('Usual greeting:')
    print(greeter.greet())

    print()
    print('Colored!:')
    print(colorize(greeter.greet()))


if __name__ == "__main__":
    say_hello()



