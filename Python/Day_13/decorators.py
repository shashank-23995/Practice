# we define a decorator
def log(orignal_function):
    def new_function(*args, **kwargs):
        print("Function %s called with positional arguments %s\
        and keyword arguments %s.\n" % (
            orignal_function.__name__, args, kwargs))

        return orignal_function(*args, **kwargs)
    return new_function


# here is function to decorate
@log
def print_a_message(message):
    print(message)

# and here is how we decorate it
import pdb; pdb.set_trace()
# print_a_message = log(print_a_message)

print_a_message("Hello World")
