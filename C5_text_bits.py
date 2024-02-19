# Calculate number of bits needed to represent text in asccii

def calc_text_bits():

    # Get text from user
    response = input("Enter text: ")

    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it."
              f"\nwhich is {num_bits} bits.")

    return answer


# Main routine goes here
text_ans = calc_text_bits()
print(text_ans)
