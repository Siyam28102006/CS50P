import re

email = input("What's your email? ").strip().lower()

#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+[.]edu+$",email)
#if re.search(r"^\w+@\w+[.]\(com|edu|net|org)$",email):
if re.search(r"^\w+@\w+[.]\w+$",email): #ekhane +$ deyar mane hocche atleast one or more words needed after
    print("Valid")
else:
    print("Invalid")

#The (com|edu|net|org) part is a group of literal words separated by the | (OR) operator. Regex looks at this group and says, "I will match exactly one of these complete options."

#CS50P Regex Quick Reference:
# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character ... as well as numbers and the underscore
# \W    not a word character
