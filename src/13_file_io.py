"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

with open('src/foo.txt', "r") as f:
    print("Name of the file: ", f.name)
    print("Closed or not : ", f.closed)
    print("Opening mode : ", f.mode)
    string = f.read()
    print("Read string is: ", string)


# with open('/foo.txt') as foo:
#     read_data = foo.read()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

### WORKED

with open("src/bar.txt", "w") as b:
    b.writelines("hello again world")
    b.writelines("hello again world")
    b.writelines("hello again world")
    print("Name of the file: ", b.name)
    print("Closed or not : ", b.closed)
    print("Opening mode : ", b.mode)

###DIDNT WORK

# b = open("src/bar.txt", "w")
# with open('src/bar.txt') as b:
#     b.write("hello")
#     b.write("again")
#     b.write("world")
#     print("Name of the file: ", b.name)
#     print("Closed or not : ", b.closed)
#     print("Opening mode : ", b.mode)