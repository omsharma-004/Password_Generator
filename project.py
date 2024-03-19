import random

def generate_password(length):
    if length < 12:
        print("Minimum password length is 12.")
        return None

    DIGITS = '0123456789'
    LOCASE_CHARACTERS = 'abcdefghijklmnopqrstuvwxyz'
    UPCASE_CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SYMBOLS = '@#$%=:?.|~*()'

    combined_list = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for _ in range(length - 4):
        temp_pass += random.choice(combined_list)

    password = ''.join(random.sample(temp_pass, len(temp_pass)))
    return password

def main():
    length = int(input("Enter length of Password: "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
    print("\n****************************************************")
    print("        Thank You For Using Our Application")
    print("                Please Visit Again")
    print("****************************************************\n")

if __name__ == "__main__":
    main()
