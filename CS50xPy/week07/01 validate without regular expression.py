email=input("What's you email?").strip().lower()

# if '@' in email and '.' in email:
#     print("Valid")
# else :
#     print("Invalid")

username , domain=email.split("@")

# if (username) and ('.' in domain):
#     print("valid")
if (username) and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
