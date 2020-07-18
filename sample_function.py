from random import randint

def padding(modifier):
  random_numer = randint(1, 10)
  return random_numer + modifier

print(padding(5))
