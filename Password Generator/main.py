import random
import string
import os
import json

PASSWORD_FILE = 'saved_passwords.json'

def load_saved_passwords():
    """Load saved passwords from a JSON file."""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            return json.load(file)
    return []

def save_passwords(passwords):
    """Save passwords to a JSON file."""
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file)

def generate_password(length, use_digits=True, use_special_chars=True):
    """Generate a random password based on user preferences."""
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    character_pool = letters + digits + special_chars

    if length <= 0 or not character_pool:
        return "Invalid password length or no character set selected."
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Load previous saved passwords
    saved_passwords = load_saved_passwords()

    while True:
        print("\nSaved Passwords:")
        for i, pwd in enumerate(saved_passwords, 1):
            print(f"{i}. {pwd}")

        # Get desired password length from the user
        while True:
            try:
                length = int(input("Enter the desired length of the password: "))
                if length < 1:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        
        # Ask if the user wants to include digits and special characters
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Generate the password
        password = generate_password(length, use_digits, use_special_chars)
        print(f"Generated password: {password}")

 
        save = input("Do you want to save this password? (y/n): ").strip().lower()
        if save == 'y':
            saved_passwords.append(password)
            save_passwords(saved_passwords)
            print("Password saved successfully.")

        # Option to delete a saved password
        delete = input("Do you want to delete a saved password? (y/n): ").strip().lower()
        if delete == 'y':
            if saved_passwords:
                try:
                    index_to_delete = int(input("Enter the number of the password to delete: ")) - 1
                    if 0 <= index_to_delete < len(saved_passwords):
                        deleted_password = saved_passwords.pop(index_to_delete)
                        save_passwords(saved_passwords)
                        print(f"Deleted password: {deleted_password}")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
            else:
                print("No saved passwords to delete.")
        
        # Option to exit
        exit_program = input("Do you want to exit? (y/n): ").strip().lower()
        if exit_program == 'y':
            break

if __name__ == "__main__":
    main()
