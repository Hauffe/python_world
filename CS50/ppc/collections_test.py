#collectons: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaaabbbbb"
my_counter = Counter(a)
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))


Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['a'] = 1
ordered_dict['d'] = 4
print(ordered_dict)

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

d = deque()
d.append(1)
d.append(2)
d.append(3)

d.appendleft(4)
d.pop()
d.popleft()
d.clear()
d.extendleft([5,6,7])
print(d)
d.rotate(1)
print(d)
