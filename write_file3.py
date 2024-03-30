# test program to create text file

def primeNumCheck(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        
    return True  

j = 0
for i in range(2,100000):
    if primeNumCheck(i):
        j = j + 1
        print(str(j) + '\t' + str(i))

filename = input("File name: ")

with open(filename, 'w') as outFile:
    outFile.write("This is the first line in output file\n")

    for i in range(10):
        txt = "i = " + str(i) + "\t" + str(i**3) + "\n"
        outFile.write(txt)
