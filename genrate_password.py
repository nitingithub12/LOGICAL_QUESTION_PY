import random
import string

def generate_password(length):
    # Define characters for password generation
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    # Combine all characters
    all_chars = letters + digits + special_chars
    
    # Generate password using random choice
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

# Test the function
length = int(input("Enter the length of the password: "))
password = generate_password(length)
print("Generated password:", password)
