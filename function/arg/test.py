def display_decorator(func):
    def tester(*args, **kwargs):
        print(f'Log : The function {func.__name__} is executing ...')

        func(*args, **kwargs)
        print("Log : Execution completed. \n")

    return tester


@display_decorator
def say_hello(*args, **kwargs):
    print(args)


say_hello('d', 'b', 'c')
