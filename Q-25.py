# Write a program that copies the contents of one text file to another.
file1=open("D:/Coding/python/Assignment-1/file_1.txt","r")
file2=open("D:/Coding/python/Assignment-1/file_2.txt","w")
for line in file1:
    file2.write(line)