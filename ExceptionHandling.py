# exception handling in python
try:
    f = open('testfile.txt')

    corrupt = True

    if corrupt:  # raising custom exceptions
        raise Exception('File is corrupt')


except FileNotFoundError:  # specific exception
    print(f"File not found")

except Exception as e:  # this is the default exception
    print(f"Exception raised: {e}")  # e is the exception object

else:  # else block is executed if no exception is raised
    print(f.read())
    f.close()

finally:  # this is always executed, generally used to close files/ free resources
    print("Executing finally clause")
