from sys import argv

# use ex15_sample.txt
script, filename = argv
# txt is a variable
txt = open(filename)

print(f" Here's your file {filename}:\n")
print(txt.read())

print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
