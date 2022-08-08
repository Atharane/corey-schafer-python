# working with files the naive way
f = open('workfile.txt', 'a')  # open file in write mode, default is read mode
f.write('\nSubstitutes: \n')
f.write('Mason Greenwood\n')
f.write('Jadon Sancho\n')
f.write('Frederico Rodrigues\n')
f.close()  # requires explicit close statement, else can lead to resource leak

# working with files using with statement/ context manager
with open('workfile.txt', 'r+') as f:
    file_contents = f.read()  # reads the entire file contents
    print('Reading file contents using read() method: ')
    print(file_contents)

    f.seek(0)  # moves the cursor to the beginning of the file

    print('Reading file using readline method:')
    print(f.readline(), end='')  # reads the first line
    print(f.readline(), end='')  # reads the first line
    print(f.readline(), end='')  # reads the first line


'''
if an exception is thrown, the file will be closed automatically
file is automatically closed when the with statement is exited
although the file is automatically closed, the file object is still available
'''
