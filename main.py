PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    name = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for i in name:
        stripped_name = i.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as new_file:
            new_file.write(new_letter)