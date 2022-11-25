def keyword(*args):
    for key in args:
        print("Keyword", key)


keyword('dfdfdsdsf')


def my_func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


my_func(d=1)
