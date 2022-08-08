# creating a list
listOne = ['Cristiano Ronaldo', 'David de Gea', 'Bruno Fernandez', 'Paul Pogba', 'Jadon Sancho']
print(listOne)

print(len(listOne))  # length of list

print(listOne[0])  # index of list

print(listOne[-1])  # negative index of list

#  list slicing is similar to strings  [start:stop:step], more about slicing in StringSlicing&Formatting.py
print(listOne[1:4:2])  # start at index 1, stop at index 4, step by 1

#  append to list
listOne.append('Edinson Cavani')

# inserting into list
listOne.insert(1, 'Alex Telles')

listTwo = ['Raphael Varane', 'Diogo Dalot']

# extending a list
listOne.extend(listTwo)
print(listOne)

# removing from list
listOne.remove('Alex Telles')

listOne.pop()  # removes last item in list

listOne.reverse()  # reverse list

listOne.sort()  # sort list
listOne.sort(reverse=True)  # sort list in reverse
# more about sorting in SortingBasics.py

minVal = min(listOne)
maxVal = max(listOne)
# sumVal = sum(listOne)  # works on integer lists

# index of a value in list
print(listOne)
print(listOne.index('David de Gea'))
