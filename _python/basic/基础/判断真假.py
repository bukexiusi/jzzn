if "":
    print("空字符串为真")
else:
    print("空字符串为假")

if 0:
    print("0为真")
else:
    print("0为假")

a = True
b = True
c = False

d = "a and (b or c)"
print("d:", eval(d))

e = "True and (True or False)"
print("e:", eval(e))

f = d.replace("a", "True", 1)
f = f.replace("b", "True", 1)
f = f.replace("c", "False", 1)

g = d.replace("a", "True", 1).replace("b", "True", 1).replace("c", "False", 1)
# print("f:", eval(f))
print("f:", f)
print("g:", g)

dict_zn = {"name": "zn", "age": "11", "flag": True.__str__()+"1"}
for k, v in dict_zn.items():
    print("k", k)
    print("v", v)

dict_jz = {}
if dict_jz:
    print("zn")
else:
    print("jz")
for k, v in dict_jz.items():
    print("1")
print("name:", "name" in dict_zn)
print("age:", "age" in dict_zn)
print("zn:", "zn" in dict_zn)

