import re

#re.search(pattern,string,flags=0)

email=input("What's your email?").strip().lower()
if re.search(r"^.+@.+[.]edu$",email):
    print(f"Valid")
else :
    print(f"Invalid")

#. : Matches any character except a newline.
# * : Matches 0 or more repetitions of the preceding token (.*@ -> @ er bam e 0 or more words ; @.* -> @ er dan e 0 or more other characters).
# + : Matches 1 or more repetitions of the preceding token.(.+@.+ -> @ er dan and bam e at least 1ta or more or more other characters to be valid!)
# ? : Matches 0 or 1 repetition of the preceding token (makes it optional).
# {m} : Matches exactly $m$ repetitions of the preceding token.
# {m,n} : Matches anywhere from $m$ to $n$ repetitions (inclusive) of the preceding token.
#Combining the raw string prefix r with the character class [.] is actually an excellent safety measure—it guarantees that Python won't touch any characters in the string, and regex will interpret the dot literally.
#^ : Matches the start of the string.
#$ : Matches the end of the string.