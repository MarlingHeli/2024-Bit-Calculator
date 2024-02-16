#generates headings

def statement_generator(statement, decoration): #prints statement with fancy decoration
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

#displays instructions
def instructions():
    statement_generator("Instructions", "_")

    print("""
How to open a door
1. Wrap your hand around the door handle
2. Pull the door towards you
3. Walk through the gap you just created
4. Enter the McDonalds facility
5. Buy chicken nuggets    
    """)

#main routine goes here
want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")