import re

def load_common_passwords(filepath='common_passwords.txt'):
    with open(filepath, 'r') as file:
        return set(p.strip() for p in file)

def check_password_strength(password: str) -> dict:
    score = 0
    feedback = []
    common_passwords = load_common_passwords()

    if password in common_passwords:
        feedback.append("This is a commonly used password.")
        return {"score": 0, "feedback": feedback, "strength": "Very Weak"}

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    return {
        "score": score,
        "feedback": feedback,
        "strength": ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Excellent"][score]
    }
