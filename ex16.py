from sys import argv

script, filename = argv
# use ex16_test.txt
print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
# target.truncate()

print("give 3 lines plz")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("lastly, close file")
target.close()

read_target = open(filename, "r")
print("\nLets read the file")
print(read_target.read())
