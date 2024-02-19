# ask user for width and loop until they enter a number > 0

def int_check(question, low):
    error = f"Please enter a number more than or equal to {low}\n"
    while True:
        try:
            response = int(input(question))

            if response >= low:
                return response #ends loop
            else:
                print(error)

        except ValueError:  # prevents string input
            print(error)


# Main routine here
for item in range(0, 2):
    integer = int_check("Integer: ", 1)
    print(integer)

print()

for item in range(0, 2):
    width = int_check("Width: ", 1)
    print(width)

print()

for item in range(0, 2):
    height = int_check("Height: ", 1)
    print(height)

