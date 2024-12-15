# Python program that accepts a word from the user and reverses it.



A = input("enter your string: ")

reverse_string=""


for i in A:
    reverse_string = i+reverse_string
print(reverse_string)