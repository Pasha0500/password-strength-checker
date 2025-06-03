from checker import check_password_strength

if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(f"Strength: {result['strength']}")
    for tip in result['feedback']:
        print(f"- {tip}")
