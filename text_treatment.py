

# _____________________________________________Programs that clean speeches____________________________________________#


def president_last_name(files: list) -> list:
    """
    Extracts only the president name from the name of a folder
    :param files: List of strings containing the full name of a file
    :return: New liste containing the name of every president without any reoccurrences
    """

    extracted_names = []
    for name in files:  # Browse through every file name

        if name[-5].isdigit():  # If the president gives multiple speeches, then remove the number at the end
            # .isdigit() is used to observe whether the element is a digit or a character.

            if name[11:-5] not in extracted_names:  # If his name has not already been saved in the list:
                extracted_names.append(name[11:-5])  # -5 to remove the number
        else:
            extracted_names.append(name[11:-4])  # In this case, there is no number to remove, only '.txt'

    return extracted_names


def president_first_name() -> dict:
    """
    Assigns a first name to every last name given in the list.
    :return: Dictionary containing last names as keys and first names as values
    """

    dictionary_names = {}  # Dictionary where the keys are the last names and the values are the first names

    file_names = open("nom_prenom", "r", encoding='utf-8')  # Text file containing every first and last name
    lines = file_names.readlines()  # .readlines() turns the text file into a list

    for i in range(0, len(lines), 3):  # Increment by three to skip the line that doesn't include anything
        dictionary_names[lines[i][5:-1]] = lines[i + 1][8:-1]  # Remove any unnecessary letter

    return dictionary_names


def president_full_name(dico: dict):
    """
    Prints the full name of every president
    :param dico: List of strings containing the full name of every president.
    :return: Prints out every string in the list
    """

    for name in dico:
        value = dico[name]
        print("Nom: ", name, ", Prénom: ", value)


def cleaned_speech(list_speeches):
    """
    Re-writes every speech in a new folder but removes special characters and turns everything into lowercase
    :param list_speeches: List of strings containing the file name of every speech
    :return: Nothing
    """

    special_characters_remove = [".", ",", "!", "?", ":", ";", "`", "\""]  # Every possible special characters to remove

    for file_name in list_speeches:  # Name of every file in the speeches folder

        lowercase_file = open("./cleaned/" + file_name, "w", encoding='utf-8')  # Create a new file with the same name-
        # in the cleaned folder
        normal_file = open("./speeches/" + file_name, "r", encoding='utf-8')  # Open the corresponding speech
        lines = normal_file.readlines()  # Create a list containing every line in the speech

        for line in lines:  # Iterate through every line in the speech
            lowercase_line = line.lower()  # .lower() turns every letter into its lowercase counterpart
            temp = ""  # New string

            for letter in lowercase_line:  # Iterate through each letter on this line
                if letter not in special_characters_remove:  # If it isn't any of the specified special characters
                    if letter == "'" or letter == "-":  # Check if we need to remove the character by a space or not
                        temp += " "  # Add a space instead
                    else:
                        temp += letter  # Add the letter
                # Since we've created a new empty string 'Temp', if it is a special character we don't do anything

            lowercase_file.write(temp)  # Write the newly modified line into our cleaned speech file

        lowercase_file.close()  # Close the cleaned file
        normal_file.close()  # Close the unmodified speech.

def cleaned_text(text):
    """
    Instead of taking in a directory, this function only needs text
    :param text: Str the text that you want filtered
    :return: Str after being "standardized
    """

    special_characters_remove = [".", ",", "!", "?", ":", ";", "`", "\""]  # Every possible special character to remove

    temp = ""  # New string
    lowercase_text = text.lower()  # .lower() turns every letter into its lowercase counterpart

    for letter in lowercase_text:  # Iterate through each letter on this line
        if letter not in special_characters_remove:  # If it isn't any of the specified special characters
            if letter == "'" or letter == "-":  # Check if we need to remove the character by a space or not
                temp += " "  # Add a space instead
            else:
                temp += letter  # Add the letter
        # Since we've created a new empty string 'Temp', if it is a special character we don't do anything

    return temp