
print("Input password: ")
password = input()
if len(password) >= 8 and any(num.isdigit() for num in password):
    print("Password is valid.")
else:
    print("Password is not valid.")
