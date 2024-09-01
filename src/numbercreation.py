def sum_of_digits(num):
    total = sum(int(digit) for digit in str(num))
    while total >= 10:
        total = sum(int(digit) for digit in str(total))
    return total

def categorize_lucky_pattern(num_str):
    # Ensure the number is treated as a four-digit string
    if len(num_str) < 4:
        num_str = num_str.zfill(4)
    
    # Check for ABAB pattern
    if num_str[0] == num_str[2] and num_str[1] == num_str[3] and num_str[0] != num_str[1]:
        return "ABAB"
    # Check for ABBA pattern
    if num_str[0] == num_str[3] and num_str[1] == num_str[2] and num_str[0] != num_str[1]:
        return "ABBA"
    # Check for AAAB pattern
    if num_str[0] == num_str[1] == num_str[2] and num_str[0] != num_str[3]:
        return "AAAB"
    # Check for ABBB pattern
    if num_str[0] != num_str[1] == num_str[2] == num_str[3]:
        return "ABBB"
    # Check for AAAA pattern
    if num_str[0] == num_str[1] == num_str[2] == num_str[3]:
        return "AAAA"
    # Check for AABA pattern
    if num_str[0] == num_str[1] and num_str[2] != num_str[0] and num_str[2] == num_str[3]:
        return "AABA"
    # Check for ABAA pattern
    if num_str[0] == num_str[2] and num_str[1] == num_str[3] and num_str[0] != num_str[1]:
        return "ABAA"
    # Check for AABB pattern
    if num_str[0] == num_str[1] and num_str[2] == num_str[3] and num_str[0] != num_str[2]:
        return "AABB"
    return None

def is_series(num_str):
    # Ensure the number is treated as a four-digit string
    if len(num_str) < 4:
        num_str = num_str.zfill(4)
    
    # Check if the number is a series
    if all((int(num_str[i]) + 1) % 10 == int(num_str[i + 1]) for i in range(len(num_str)-1)):
        return True
    if all((int(num_str[i:i+2]) + 1) % 100 == int(num_str[i+2:i+4]) for i in range(0, len(num_str)-2, 2)):
        return True
    return False

def find_numbers(start, end, target_sum=None, check_lucky=True):
    all_numbers = []
    fancy_numbers = {
        "ABAB": [],
        "ABBA": [],
        "AAAB": [],
        "ABBB": [],
        "AAAA": [],
        "AABA": [],
        "ABAA": [],
        "AABB": [],
        "Series": []
    }
    
    for num in range(start, end + 1):
        if target_sum is not None and sum_of_digits(num) == target_sum:
            all_numbers.append(num)
            if check_lucky:
                num_str = str(num)
                pattern = categorize_lucky_pattern(num_str)
                if pattern:
                    fancy_numbers[pattern].append(num)
        if check_lucky:
            num_str = str(num)
            if is_series(num_str):
                fancy_numbers["Series"].append(num)
            pattern = categorize_lucky_pattern(num_str)
            if pattern:
                fancy_numbers[pattern].append(num)
    
    return all_numbers, fancy_numbers

def save_to_file(filename, all_numbers, fancy_numbers):
    def format_numbers(numbers):
        return '\n'.join(', '.join(map(str, numbers[i:i+20])) for i in range(0, len(numbers), 20))

    with open(filename, 'w') as file:
        if all_numbers:
            file.write("All numbers that sum to the target:\n\n")
            file.write(format_numbers(all_numbers) + '\n\n')

        file.write("Fancy numbers:\n\n")
        for pattern, numbers in fancy_numbers.items():
            if numbers:
                file.write(f"\n{pattern} pattern: \n")
                for i in range(0, len(numbers), 10):
                    file.write(format_numbers(numbers[i:i+10]) + '\n')

def numbercreation(start=1,end=9999,target_sum=None,check_lucky=True):
    filename = 'output/lucky_numbers.txt'

    # Find all numbers within the range and with the target sum
    all_numbers, fancy_numbers = find_numbers(start, end, target_sum, check_lucky)

    # Print the results
    if target_sum is not None:
        print("All numbers that sum to the target:")
        print(all_numbers)

    print("\nFancy numbers:")
    for pattern, numbers in fancy_numbers.items():
        print(f"{pattern} pattern: {numbers}")

    # Save the results to a text file
    save_to_file(filename, all_numbers, fancy_numbers)
    print(f"\nResults saved to {filename}")
