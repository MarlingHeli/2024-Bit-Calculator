#asks users for file type (integer/image/text/xxx)
def get_filetype():
    while True:
        response = input("File type: ").lower()

        #check for i or the exit code
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


#main routine goes here
while True:
    file_type = get_filetype()

    if file_type == "i":
        want_image = input("Press <enter> for an integer for any key for an image. ")

        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}")

    if file_type == "xxx":
        break
