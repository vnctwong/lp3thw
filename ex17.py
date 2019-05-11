from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

inData = open(from_file).read()

print(f"The input file is {len(inData)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("ready, hit return to continue, CTRL-C to abort")
input()

out_file = open(to_file, "w")
out_file.write(inData)

print("alright, all done")

out_file.close()
