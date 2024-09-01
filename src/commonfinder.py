def read_numbers_from_file(file_path):
    """Reads numbers from a file and returns a set of numbers."""
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file if line.strip().isdigit())

def read_patterns_from_file(file_path):
    """Reads patterns from a file and returns a dictionary of pattern names and their numbers."""
    patterns = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_pattern = None
        
        for line in lines:
            line = line.strip()
            if line.endswith('pattern:'):
                current_pattern = line[:-8].strip()
                patterns[current_pattern] = set()
            elif line.endswith('target:'):
                current_pattern = line[:-1].strip()
                patterns[current_pattern] = set()
            elif current_pattern and line:
                # Parse numbers from the line and add to the current pattern set
                numbers = line.split(',')
                patterns[current_pattern].update(number.strip() for number in numbers if number.strip().isdigit())
    
    return patterns

def find_common_numbers(numbers_set, patterns_dict):
    """Finds common numbers between the set of numbers and each pattern set."""
    common_numbers = {}
    
    for pattern_name, pattern_numbers in patterns_dict.items():
        common = numbers_set.intersection(pattern_numbers)
        if common:
            common_numbers[pattern_name] = sorted(common)
    
    return common_numbers

def write_common_numbers_to_file(file_path, common_numbers):
    """Writes the common numbers in the specified format to a file."""
    with open(file_path, 'w') as file:
        file.write('Fancy numbers:\n\n')
        for pattern_name in ['All numbers that sum to the target','ABAB', 'ABBA', 'AAAB', 'ABBB', 'AAAA', 'AABA', 'Series']:
            if pattern_name in common_numbers:
                numbers = ', '.join(common_numbers[pattern_name])
                file.write(f'{pattern_name} pattern: {numbers}\n')
            else:
                file.write(f'{pattern_name} pattern:\n')

def extract_last_four_digits(file_path):
    """Extracts the last four digits from each registration number in the file."""
    with open(file_path, 'r') as file:
        return {line.strip()[-4:] for line in file if len(line.strip()) >= 4}

def remove_matching_numbers(numbers_set,regnumberset):
    """Removes matching numbers from the number set."""
    # Remove matching numbers
    numbers_set -= regnumberset
    return numbers_set

def commmonfinder():
    # File paths
    numbers_file = 'output/numbers.txt'
    patterns_file = 'output/lucky_numbers.txt'
    output_file = 'OutputNumbers.txt'
    regnumbers_file = 'output/regnumbers.txt'
    
    # Read the numbers and patterns
    numbers_set = read_numbers_from_file(numbers_file)
    # print(f"\nnumberset :\n {numbers_set}")
    patterns_dict = read_patterns_from_file(patterns_file)
    # print(f"\npatternset :\n {patterns_dict}")
    # Extract last four digits from registration numbers
    regnumberset = extract_last_four_digits(regnumbers_file)
    # print(f"\nregnumberset :\n {regnumberset}")
    # Find common numbers
    common_numbers = find_common_numbers(numbers_set, patterns_dict)
    
    # Write the results to the output file
    write_common_numbers_to_file(output_file, common_numbers)
    
    print(f"Common numbers have been written to {output_file}.")
    # Remove matching numbers from output file
    updated_number_set = remove_matching_numbers(numbers_set,regnumberset)
    # Find common numbers
    updated_common_numbers = find_common_numbers(updated_number_set, patterns_dict)
    # Write the results to the output file
    write_common_numbers_to_file("updated"+output_file, updated_common_numbers)
    print(f"Common numbers have been written to Updated{output_file} by removing booked reg numbers.")