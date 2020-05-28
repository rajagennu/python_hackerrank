### Randome - Sample - Seed 

```python

import random 

In [87]: random.seed(2)

In [88]: random.sample(range(10), 10)
Out[88]: [0, 1, 8, 2, 7, 6, 4, 3, 9, 5]

In [89]: random.seed(2)

In [90]: random.sample(range(10), 10)
Out[90]: [0, 1, 8, 2, 7, 6, 4, 3, 9, 5]

In [91]: random.sample(range(10), 10)
Out[91]: [9, 2, 6, 5, 3, 4, 8, 7, 1, 0]

```