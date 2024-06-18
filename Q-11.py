# Write a python program that generates the first n numbers in the Fibonacci sequence.
a=0
b=1
num=int(input("Enter the number of terms of fibonacci sequence: "))
if num==0 :
    print("Term 1 is: ",a)
elif num==1:
    print("Term 2 is: ",b)
else:
    print("Term 1 is: ",a)
    print("Term 2 is: ",b)
    for i in range(3,num+1):
        sum=a+b
        print("Term {} is: ".format(i),sum)
        a=b
        b=sum