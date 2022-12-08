dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]
country_dial = {country: code for code, country in dial_codes}
country_dial
{code: country.upper() 
    for country, code in sorted(country_dial.items())
    if code < 70
}

def dump(**kwargs):
    return kwargs

dump(**{'x': 1}, y=2, **{'z': 3})


d1 = {'a': 1, 'b': 3, 'd': 7}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 | d2

d1
d1 |= d2
d1
