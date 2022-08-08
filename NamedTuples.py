from collections import namedtuple

# list / tuple
color = (55, 155, 255)

# dictionary
color_dictionary = {'red': 55, 'green': 155, 'blue': 255}

# namedtuple - immutable with the benefits of dictionaries
Color = namedtuple('Color', ['red', 'green', 'blue'])
color_namedtuple = Color(blue=55, green=155, red=255)

Color = namedtuple('Color', ['red', 'green', 'blue'])

peacock_blue = Color(15, 44, 179)
crimson = Color(220, 20, 60)

print(crimson.blue)
