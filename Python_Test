import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return False
    
    # Uppercase and lowercase letters check
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    
    # Digit check
    if not any(char.isdigit() for char in password):
        return False
    
    # Special character check
    special_chars = "!@#$%^&*()_+[]{}|;:,.<>?/~`"
    if not any(char in special_chars for char in password):
        return False
    
    return True

def main():
    password = input("Enter your password: ")
    if check_password_strength(password):
        print("Password meets the strength criteria.")
    else:
        print("Password does not meet the strength criteria.")

if __name__ == "__main__":
    main()
