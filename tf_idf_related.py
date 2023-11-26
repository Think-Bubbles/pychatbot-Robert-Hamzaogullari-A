from math import log10
from extract_files import *


# ---------------------------------------------------Part TF-IDF-------------------------------------------------------#

def sort_by_selection(liste: list):
    """
    Note: en effet, nous n'avons pas vu les algorithmes de tri cette année mais en terminale si, de plus pour mon TP au
    BAC d'NSI on nous a demandé de faire ce tri donc on le maîtrise bien.

    Think of our table as two separate parts : a left side where all the sorted elements are, and a right side where all
    the unsorted elements are. In our first iteration through the list, len(leftside) = 0 and
    len(rightside) = len(liste). We'll start off by saying that the first element of the right side is the smallest
    value, and then we'll compare it to every other element in the right side to see if we find a smaller one.
    We then add it to the left side and restart over again but this time the size of our search is diminished because
    we'll start from liste[1] till len(rightside)


    """

    for element in range(len(liste) - 1):  # We don't need to go till the end because the last unsorted element is the
        # biggest
        smallest_position = element  # Set the position of the smallest_value as the first element on the right side
        for other_element_position in range(element + 1, len(liste)):  # We can start at +1 because we don't need to
            # compare "other_element_position" to itself
            if liste[other_element_position] < liste[smallest_position]:  # We found a new smallest element
                smallest_position = other_element_position  # Remember its position

        if smallest_position != element:  # If the position of the smallest value is different from what he first had
            liste[element], liste[smallest_position] = liste[smallest_position], liste[element]  # Swap the elements.

    return liste


def list_words(directory: str):
    """
    This entire function could be done in one line in IDF_process, but we'd rather detail what we are doing here
    Creates a 1D Array containing every word throughout all the files, no reoccurrences. and unordered
    :param directory: String containing the path to the folder
    :return: List with strings corresponding to every word throughout the files
    """

    list_all_words = []
    list_of_file_names = list_of_files(directory, "txt")

    for file in list_of_file_names:  # Repeat for every file in the folder
        speech = open(directory + file, "r", encoding='utf-8')
        lines = speech.readlines()

        for line in lines:
            words = line.split()

            for word in words:
                if word not in list_all_words:  # If the word isn't already in the list, add it
                    list_all_words.append(word)
        speech.close()

    list_all_words = sort_by_selection(list_all_words)
    return list_all_words


def process_TF(filename: str) -> dict:
    """
    Puts every word of a text (without any reoccurrences) and counts the amount of times it appears.
    :param filename: String -> the name of the file
    :return: Dictionary containing every word and how many times it appeared
    """

    word_frequency = {}
    speech = open("./cleaned/" + filename, "r", encoding="utf-8")
    lines = speech.readlines()

    for line in lines:  # Iterate through every line
        words_in_line = line.split()  # .split() splits the line (string) into a list with all the words as elements

        for word in words_in_line:  # Iterate through every word in the line

            if word in word_frequency:  # If the word was already in our dictionary, add 1 to the word's counter
                word_frequency[word] += 1

            else:  # In this case the word hasn't been seen before
                word_frequency[word] = 1  # Set the word's counter to 1

        speech.close()  # Always good practice to close a file once we are done with it

    return word_frequency


def process_TF_by_president(list_file_names, president: str):
    # list_every_file_names = list_of_files(directory, "txt")
    concerned_file_names = []
    for file_name in list_file_names:
        if president in file_name:
            concerned_file_names.append(file_name)

    total_speeches = process_TF(concerned_file_names[0])    # Clone the first speech's TF dictionary

    if len(concerned_file_names) > 1:   # If the President gave more than 1 speech we need to combine all the TF scores

        for file in concerned_file_names[1:]:   # We already added his first speech so no need to add it again
            tf_file = process_TF(file)

            for key in tf_file:
                if key in total_speeches:   # If he's already said the word in any of his speeches so far, add the score
                    total_speeches[key] += tf_file[key]
                else:   # If it's a new word then insert it into the dictionary
                    total_speeches[key] = tf_file[key]

    return total_speeches


def process_IDF(directory: str):
    """
    Creates a dictionary containing every word throughout every file in a folder and calculates the word's importance
    :param directory: Path of the folder
    :return: Dictionary containing every word and its IDF score
    """

    file_name = list_of_files(directory, "txt")  # Create a list containing the name of every file.
    number_of_documents = len(file_name)  # Obtain the total amount of documents.
    appearance_frequency = {}  # Dictionary that counts the amount of documents a word appears in

    for word in list_words(directory):
        appearance_frequency[word] = 0

    for name in file_name:
        # This second loop will then count the amount of documents each word appears in.

        speech = open(directory + name, "r", encoding="utf-8")
        lines = speech.readlines()
        found_twice = []  # used to check if we've found a word already in a file or not

        for line in lines:
            words = line.split()

            for word in words:
                if word not in found_twice:  # if the word hasn't been seen in the file yet
                    found_twice.append(word)

                    if word not in appearance_frequency.keys():  # If we've never seen the word before
                        appearance_frequency[word] = 1
                    else:  # If we've already seen it in another file
                        appearance_frequency[word] += 1

        speech.close()

    IDF = {}
    for key in appearance_frequency.keys():
        # This final  loop just calculates the IDF value, in other words: the word's significance.

        IDF[key] = log10((number_of_documents / appearance_frequency[key]) + 1)
    return IDF


def process_TF_IDF(directory: str):
    """
    Creates a dictionary containing the words as keys and a lists as values, each list contains the TF-IDF score
    for every document
    :param directory: Path to the folder containing all the text files
    :return: Dictionary containing the words and all of their TF-IDF scores.
    """

    list_file_names = list_of_files(directory, "txt")
    score_IDF = process_IDF(directory)

    all_keys = (list_words(directory))  # Add every word into a list and then sort the list
    dict_TF_IDF = {key: [] for key in all_keys}
    # We can then take all the words in all_keys and add them as keys in our new dictionary
    # We'll set all of their values as an empty list,

    for key in dict_TF_IDF.keys():

        for file in list_file_names:

            score_TF = process_TF(file)

            if key not in score_TF.keys():
                final_value = 0
            else:
                final_value = score_TF[key] * score_IDF[key]
            dict_TF_IDF[key].append(final_value)

    return dict_TF_IDF


def process_TF_IDF_conversion(directory: str):
    """
    Since we initially made our TF-IDF score using a dictionary, we decided to make a function that would convert it
    into a 2D array like we were originally supposed to.
    :param directory:
    :return: 2D array, each line is a word and the columns are it's TF-IDF score for every file
    """

    list_file_names = list_of_files(directory, "txt")
    score_IDF = process_IDF(directory)
    all_keys = sort_by_selection(list_words(directory))
    final = process_TF_IDF(directory)
    list_TF_IDF = []

    for word in all_keys:
        list_TF_IDF.append(final[word])

    return list_TF_IDF


def process_final_2DArray(directory: str):
    """
    We also just wanted to show that we were capable of making it with a 2D array from the start.
    :param directory:
    :return:
    """

    list_file_names = list_of_files(directory, "txt")
    score_IDF = process_IDF(directory)
    all_keys = sort_by_selection(list_words(directory))
    list_TF_IDF = []

    for i in range(len(all_keys)):

        temp = []
        for file in list_file_names:

            score_TF = process_TF(file)

            if all_keys[i] not in score_TF.keys():
                final_value = 0
            else:
                final_value = score_TF[all_keys[i]] * score_IDF[all_keys[i]]
            temp.append(final_value)
        list_TF_IDF.append(temp)

    return list_TF_IDF
