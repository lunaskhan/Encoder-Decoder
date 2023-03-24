def encode(password):
    encoded = ''
    for i in password:
        c = (int(i) + 3) % 10
        encoded += str(c)
    return encoded


def decode(password):
    decoded = ''
    for i in password:
        c = (int(i) - 3) % 10
        decoded += str(c)
    return decoded


def main():
    password = ''
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        op = input('Please enter an option: ')
        if op == '1':
            password = encode(input("Enter your password to encode: "))
            print('Your password has been encoded and stored!')
        elif op == '2':

            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
        elif op == '3':
            exit()


if __name__ == '__main__':
    main()