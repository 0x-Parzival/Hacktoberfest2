# Python program to check whether a character is alphabet or not

# take input
ch = input("Enter any character: ")

# check charater is alphabet or not
if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
    print(ch, "is an Alphabet.")
else:
    print(ch, "is not an Alphabet.")
