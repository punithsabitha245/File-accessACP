# File Handling in Python
# Demonstrating Read, Write, and Append modes

file_write = open('File handling.txt', 'w')
print("File opened in Write Mode -")
file_write.write("This file is opened in write mode.\n")
file_write.write("Hi! I am Penguin. I am 1 year old.\n")
file_write.close()
print("Data written successfully in write mode.\n")

# 2. Append Mode ('a')
# Adds new content without removing the existing data
file_append = open('File handling.txt', 'a')
print("File opened in Append Mode -")
file_append.write("This file is opened in append mode.\n")
file_append.write("Hi again! I am Penguin, now appending data.\n")
file_append.close()
print("Data appended successfully.\n")

# 3. Read Mode ('r')
# Reads the content of the file
file_read = open('File handling.txt', 'r')
print("File opened in Read Mode -")
content = file_read.read()
print("File Content:\n")
print(content)
file_read.close()
