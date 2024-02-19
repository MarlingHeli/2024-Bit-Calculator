# generates headings

def statement_generator(statement, decoration):  # prints statement with fancy decoration
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator("Instructions", "_")

    print("""Enter what your file type is.
It will tell you the bits required for your file type.   
    """)


# asks users for file type (integer/image/text/xxx)
def get_filetype():
    while True:
        response = input("File type: ").lower()

        # check for i or the exit code
        if response == "xxx" or response == "i":
            return response

        # find if response in in list
        elif response in ["integer", "int"]:
            return "integer"

        elif response in ["image", "picture", "img"]:
            return "image"

        elif response in ["text", "txt", "t"]:
            return "text"

        else:
            print("Please enter a valid file type")

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
def image_calc():
    # get image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    # calculate no. of pixels and multiply by 24 to get no. of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it
    # Put f string in brackets if there are multiple f strings
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer

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


# main routine goes here
want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    if file_type == "i":
        want_image = input("Press <enter> for an integer for any key for an image. ")

        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        # Put function into a variable then print variable
        image_ans = image_calc()
        print(image_ans)

    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)

    else: #if it's not int or image, it's text.
        text_ans = calc_text_bits()
        print(text_ans)

    print()
