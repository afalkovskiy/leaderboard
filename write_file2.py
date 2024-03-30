# test program to create text file

filename = input("File name: ")

with open(filename, 'w') as outFile:
    outFile.write("This is the first line in output file\n")

    for i in range(10):
        txt = "i = " + str(i) + "\t" + str(i**3) + "\n"
        outFile.write(txt)
