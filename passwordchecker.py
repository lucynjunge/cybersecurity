import hashlib

# password security
class PasswordSecurity:

    def check_strength(self, password):
        """
        Checks if the password is strong based on:
        - Minimum 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one number
        """
        if len(password) < 8:
            return False, "Password must be at least 8 characters."

        if not any(char.isupper() for char in password):
            return False, "Password must contain an uppercase letter."

        if not any(char.islower() for char in password):
            return False, "Password must contain a lowercase letter."

        if not any(char.isdigit() for char in password):
            return False, "Password must contain a number."

        return True, "Strong password."

    def hash_password(self, password):
        """
        Hashes a password using SHA-256.
        This ensures the real password is never stored.
        """
        return hashlib.sha256(password.encode()).hexdigest()


# user information
class User:
    def __init__(self, username, hashed_password):
        self.username = username
        self.hashed_password = hashed_password


# authentication system
class AuthenticationSystem:

    def __init__(self):
        self.users = {} 

    def register(self, username, password, security):
        """
        Registers a new user after validating password strength.
        """
        if username in self.users:
            print("❌ Username already exists.")
            return

        valid, message = security.check_strength(password)
        if not valid:
            print("❌", message)
            return

        hashed = security.hash_password(password)
        self.users[username] = User(username, hashed)
        print("✅ Registration successful! Password stored securely (hashed).")

    def login(self, username, password, security):
        """
        Authenticates user by comparing hashed passwords.
        """
        if username not in self.users:
            print("❌ User not found.")
            return

        hashed_input = security.hash_password(password)

        if hashed_input == self.users[username].hashed_password:
            print("✅ Login successful! Access granted.")
        else:
            print("❌ Incorrect password. Access denied.")



security = PasswordSecurity()
system = AuthenticationSystem()

print("==== SIMPLE AUTHENTICATION SYSTEM ====")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        system.register(username, password, security)

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        system.login(username, password, security)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid option. Try again.")
