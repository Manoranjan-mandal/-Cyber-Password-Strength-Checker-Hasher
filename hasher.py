import hashlib

# ============================================
# SHA-256 Password Hasher
# ============================================

def hash_password(password):
    """
    Generates a SHA-256 hash for the given password.

    Args:
        password (str): User password

    Returns:
        str: 64-character hexadecimal SHA-256 hash
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


# ============================================
# Run Directly (Testing)
# ============================================

if __name__ == "__main__":
    password = input("Enter a password to hash: ")

    hashed_password = hash_password(password)

    print("\n========== HASH RESULT ==========")
    print("Original Password :", password)
    print("SHA-256 Hash      :", hashed_password)