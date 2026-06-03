import re

#re.search(pattern,string,flags=0)

email=input("What's your email?").strip().lower()
if re.search(r"^[^ @]+@[^ @]+[.]edu$",email):
#start(^) ,whitespace baade shb thakte parbe, then @ sign , pore @ and whitespace baade shb thakte parbe , then literal dot(.) , then edu , then sesh ; in the email!
    print(f"Valid")
else :
    print(f"Invalid")

#[] : ei box e ja ja thakbe shob allowed(set of char). [abdce] -> ei 5ta word allowed
#[^a] -> a baade shb allowed (complement set of char)