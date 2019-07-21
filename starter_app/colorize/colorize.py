from termcolor import colored


def colorize(message):
    return colored(message, 'red', attrs=['reverse', 'blink'])
