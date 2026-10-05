content = """Python and Bash Assignment
This file was created using Python file handling.
Python can write text data into a file using open() and write().
"""

with open("sample.txt", "w") as file:
    file.write(content)

print("Content written to sample.txt successfully.")
