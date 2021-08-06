text=open('text.txt','r')
file=text.read()
print(file)

temp=file

text2=open('text2.txt','r')
file2=text2.read()

text=open('text.txt','w')
file=text.write(file2)

text=open('text2.txt','w')
file2=text.write(temp)


##def swap() :
   ## with 


