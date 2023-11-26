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
