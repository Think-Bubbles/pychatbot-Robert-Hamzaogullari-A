# Chatbot EFREI L1
# William ROBERT | Batur HAMZAOGULLARI

import os
import math

def list_of_files(directory, extension):
    """
    Sorts all every file name into a list
    :param directory: String Folder containing all the files
    :param extension: String the type of file you are looking for
    :return: List with every file name including the extension
    """

    file_names = []

    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_names.append(filename)
    return file_names

# ___________________________________________Initial Speech related functions__________________________________________#

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

def president_full_name(dico : dict):
    """
    PRINTS the full name of ever president
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

    special_characters_remove = ["-", ".", ",", "!", "?"]  # List of all the possible special characters to remove

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
        
#---------------------------------------------------Partie TF-IDF------------------------------------------------------#

def TF_process(text_file : list):
    """

    :param file_name:
    :return:
    """

    word_frequency = {}

    text = open("./cleaned/" + text_file[0], "r", encoding="utf-8")
    lines = text.readlines()

    for line in lines:
        words_in_line = line.split()

        for word in words_in_line:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    text.close()

    print(word_frequency)

def IDF_process(file_name : list):
    """

    :param file_name:
    :return:
    """

    appearance_frequency = {}   # Dictonary that counts the amount of documents a word appears in

# ---- 1st loop to add all the word to the dictonary

    number_of_documents = len(file_name)    # Obtain the total amount of documents.

    for name in file_name:
        # This for loop's main objective is to add into a dictionary every word in all the documents combined

        speech = open("./cleaned/" + name, "r", encoding="utf-8")
        lines = speech.readlines()

        for line in lines:  # Split up the search into line by line
            words = line.split()

            for word in words:  # Split up the search into word by word
                if word not in appearance_frequency:    # if the word
                    appearance_frequency[word] = 0
        speech.close()

# ---- 2nd loop to calculate their frequency

    for name in file_name:
        # This second for loop will then count the amount of documents each word appears in.

        speech = open("./cleaned/" + name, "r", encoding="utf-8")

        text = speech.read()

        for key in appearance_frequency.keys():
            if key in text:
                appearance_frequency[key] += 1

        speech.close()

# ----  Calcul de score IDF

    IDF = {}
    for key in appearance_frequency.keys():
        # This final for loop just calculates the IDF value.

        IDF[key] = math.log10(number_of_documents / appearance_frequency[key])

    print(IDF)
    
#------------------------------------------------Programme Principale--------------------------------------------------#

directory = ".\speeches"
file_names = list_of_files(directory, "txt")
