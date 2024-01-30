#sets: unordered, mutable, no duplicates

odds = {i for i in range(1, 10, 2)}
evens = {i for i in range(0, 10, 2)}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

i = odds.difference(primes)
print(i)

i = odds.symmetric_difference(primes) # get the difference
print(i)

primes.update(evens)
print(primes)

print(primes.issubset(odds))
print(primes.issuperset(odds))
print(evens.isdisjoint(odds))

#imutable set
a = frozenset([1,3,4])
a.remove(1)