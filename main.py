def read_and_filter_positive_numbers(file_path):
    positive_numbers = [] 

    with open(file_path, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                if number > 0:
                    positive_numbers.append(number)
            except ValueError:
                continue

    return positive_numbers

file_path = 'konto.txt'
positive_numbers = read_and_filter_positive_numbers(file_path)

for number in positive_numbers:
    print(number)
