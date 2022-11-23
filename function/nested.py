def outer_func(who):
    def inner_func():
        print(f"sdasdsadas, {who}")

    inner_func()


outer_func("asdsdaasdsasdads")

print(type(outer_func("asdsdaasdsasdads")))