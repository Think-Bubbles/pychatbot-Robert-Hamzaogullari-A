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

#------------------------------------------------Programme Principale--------------------------------------------------#

directory = ".\speeches"
file_names = list_of_files(directory, "txt")

print(liste_nom_president(file_names))