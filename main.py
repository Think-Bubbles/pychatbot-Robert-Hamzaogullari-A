# Chatbot EFREI L1
# William ROBERT | Batur HAMZAOGULLARI

from extract_files import *
import text_treatment

#---------------------------------------------------Partie TF-IDF------------------------------------------------------#

def TF_process(filename: str) -> dict:
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
