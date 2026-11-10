file1 = open("IIBSC_CS.txt", "a")#append
file1.write("STAND-ECC-NSS-FINE ARTS \n")
file1.close()

file1 = open("IIBSC_CS.txt", "r")
print("output after appending")
print(file1.read())
print()
file1.close()

