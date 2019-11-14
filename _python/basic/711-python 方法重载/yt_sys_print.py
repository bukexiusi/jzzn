
def yt_print(*args, sep, end):
    result = ()
    for arg in args:
        arg = str(arg)
        arg = arg.encode('unicode_escape').decode("utf-8"),
        result = result + arg
    print(*result, sep=sep, end=end)


