from cryptography.fernet import Fernet
import bcrypt
import json
import os

def main():
    # Save encrypted passwords to a file
    def save_passwords(encrypted_passwords):
        serialized_passwords = {
            username: encrypted_password.decode() for username, encrypted_password in encrypted_passwords.items()
        }
        with open('passwords.json', 'w') as file:
            json.dump(serialized_passwords, file)

    # Load encrypted passwords from a file
    def load_passwords():
        try:
            with open('passwords.json', 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def verify_master_password():
        entered_password = input("Enter the master password: ").encode('utf-8')
        return bcrypt.checkpw(entered_password, master_password_hash)

    def removefile():
        try:
            os.remove('passwords.json')
            print("Password file removed.")
        except FileNotFoundError:
            print("Password file not found.")

    def view(fer):
        try:
            for username, encrypted_password in encrypted_passwords.items():
                decrypted_password = fer.decrypt(encrypted_password).decode()
                print("Username:", username, "| Password:", decrypted_password)
        except Exception as e:
            print("Error:", e)

    def add(fer):
        username = input("Enter the account username: ")
        password = input("Enter the account password: ")

        encrypted_password = fer.encrypt(password.encode())
        encrypted_passwords[username] = encrypted_password

        print("Password added.")

    def remove():
        username_to_remove = input("Enter the username to remove: ")
        if username_to_remove in encrypted_passwords:
            del encrypted_passwords[username_to_remove]
            print(f"Password for {username_to_remove} removed.")
        else:
            print(f"Password for {username_to_remove} not found.")

    master_password_hash = b'PUT YOUR HASH HERE'
    encrypted_passwords = load_passwords()

    while not verify_master_password():
        print("Invalid master password.")

    while True:
        key = input("Enter the encryption key: ").encode('utf-8')
        try:
            fer = Fernet(key)
            break
        except ValueError:
            print("Not a valid key!")
            continue
    
    while True:
        mode = input(
            "Would you like to add a new password, view existing ones, remove existing ones, delete password file, or press q to quit (view, add, remove, remove file, q)? "
        ).lower()
        if mode == "q":
            try:
                save_passwords(encrypted_passwords)
                quit()
            except AttributeError:
                quit()

        if mode == "view":
            view(fer)
        elif mode == "add":
            add(fer)
        elif mode == "remove":
            remove()
        elif mode == "remove file":
            removefile()
        else:
            print("Invalid mode.")
            continue

if __name__ == "__main__":
    main()
