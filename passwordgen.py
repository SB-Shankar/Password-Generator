import random
import string

def generate_password(length):
    # Define the character set: uppercase, lowercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main program
if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length (e.g., 12): "))
        if length <= 0:
            print("Password length must be a positive integer.")
        else:
            password = generate_password(length)
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid integer for the password length.")