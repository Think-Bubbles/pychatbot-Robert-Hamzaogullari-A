"""                                         Nom du projet : Chatbot EFREI L1
                                     Auteurs : William ROBERT | Batur HAMZAOGULLARI

This function responds to all of the demands in the second part of the project. It starts off by taking in a question
and transforming it into a standardised format akin to the treatment the text files underwent. It then builds off of
that question to make a TF-IDF score out of it along with the text files. It then uses this to determine the most
important word in the question, the best corresponding file all in order to create an answer to the original question.
"""
# ______________________________________________Functions from part 2__________________________________________________#

import math
import extract_files
import tf_idf_related
import text_treatment

path = "./speeches/"
cleaned_path = "./cleaned/"
files = extract_files.list_of_files(cleaned_path, ".txt")
score_IDF = tf_idf_related.score_IDF
score_TF_IDF_Array = tf_idf_related.process_final_2DArray(cleaned_path)
all_keys = tf_idf_related.list_words(cleaned_path)


def tokenise_question(question: str) -> list:
    """
    Takes in a string entered by the user and returns a tokenized version of it, meaning that each word is a list and
    the question has been filtered
    :param question: Str
    :return: List containing every word
    """

    tokenized_question = text_treatment.cleaned_text(question).split()  # Clean the text and make a list of every word
    return tokenized_question


def search_related_words(list_of_words: list) -> list:
    """
    Takes the words of a question and checks to see which of those words also exist in the documents
    :param list_of_words: List of strings
    :return: List of strings corresponding to all the words in question that were also in the documents
    """
    related_words = []
    every_word = tf_idf_related.list_words(cleaned_path)
    for word in list_of_words:

        if word in every_word:  # If a word in the given list was said at least once in the overall list of words
            related_words.append(word)
    return related_words
