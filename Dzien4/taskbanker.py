import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(len(friends))
#albo print(random.choice(friends)) XD
print(friends[int(random.random() * (len(friends)-1))])