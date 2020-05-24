# Namedtuple

There is no big difference between a Namedtuple and normal tuple.
We create a Namedtuple using `namedtuple()` function.

The big advatnage of using namedtuple is, it will avoid the headache of remembering index of each value in the tuple. 

__regular tuple__

```py
a = ( 'charlie', 30 , 'male')
b = ( 'samantha', 29, 'female')
print(a)
print(b)
```

__namedtuple__

```py
from collections import namedtuple

# create a namedtuple class

Person = namedtuple("Person", "name age gender")

# New Person object
p1 = Person("X", 23, "male")
p2 = Person("Y", 32, "female")

# print
print(p1)
print(p1.name)
print(p1.age)
print("{} is {} old and is a {} ".format(*p1));
print("{} is {} old and is a {} ".format(*p2));
```

advatnage is when you are dealing with large data strcutures, it would be easy to store and extract the data. 

