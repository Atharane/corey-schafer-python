"""
generators are a way to create iterators, which are iterable objects
generators are not stored in memory but are created on the fly when needed.
Thus, the programme takes up less memory than lists and tuples.
A generator can be typecast into a list using function: list(), but that negates the benefits of generators.
"""

import random
import time

import memory_profiler as profiler

# create a list of strings
list_numbers = ['one', 'two', 'three', 'four', 'five']

# create a generator object
generator_one = (i for i in list_numbers)

# iterate through the generator object
for i in generator_one:
    print(i)


# function to generator a generator object
def square_numbers(nums):
    for i in nums:
        print('generator function called... ', end='')
        yield i ** 2


# creating a generator object using a generator function
my_nums = square_numbers([1, 2, 3, 4, 5])

# creating a generator object through comprehension
my_nums2 = (x ** 2 for x in [1, 2, 3, 4, 5])

# print(list(my_nums))  # [1, 4, 9, 16, 25] - list() converts generator object into a list

# for num in my_nums:
#     print(num)

# Analysing the performance of generators, in terms of memory usage


names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(profiler.memory_usage()))


# regular function that returns a list
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


# generator function
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


# Analysing lists
# start = time.time()
# people = people_list(1000000)
# stop = time.time()

# Analysing generators
start = time.time()
people = people_generator(1000000)
stop = time.time()

print('Memory (After) : {}Mb'.format(profiler.memory_usage()))
print('Took {} Seconds'.format(stop - start))
