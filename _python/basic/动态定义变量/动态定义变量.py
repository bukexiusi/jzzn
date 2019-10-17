aaaa = {
    0: ["1", "2"],
    1: ["2", "2"],
    2: ["3", "2"],
    3: ["4", "2"],
    4: ["5", "2"]
}

for i in range(5):
    expression = 'var{} = {}'
    exec(expression.format(i, aaaa.get(i)))

print(var0, var1, var2, var3 ,var4)

verify = True
self = "(2018)闽0203执1号"
exec("verify = len(self) > 100")
print(verify)
