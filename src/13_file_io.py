"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

foo = open("foo.txt", 'r')

for line in foo:
    print(line.rstrip())

foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

bar = open("bar.txt", 'wt')


bar.write("Going to the Gym.\n")
bar.write("To lift some mad crazy weight.\n")
bar.write("And get all the Gains.\n")

bar = open("bar.txt", 'r')

for line in bar:
    print(line.rstrip())

bar.close()
