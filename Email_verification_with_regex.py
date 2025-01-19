import re


def is_valid_email(email):
    """
    Function to validate if the given email is valid or not.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Regular expression for validating an email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Match the email against the regex
    if re.match(email_regex, email):
        return True
    else:
        return False


# Test the function
emails = [
    "example@example.com",
    "user.name@domain.co",
    "user_name@sub.domain.org",
    "invalid-email.com",
    "user@domain",
    "user@domain.c",
    "@domain.com",
    "user@.com",
    "user@domain.toolongtld"
]

print("Email Validation Results:")
for email in emails:
    result = "Valid" if is_valid_email(email) else "Invalid"
    print(f"{email}: {result}")