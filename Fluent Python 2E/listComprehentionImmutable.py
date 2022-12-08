def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])
fixed(tf)
# True
fixed(tm)
# False

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # unpacking
latitude
# 33.9425
longitude


divmod(20, 8)
(2, 4)
t = (20, 8)
divmod(*t)
(2, 4)
quotient, remainder = divmod(*t)
quotient, remainder
(2, 4)

path, filename = os.path.split('/home/lucas/yes.pub')
path
'/home/lucas'
filename
'yes.pub' 

a, b, *rest = range(5)
rest
[2, 3, 4]
a, b, rest
(0, 1, [2, 3, 4])


def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

fun(*[1, 2], 3, *range(4, 7))

*range(4), 4
# (0, 1, 2, 3, 4)
[*range(4), 4]
# [0, 1, 2, 3, 4]
{*range(4), 4, *(5, 6, 7)}
# {0, 1, 2, 3, 4, 5, 6, 7}

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == '__main__':
    main()


    