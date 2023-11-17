def str_upper(func):
    def inner():
        strl=func()
        return strl.upper()
    return inner

@str_upper
def print_str():
    return "good morning"

print(print_str())
