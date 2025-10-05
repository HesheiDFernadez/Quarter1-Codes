password = input("Enter your password: ")
if 8 <= len(password) <= 15:
    print("\nPassword length is valid.")
else:
    print("\nPassword too short or too long. Please try again.")
