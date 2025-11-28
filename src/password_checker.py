import string

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    strength = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong"
    }

    return strength[score]

password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))
