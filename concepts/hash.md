`hash` is one of the built in library in Python. We dont have to import it. 

`hash()` function will generate integer values which will use to compare dict keys during dict lookup.

syntax

```
hash(obj)
```

obj can be string, int, float.

for example if you have tuple, you can get it hash using same function as above.

```
t1 = (1, 2, 3)
print(hash(t1))
```