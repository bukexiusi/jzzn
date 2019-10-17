try:
    a = ["1", "2"]
    b = a[4]
except Exception as e:
    print(e)
    raise e

print("执行了这句话")


