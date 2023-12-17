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


def question_TF(list_of_words: list):
    """
    Given a list of words, it'll return the TF score of an entered list
    :param list_of_words: liste of strings
    :return: List of Integers
    """

    question_TF_scores = {}  # Overall same steps as the TF function in tf_idf_related

    for word in list_of_words:
        if word in question_TF_scores:
            question_TF_scores[word] += 1
        else:
            question_TF_scores[word] = 1

    return question_TF_scores


def question_TF_IDF(words_dict_TF: dict):
    """
    Determines the TF-IDF score of each word in a given sentence
    :param words_dict_TF: Dictionary containing the TF scores for all the words in a given list
    :return: Dictionary containing the TF-IDF scores of all those words
    """

    question_dict_TF_IDF = score_IDF  # Keep the same pre-existing IDF scores

    for word in question_dict_TF_IDF.keys():

        if word in words_dict_TF:
            question_dict_TF_IDF[word] = score_IDF[word] * words_dict_TF[word]  # Same IDF times the question's TF
        else:
            question_dict_TF_IDF[word] = 0  # If a word in the folders text files isn't in the question we don't care

    return question_dict_TF_IDF


def TF_IDF_conversion(TF_IDF_dict: dict):
    """
    Converts a TF_IDF score from a dictionary into the form of a 2D array
    :param TF_IDF_dict: Dictionary with strings as keys and integers as values
    :return:
    """

    list_TF_IDF = []  # Empty list

    for word in all_keys:
        list_TF_IDF.append(TF_IDF_dict[word])  # Fill the list with sub-lists making it a 2D array

    return list_TF_IDF

