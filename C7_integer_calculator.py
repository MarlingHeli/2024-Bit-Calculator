# ask user for width and loop until they enter a number > 0

def int_check(question, low):
    error = f"Please enter a number more than or equal to {low}\n"
    while True:
        try:
            response = int(input(question))

            if response >= low:
                return response  # ends loop
            else:
                print(error)

        except ValueError:  # prevents string input
            print(error)


# calculates how many bits are needed to represent an integer
def integer_calc():
    # ask the user to enter an integer >= 0
    integer = int_check("Integer: ", 0)

    # convert integer to binary and find bits needed to represent the integer
    raw_binary = bin(integer)

    binary = raw_binary[2:]  # exclude the first 2 characters (0b)
    num_bits = len(binary)

    # set up answer and return it
    # Put f string in brackets if there are multiple f strings
    answer = f"{integer} in binary is {binary}. We need {num_bits} bits to represent it."

    return answer


# Main code goes here
# Put function into a variable then print variable
integer_ans = integer_calc()
print(integer_ans)
