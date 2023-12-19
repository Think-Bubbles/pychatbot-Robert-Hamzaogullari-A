"""                                         Nom du projet : Chatbot EFREI L1
                                     Auteurs : William ROBERT | Batur HAMZAOGULLARI

We've decided to put this function into its own separate file in order to avoid circular importation issues.
"""
import os


def list_of_files(directory, extension):
    """
    Sorts all every file name into a list
    :param directory: String Folder containing all the files
    :param extension: String the type of file you are looking for
    :return: List with every file name including the extension
    """

    file_names = []

    for filename in os.listdir(directory):  # Creates a list containing every file name in 'directory'
        if filename.endswith(extension):
            file_names.append(filename)
    return file_names


list_of_all_file_names = list_of_files("./cleaned/", ".txt")
number_of_files = len(list_of_all_file_names)
