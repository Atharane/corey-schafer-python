def garbage():
    # getting help in python
    x = 'lorem ipsum'
    print(dir(x))  # dir() is a function that returns a list of all the attributes and methods of an object
    help(str)  # help() is a function that returns the documentation of an object
    help(str.upper)

    exit()

    # Python Ternary Operator
    age = 10

    can_vote = True if age >= 18 else False
