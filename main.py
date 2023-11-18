# Chatbot EFREI L1
# William ROBERT | Batur HAMZAOGULLARI

import os
import math

def list_of_files(directory, extension):

    file_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_names.append(filename)
    return file_names


def liste_nom_president(files : list) -> list:
    """
    écrit dans une nouvelle liste le nom de tous les présidents.
    :param files: Liste des strings contenant les noms des fichiers
    :return: Nouvelle liste contenant le nom de chaque président SANS DOUBLONS.
    """

    extracted_names = []
    for name in files:

        if name[-5].isdigit():      # If presidents give several speeches, remove the number at the end.
            # .isdigit() is used to observe whether the element is a digit or a character.
            if name[11:-5] not in extracted_names:      # If his name has not already been saved in the list:
                extracted_names.append(name[11:-5])     # we add it to the list
        else:
            extracted_names.append(name[11:-4])         # In this case, there is no number to remove.

    return extracted_names

def extract_full_name() -> dict:
    """
    assigns a first name to every last name given in the list.
    :return: Nothing
    """
    dictionary_names = {}   # Dictionary where the keys are the last names and the values are the full names

    file_names = open("nom_prenom", "r", encoding='utf-8')  # Open the text file with every last name and first name
    liste = file_names.readlines()

    for i in range(0, len(liste), 3):   # We step by 3 to gather the last name(line1) the first name(line2) and skip-
                                        # -the empty line
        dictionary_names[liste[i][5:-1]] = liste[i+1][8:-1] # The slices here allow use to remove any unnecessary text

    return dictionary_names

def afficher_noms(dico : dict):
    """
    PRINTS the last name of every president that gave a speech once
    :param dico: List of strings containing the last name of every president.
    :return: Prints out every string in the list
    """

    for name in dico:
        value = dico[name]
        print("Nom: ", name, ", Prénom: ", value)

def cleaned_speech(list_speeches):
    """
    re-writes every speech in a new folder but everything is in lowercase
    :param list_speeches: List of strings containing the file name of every speech
    :return: Nothing
    """

    special_characters_remove = ["-", ".", ",", "!", "?", "\""]  # List of all the possible special characters to remove
    for file_name in list_speeches: # Name of every file in the speeches folder

        lowercase_file = open("./cleaned/" + file_name, "w", encoding='utf-8')  # Create a nex file with the same name-
        # in the cleaned folder
        normal_file = open("./speeches/" + file_name, "r", encoding='utf-8')    # Open the corresponding speech
        lines = normal_file.readlines()  # Create a list containing every line in the speech

        for line in lines:  # Iterate through every line in the speech
            lowercase_line = line.lower()   # .lower() turns every letter into its lowercase counterpart

            temp = ""
            for letter in lowercase_line:   # Iterate through each letter on this line
                if letter not in special_characters_remove:     # If it isn't any of the specified special characters
                    if letter == "\'" or letter == "-":
                        temp += " "  # Add a space instead
                    else:
                        temp += letter  # Remove it entirely

            lowercase_file.write(temp)  # Write the newly modified line into our cleaned speech file

        lowercase_file.close()  # Close the cleaned file
        normal_file.close()     # Close the unmodified speech.
        
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
#------------------------------------------------Programme Principale--------------------------------------------------#

directory = ".\speeches"
file_names = list_of_files(directory, "txt")
