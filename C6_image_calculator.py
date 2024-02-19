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


# Main code goes here
# Put function into a variable then print variable
image_ans = image_calc()
print(image_ans)
