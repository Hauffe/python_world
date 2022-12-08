symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol)) # ord to get the code of symbols

codes_list = [ord(symbol) for symbol in symbols]


x = 'ABC'
codes = [ord(x) for x in x]

codes = [last := ord(c) for c in x]

symbols = '$¢£¥€¤'

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))


#Example 2-4. Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
('white', 'M'), ('white', 'L')]

for color in colors:
    for size in sizes:
        print((color, size))

('black', 'S')
('black', 'M')
('black', 'L')
('white', 'S')
('white', 'M')
('white', 'L')

tshirts = [(color, size) for size in sizes 
                         for color in colors]

[('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'),
('black', 'L'), ('white', 'L')]

#Example 2-5. Initializing a tuple and an array from a generator expression
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
(36, 162, 163, 165, 8364, 164)

import array
array.array('I', (ord(symbol) for symbol in symbols)) #The array constructor takes two arguments
array('I', [36, 162, 163, 165, 8364, 164])

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)