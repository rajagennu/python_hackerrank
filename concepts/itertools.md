### Accumulate funtion

```python

In [15]: import itertools

In [16]: import operator

In [17]: data = [ 1, 2, 3, 4, 5 ]

In [18]: result = itertools.accumulate(data, operator.mul)

In [19]: result
Out[19]: <itertools.accumulate at 0x12260e0a0>

In [20]: for each in result:
    ...:     print(each)
    ...:
1
2
6
24
120

In [21]:

```

### GroupBy

```python
[list(g) for k, g in groupby('12223311')]
```

```python
for item in [list(g) for k, g in groupby('12223311')] :
  print( (len (item) , int(item[0]) ), end=" ")
```