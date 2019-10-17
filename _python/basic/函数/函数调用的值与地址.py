# 值传递
def f1(a):
    a = a + 1
b = 1
f1(b)
print(b)

# 址传递
def f2(a):
    a["id2"] = "2"
b = {"id": "1"}
f2(b)
print(b)