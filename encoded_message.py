def read_word_number_dict(file_path):
    """Reads a file and returns a dictionary mapping numbers to words."""
    word_number_dict = {}
    with open(file_path, "r") as file:  # Using context manager for file operations
        for line in file:
            parts = line.split()
            if len(parts) >= 2:  # Validate data format
                number, word = int(parts[0]), parts[1]
                word_number_dict[number] = word
    return word_number_dict

def construct_pyramid_words(word_number_dict):
    """Constructs a list of words based on a pyramid pattern."""
    result = []
    current_index = 1  # Starting index
    step_increase = 2  # Initial step increase
    max_index = max(word_number_dict.keys())  # Get the maximum index to avoid going out of bounds

    if 1 in word_number_dict:  # Check if the starting index is in the dictionary
        result.append(word_number_dict[1])

    while current_index <= max_index:
        current_index += step_increase
        step_increase += 1
        if current_index in word_number_dict:  # Check if the current index is in the dictionary
            result.append(word_number_dict[current_index])

    return result

# Example usage
file_path = "coding_qual_input.txt"
word_number_dict = read_word_number_dict(file_path)
pyramid_words = construct_pyramid_words(word_number_dict)
print(" ".join(pyramid_words))