

def main():
    min_length = 6
    password = get_password(min_length)
    for char in password:
        print("*", end="")

def get_password(min_length):
    chars = str(input("Enter your password: "))
    while len(chars) < min_length:
        print("Please enter a password of at least {} digits!".format(min_length))
        chars = str(input("Enter your password: "))
    return chars

main()



