import random
import string

# Lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Mighty", "Brave", "Gentle", "Sneaky", "Fierce", "Clever", "Wild", "Electric"]
nouns = ["Tiger", "Dragon", "Wolf", "Eagle", "Lion", "Shark", "Panda", "Phoenix", "Cheetah", "Bear"]

def generate_username(add_numbers=False, add_special_chars=False, length=8):
    # Select random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Combine adjective and noun
    username = adjective + noun
    
    # Add numbers if specified
    if add_numbers:
        username += str(random.randint(1, 9999))
    
    # Add special characters if specified
    if add_special_chars:
        username += random.choice(string.punctuation)
    
    # Trim or pad the username to the specified length
    if len(username) > length:
        username = username[:length]
    elif len(username) < length:
        username = username.ljust(length, random.choice(string.ascii_lowercase))
    
    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}")

def main():
    print("Welcome to the Random Username Generator!")
    
    # Get user preferences
    try:
        num_usernames = int(input("How many usernames would you like to generate? "))
        add_numbers = input("Do you want to include numbers? (yes/no): ").lower() == "yes"
        add_special_chars = input("Do you want to include special characters? (yes/no): ").lower() == "yes"
        length = int(input("What length should the usernames be? (e.g., 8): "))
    except ValueError:
        print("Invalid input, please enter valid numbers.")
        return
    
    # Generate usernames
    usernames = [generate_username(add_numbers, add_special_chars, length) for _ in range(num_usernames)]
    
    # Save to file
    save_option = input("Do you want to save the usernames to a file? (yes/no): ").lower()
    if save_option == "yes":
        filename = input("Enter the filename to save (e.g., usernames.txt): ")
        save_usernames_to_file(usernames, filename)
    
    # Display the generated usernames
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

if __name__ == "__main__":
    main()
