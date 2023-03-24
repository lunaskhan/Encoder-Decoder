def encode(password):
    encoded = ''
    for i in password:
        c = (int(i) + 3) % 10
        encoded += str(c)
    return encoded


def main():
    password = input("Enter a password to encode: ")
    print(encode(password))

if __name__ == '__main__':
    main()