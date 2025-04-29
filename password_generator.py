import random
import string
import re

def generate_password(length=12):
    """Generate a random password with letters, digits, and symbols."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Define character pools
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits          # 0-9
    special = string.punctuation    # !@#$%^&*()_+-=[]{}|;:',.<>?/ and more

    # Ensure the password has at least one of each type
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def is_password_strong(password):
    """Check if a password is strong."""
    if len(password) < 12:  # Updated minimum length to 12
        return False, "Password must be at least 12 characters long."
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."
    if not any(char in string.punctuation for char in password):
        return False, "Password must contain at least one special character."
    
    # Check if the password is easily crackable without symbols
    password_without_symbols = ''.join(char for char in password if char not in string.punctuation)
    if password_without_symbols.isalpha() or password_without_symbols.isdigit():
        return False, "Password is too simple without symbols and can be easily cracked."

    return True, "Password is strong."

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(password_length)
    print(f"\nGenerated password : {generated_password}")
    is_strong, message = is_password_strong(generated_password)
    print(message)