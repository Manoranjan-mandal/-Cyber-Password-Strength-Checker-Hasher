import re

# Password Strength Checker

def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Minimum Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    # Rule 2: Uppercase Letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    # Rule 3: Lowercase Letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    # Rule 4: Digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Rule 5: Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character.")

    # Password Strength
    if score <= 2:
        strength = "🔴 Weak"
    elif score <= 4:
        strength = "🟡 Medium"
    else:
        strength = "🟢 Strong"

    return strength, feedback


# Main Program

password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print("\n========== RESULT ==========")
print("Password Strength:", strength)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print(item)
else:
    print("\n✅ Excellent! Your password meets all security requirements.")