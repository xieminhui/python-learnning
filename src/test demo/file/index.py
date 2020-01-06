# file


file1 = open("1.b", "wb")

len = file1.write("花田".encode("utf_32_be"))

print(len)

file1.close()

file1 = open("1.b", "rb")

by = file1.read()

print(by.decode("utf_32_be"))
