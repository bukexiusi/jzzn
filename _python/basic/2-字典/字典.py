'''创建字典'''
a = {
    "a": 4,
    "b": 3,
    "c": 2,
    "d": 1,
}

b = dict([
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c')
])

c = dict.fromkeys(['a', 'b', 'c'], 'a')
print(len(a))
print(a)
print(b)
print(type(("a", "a")))
print(c)

'''字典取值'''
print(a.keys())
print(a.values())
print(a.items())

'''字典排序'''
'''利用第二种创建方式'''
'''字典是可以排序的，区别于java的hashmap'''
a_sorted = dict(sorted(a.items(), key=lambda e: e[0]))
print(a_sorted)
a_sorted = dict(sorted(a.items(), key=lambda e: e[1]))
print(a_sorted)


'''字典包含key'''
print(hasattr(a, "var_name"))
print(hasattr(a, "a"))
print("var_name" in a)
print("a" in a)
print("var_name" in a.keys())
print("a" in a.keys())
print(a)
