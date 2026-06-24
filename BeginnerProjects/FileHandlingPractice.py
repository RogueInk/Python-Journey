# The code below is to create file txt and check name , mode , and is closed or not
# f = open("geek.txt", "w")
# print("Filename:", f.name)
# print("Mode:", f.mode)
# print("Is Closed?", f.closed)

# f.close()
# print("Is Closed?", f.closed)


# The code below is to read a file and print its content
# file = open("geek.txt", "r")
# content = file.read()
# print(content)
# file.close()

# The code below is to write in a file
with open("geek.txt", "w") as file:
    file.write("Test to write in a file")
    file.write("\nThis is for Test but who know's it might fail!")

print("File written successfully")
