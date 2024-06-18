# Write a python program that removes all punctuation from a given string.
str1=input("Enter the string : ")
for i in str1:
    if(ord(i) in range(33,48) or ord(i)in range(58,65) or ord(i)in range(91,97) or ord(i)in range(123,127)):
       pass
    else:
        new_str=str(i)
        print("The remaining string is: ",new_str)