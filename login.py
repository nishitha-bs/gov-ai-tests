user, pw = input("Username: "), input("Password: ")

if user == "admin" and pw == "gov123":
    print("Access Granted: Welcome to GovPreneurs!")
else:
    print("Access Denied: Invalid Credentials.")
