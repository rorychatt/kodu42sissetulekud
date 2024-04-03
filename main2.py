def print_positive_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        try:
            number = float(lines[i].strip())
            if number > 0:
                print(number)
        except ValueError:
            continue

file_path = 'konto.txt'

print_positive_numbers_from_file(file_path)
