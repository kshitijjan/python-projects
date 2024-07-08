import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to include all character types.")

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each set
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters from all sets
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)  # Shuffle to ensure randomness
    return ''.join(password)

def main():
    print("Welcome to the Secure Password Generator!")
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            password_length = int(input("Enter the desired password length: "))
            if password_length < 4:
                print("Password length must be at least 4 characters. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for _ in range(num_passwords):
        print(generate_password(password_length))

if __name__ == "__main__":
    main()
