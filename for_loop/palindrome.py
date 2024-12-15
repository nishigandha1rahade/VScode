A = "nayan"

reverse_string=""


for i in A:
    reverse_string=reverse_string+i

    if (A==reverse_string):
        print("given String is palindrome")
    else:
        print("given string is not palindrome")