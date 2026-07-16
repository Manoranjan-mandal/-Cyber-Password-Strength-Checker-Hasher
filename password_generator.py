import random
import string

# 
# Secure Password Generator
# 

def generate_password(length=12):
    """
    Generates a secure random password.
    """

    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_-+=<>?"

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining characters
    all_characters = lowercase + uppercase + digits + symbols

    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle for randomness
    random.shuffle(password)

    return "".join(password)



# Test

if __name__ == "__main__":
    print("Generated Password:")
    print(generate_password())
