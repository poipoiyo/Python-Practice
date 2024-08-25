# default parameter
print("----- sample 1 -----")
def print_it(a: int, b="false")->None:
    print("a = {}, b = {}".format(a, b))

print_it(3, "true")
print_it(5)


# inner function
print("\n----- sample 2 -----")
def outer(a, b):
    def inner(c, d):
        return c+d
    return inner(a, b)


print(outer(2, 4))


# decorator
print("\n----- sample 3 -----")
def debug_it(func) :
    def my_func(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return my_func

@debug_it
def add_them(a, b, c):
    return a+b+c

add_them(7, 8, 9)


# global and loca
print("\n----- sample 4 -----")
animal = "dog"
def show_animal():
    print("show_animal : ", animal)

show_animal()
print("outside_animal : ",animal)

hat = "black"
def show_hat():
    hat = "white"
    print("\nshow_hat : ", hat)

def show_global_hat():
    global hat
    print("show_global_hat : ", hat)


show_hat()
show_global_hat()
print("outside_hat : ", hat)