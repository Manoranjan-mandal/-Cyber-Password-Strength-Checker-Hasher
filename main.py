from getpass import getpass
from Password_checker import check_password_strength
from hasher import hash_password
from password_generator import generate_password

# ============================================
# Cyber Password Strength Checker + Hasher
# ============================================

def show_menu():
    print("\n" + "=" * 55)
    print("      CYBER PASSWORD STRENGTH CHECKER")
    print("=" * 55)
    print("1. Check Password Strength")
    print("2. Generate Secure Password")
    print("3. Generate SHA-256 Hash")
    print("4. Exit")


def main():
    while True:
        show_menu()

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            password = getpass("\nEnter your password: ")

            strength, feedback = check_password_strength(password)

            print("\n========== RESULT ==========")
            print("Password Strength:", strength)

            if feedback:
                print("\nSuggestions:")
                for item in feedback:
                    print(item)
            else:
                print("\n✅ Excellent! Your password meets all security requirements.")

        elif choice == "2":
            length = int(input("\nEnter password length (minimum 8): "))

            if length < 8:
                print("❌ Password length must be at least 8.")
            else:
                password = generate_password(length)

                print("\nGenerated Password:")
                print(password)

        elif choice == "3":
            password = getpass("\nEnter password to hash: ")

            hashed_password = hash_password(password)

            print("\n========== SHA-256 HASH ==========")
            print(hashed_password)

        elif choice == "4":
            print("\nThank you for using Cyber Password Strength Checker!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()