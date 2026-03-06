import getpass

# Govpreneur Database
USERS = {
    "admin@govpreneur.com": "password123",
    "founder@startup.gov": "innovate2026"
}

def start_login():
    print("--- GOVPRENEUR LOGIN PORTAL ---")
    email = input("Email: ").strip()
    password = getpass.getpass("Password: ")

    if email in USERS and USERS[email] == password:
        print("Access Granted. Welcome, Govpreneur.")
    else:
        print("Access Denied. Invalid Credentials.")

if _name_ == "_main_":
    start_login()
