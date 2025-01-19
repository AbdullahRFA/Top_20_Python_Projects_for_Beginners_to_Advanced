while True:
    email = input("Enter your email or press 'q' to quit: ")
    if email.lower() == 'q':  # Exit condition
        print("Exiting the email verification program. Goodbye!")
        break

    if len(email) < 6:
        print("Invalid email: Length must be at least 6 characters.")
        continue

    if not email[0].isalpha():
        print("Invalid email: Email must start with an alphabet.")
        continue

    if email.count('@') != 1:
        print("Invalid email: Email must contain exactly one '@'.")
        continue

    if not (email[-4] == '.' or email[-3] == '.'):
        print("Invalid email: '.' must be at the 3rd or 4th position from the end.")
        continue

    # Checking for invalid characters
    invalid_character = False
    for char in email:
        if char.isspace():
            print("Invalid email: Email must not contain spaces.")
            invalid_character = True
            break
        if char.isalpha() and char.isupper():
            print("Invalid email: Email must not contain uppercase letters.")
            invalid_character = True
            break
        if not (char.isalnum() or char in ['_', '.', '@']):
            print("Invalid email: Email contains invalid characters.")
            invalid_character = True
            break

    if invalid_character:
        continue

    print("Valid email.")