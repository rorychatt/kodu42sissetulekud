def print_positive_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        number = float(lines[i].strip())
        if number > 0:
            print(number)

file_path = 'konto.txt'
print_positive_numbers_from_file(file_path)
