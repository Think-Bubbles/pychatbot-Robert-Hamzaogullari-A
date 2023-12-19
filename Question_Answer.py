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

score_idf = tf_idf_related.score_IDF
score_TF_IDF_Array = tf_idf_related.calcul_TF_IDF_matrix(cleaned_path, extract_files.list_of_all_file_names)
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

    question_dict_TF_IDF = score_idf  # Keep the same pre-existing IDF scores

    for word in question_dict_TF_IDF.keys():

        if word in words_dict_TF:
            question_dict_TF_IDF[word] = score_idf[word] * words_dict_TF[word]  # Same IDF times the question's TF
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


def vector_norm(vector: list):
    """
    Determines the norm of a vector, meaning that it squares and sums every value in the vector and then square roots it
    :param: vector:
    :return:
    """

    norm = 0
    for item in vector:
        norm += item ** 2  # Sum the squares of every value in the vector
    norm = math.sqrt(norm)  # Square root the obtained sum
    return norm


def vector_dot_product(vector1: list, vector2: list):
    """
    Sums the multiplication of two different vectors and returns the value
    :param vector1:
    :param vector2:
    :return: Dot product of two vectors
    """

    dot_product = 0
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]
    return dot_product


def similarity_calculation(vector1: list, vector2: list):
    """
    Based off of the cosine similarity, it determines the similarity between two different vectors of the same dimension
    :param vector1:
    :param vector2:
    :return:
    """
    finalscore = vector_dot_product(vector1, vector2) / (vector_norm(vector1) * vector_norm(vector2))
    return finalscore


def most_relevant_document(question_tf_idf, folder_tf_idf, list_files):
    """
    Given two sets of TF-IDF scores, it'll compare every Folder's TF-IDF score to the question's TF-IDF and determine
    the most resembling folder
    :param question_tf_idf: TF_IDF score of the question
    :param folder_tf_idf: TF_IDF score of the main folder without considering the question
    :param list_files: List of all the files in the folder we're working with
    :return: Name of the most similar file
    """

    mostRelevantDocument = 0
    temp = 0

    for i in range(len(list_files)):

        temp_array = []
        for j in range(len(folder_tf_idf)):
            temp_array.append(folder_tf_idf[j][i])

        if similarity_calculation(question_tf_idf, temp_array) > temp:  # If we find a new and more similar document
            temp = similarity_calculation(question_tf_idf, temp_array)
            mostRelevantDocument = list_files[i]  # Remember the name of file

    return mostRelevantDocument


def highest_tf_idf(scores):
    """
    Given a set of different TF-IDF scores, this will return the one with the highest score
    :param scores:  Can be either a dictionary with integers as values or a 2D array
    :return: Str the word with the highest score
    """

    if type(scores) is dict:
        highest_tf_idf_word = 0  # Stocks the highest TF-IDF value
        for key in scores.keys():
            if type(scores[key]) is list:  # If the dictionary has 1D arrays
                total = 0
                for value in scores[key]:  # Sum all the elements in the list
                    total += value
            else:  # If not then it's just an integer
                total = scores[key]
            if total > highest_tf_idf_word:  # If we find a new highest value
                highest_tf_idf_word = scores[key]  # Keep track of the value
                word = key  # Keep track of the word
        return word

    elif type(scores) is list:
        highest_tf_idf_word = 0
        line = 0
        for line in range(len(scores)):
            total = 0
            for column in range(line):
                total += scores[line][column]
                if total > highest_tf_idf_word:  # We've found a new highest TF-IDF score
                    highest_tf_idf_word = total
                    index = line  # Since we've previously sorted all the words in the folder we can easily track
                    # which word the value corresponds to
        return all_keys[line]


def response_generation(file_name: str, important_word: str, quest: str):
    """
    Based off of the most important word in a given sentence, you will get an answer from the most similar document
    This response is very basic and not yet refined - only the rest of the sentence after the most important word.
    :param quest: Str sentence that the user enters
    :param file_name: Str name of the file the most resembles the sentence
    :param important_word: Float word that has the highest TF-IDF score in the sentence
    :return: Str the sentence in the document after the word has been spotted for the first time
    """

    question_starters = {"comment": "Après analyse, ", "pourquoi": "Car", "peux-tu": "Oui, bien sûr!",
                         "quand": "Lors de l'événement, ", "où": "Dans cette région, "}
    question = quest.lower().split()  # When we enter a question, it now doesn't matter if it's in lower or uppercase

    file = open(path + file_name, "r", encoding='utf-8')
    lines = file.read()
    sentences = lines.split(".")  # Splits the document up sentence by sentence making the process much easier

    final_answer = ""
    for debuts in question_starters.keys():
        if debuts == question[0]:  # If the beginning of the question is the same as the key
            final_answer = question_starters[debuts] + " "  # Add a space for the next part
            break

    for sentence in sentences:
        if important_word in sentence:  # If we find the word we're looking for
            words_in_sentence = sentence.split()  # Split up the sentence into words
            words_in_sentence[0] = words_in_sentence[0].lower()  # Incase the original sentence starts with an uppercase
            for word in range(len(words_in_sentence) - 1):  # -1 to check the next word.
                final_answer += words_in_sentence[word]
                if words_in_sentence[word + 1] not in [",", ";", ":", "%",
                                                       " £"]:  # Don't want to add unnecessary spaces
                    final_answer += " "
            final_answer += words_in_sentence[-1] + "."  # Add a full stop at the end to end the sentence correctly
            break
    return final_answer
