class StrKeyDict0(dict):  # <1>

    def __missing__(self, key):
        if isinstance(key, str):  # <2> Check whether key is already a str. If it is, and it’s missing, raise KeyError.
            raise KeyError(key)
        return self[str(key)]  # <3> Build str from key and look it up.

    def get(self, key, default=None):
        try:
            return self[key]  # <4> The get method delegates to __getitem__ by using the self[key] notation; that gives the opportunity for our __missing__ to act.
        except KeyError:
            return default  # <5>

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
# d['2']
# d[4]
# d[1]  <-- error

d.get('2')
d.get(4)
d.get(1, 'N/A')

2 in d
1 in d