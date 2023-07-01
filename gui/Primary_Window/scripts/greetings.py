import random

def greet():
    greetings = ['Hola !', 'Hello :)', 'Sup '+("\U0001f60e"), 'Howdy '+ ("\U0001F607"),  'Ola !' , 'Allo !', 'Hallo Mas']
    return random.choice(greetings)
