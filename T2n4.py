from posixpath import split


file=open("Tn3.txt","r")
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("other.txt","w")
clas=file.read()
dis=clas.split("\n")
i=0
while i<len(dis):
    if "delhi" in dis[i]:
        file1.write(dis[i])
        file1.write("\n")
    elif "shimla" in dis[i]:
        file2.write(dis[i])
        file2.write("\n")
    else:
        file3.write(dis[i])
        file3.write("\n")
    i+=1
file.close()