def calculate_positive_negative_ratio(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip().split(',')
    state_index = header.index('state')
    positive_index = header.index('positive')
    negative_index = header.index('negative')

    state_ratios = {}

    for line in lines[1:]:
        columns = line.strip().split(',')
        state = columns[state_index]
        positive = columns[positive_index]
        negative = columns[negative_index]

        if positive.isdigit() and negative.isdigit():
            positive = int(positive)
            negative = int(negative)
            if negative > 0:  # Avoid division by zero
                ratio = positive / negative
                state_ratios[state] = ratio

    with open(output_file, 'w') as file:
        file.write('state,positive_negative_ratio\n')
        for state, ratio in state_ratios.items():
            file.write(f'{state},{ratio:.2f}\n')

# Example usage
file_path = "/Users/tawfiqabulail/Downloads/Information Infrastructure I /covid_data_set.csv"
calculate_positive_negative_ratio(file_path, 'positive_negative_ratios.csv')