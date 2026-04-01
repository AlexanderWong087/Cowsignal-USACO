import sys
filein=open('cowsignal_in.txt','r')
output=[]

def expand_line(line,size):
    newline=''
    for i in line:
        newline+=(i*size)
    for i in range(size):
        output.append(newline)

firstline=filein.readline().split()
line_count=int(firstline[0])
length=int(firstline[1])
size=int(firstline[2])
print(line_count,size)
lines=[i.strip() for i in filein.readlines()]


for i in lines:
    expand_line(i,size)

with open('cowsignal_out.txt','w') as file:
    file.write("\n".join(output)+"\n")

sys.exit()
