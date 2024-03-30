# test program to create text file

filename = input("File name: ")

with open(filename, 'w') as outFile:
    outFile.write("This is the first line in output file\n")
    outFile.write("This is the second line in output file\n")
    outFile.write("The third line in output tile\n")
