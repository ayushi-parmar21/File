name=open("Tn1.txt","r")
file=name.read()
f=file.split("\n")
count=0
for i in (f):
    if i:
        count+=1
print(count)
name.close()