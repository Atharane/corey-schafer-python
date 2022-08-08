import logging

'''
One might think that decorators are just functions that take another function as an argument and return a new function.
However, decorators are just a way to modify the behavior of a function without modifying its code.
The decorator is a function that takes another function as an argument and returns a new function.
The decorator function can do anything it wants with the original function, including modifying its behavior.
'''


def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text


generate_h1 = html_tag(tag='h1')
generate_h1(msg='Test Headline!')
generate_h1(msg='Another Headline!')

generate_p = html_tag(tag='p')
generate_p(msg='Test Paragraph!')

# Working with closures
logging.basicConfig(filename='closure_data.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(f'Running "{func.__name__}" with arguments {args}')
        print(func(*args))

    return log_func


'''
One might be tempted to create a decorator function without the inner function.
Creating a decorator shown below hard codes the inner function ie. foo, thus the decorator is not reusable.
Moreover, assigning it to the same variable name will overwrite the original function causing 
{maximum recursion depth exceeded while calling a Python object} infinite recursion

example: 
def foo():
    return 'foo'
    
def my_logger():
    logging.info(f'Running foo.. ')
    foo()


new_function = my_logger  # non-reusable
foo = my_logger  # infinite recursion


Again, one might be tempted to create a decorator function without the inner function.
However, this is not possible. Using such a function doesn't allow us to decorate the function w/o calling it 

example: 
def foo():
    return 'foo'
    
def my_logger(func, *args):
    logging.info(f'Running "{func.__name__}" with arguments {args}')
    func(*args)


decoratedFunction = my_logger(foo)  # my_logger function called 
'''


def add(x, y):
    return x + y


def square(x):
    return x ** 2


add_logger = logger(add)
square_logger = logger(square)

add_logger(3, 3)
add_logger(4, 5)

square_logger(10)
square_logger(20)


#  Decorators Basics

# decorator function
def decorator_function(function):
    def wrapper():
        # some code before calling the function
        print('wrapper executed this before {}'.format(function.__name__))

        result = function()

        # some more code after calling the function
        print('wrapper executed this after {}'.format(function.__name__))

        return result

    return wrapper


#  decorator class
class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method before {}'.format(self.original_function.__name__))
        self.original_function(*args, **kwargs)


'''
@decorator
def function():
    ...

is equivalent to: function = decorator(function).
'''


#  decorating a function
@decorator_function
def foo():
    print('foo')


foo()


# Practical Examples
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper
