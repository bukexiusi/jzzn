try:
    try:
        param = ["1"]
        a = param[1]
    except Exception as e:
        print(str(e))
        raise isinstance(e, IndexError)
except Exception as e_:
    print(str(e_))

# 捕获多个异常
try:
    try:
        param = ["1"]
        a = param[1]
    except Exception as e:
        print(str(e))
        raise isinstance(e, IndexError)
except (IndexError, Exception) as e_:
    print(str(e_))

# 断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

foo('0')

