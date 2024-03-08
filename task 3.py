import secrets
import string

def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

# Example usage
password = generate_password()
print("Generated Password:", password)
