file=open("Tn3.txt","r")
file2=file.read()
for i in file2:
    file.write(file[i])
    file.write("\n")
    i+=1
file.close()
