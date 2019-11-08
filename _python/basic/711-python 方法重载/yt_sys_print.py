
def yt_print(*args, sep, end):
    result = ()
    for arg in args:
        if isinstance(arg, str):
            arg = arg.encode('unicode_escape').decode("utf-8")
        arg = arg,
        result = result + arg
    print(*result, sep=sep, end=end)
