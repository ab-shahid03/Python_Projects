"""
🔐 Project: Secure Password Manager using bcrypt
📌 Author: Abdullah Shahid
🌐 Description:
This Python project implements a simple but secure password manager
using the `bcrypt` library for password hashing and verification.
It allows users to:
    • Add and hash passwords securely
    • Save hashed credentials to a local file
    • Verify credentials against saved hashes
"""

import bcrypt
import getpass
import os

PASSWORD_FILE = "passwords.txt"

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)

def save_password(username: str, hashed: bytes):
    with open(PASSWORD_FILE, "a") as f:
        f.write(f"{username}:{hashed.decode()}\n")
    print("✅ Credentials saved successfully.")

def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return {}
    
    creds = {}
    with open(PASSWORD_FILE, "r") as f:
        for line in f:
            if ":" in line:
                user, hash_str = line.strip().split(":")
                creds[user] = hash_str.encode()
    return creds

def main():
    print("🔐 Welcome to Secure Password Manager\n")
    print("1. Add new password")
    print("2. Verify existing password")
    choice = input("Select an option (1/2): ").strip()

    if choice == "1":
        username = input("Enter username: ").strip()
        password = getpass.getpass("Enter password to hash: ")
        if not password:
            print("❌ Password cannot be empty.")
            return
        hashed = hash_password(password)
        save_password(username, hashed)

    elif choice == "2":
        creds = load_passwords()
        username = input("Enter username to verify: ").strip()
        if username not in creds:
            print("❌ Username not found.")
            return
        password = getpass.getpass("Enter password to verify: ")
        if verify_password(password, creds[username]):
            print("✅ Password verified!")
        else:
            print("❌ Password does not match.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
