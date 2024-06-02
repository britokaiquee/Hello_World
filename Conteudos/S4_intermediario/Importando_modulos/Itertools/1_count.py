# count é um iterador sem fim (itertools)
from itertools import count

# Você pode passar argumentos nomeados com os nomes que quiser
c1 = count(step=8, start=8)
r1 = range(8, 100, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('\ncount')
for i in c1:
    if i >= 100:
        break

    print(i)

print('\nrange')
for i in r1:
    print(i)