def main():
    print('Select any one of following')
    print('1. Write a new file')
    print('2. Write an existing file')
    print('3. Read an existing file')

    choice = int(input('Enter your choice'))
    mode = 'w' if choice == 1 else 'a' if choice == 2 else 'r'
    print(mode);

    file_name = input('Enter a file name')
    if mode != 'r':
        file_data = input('Enter a file data')
    try:
        file = open(file_name, mode)
        if mode != 'r':
            file.write(file_data)
        else:
            print(file.read())
    except IOError:
        print('File not found')


if __name__ == '__main__':
    main()
