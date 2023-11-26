import text_treatment
import tf_idf_related
from extract_files import list_of_files


# ______________________________________________Additional functionalities_____________________________________________#

def request_redundant_words(directory, level):
    """
    Filters all the words who's tf_idf sum is below a determined threshold
    :param directory:
    :param level: Float, serves as the filter, only lets through smaller or equal values
    :return: Str all the words classified as redundant
    """

    print("The least important words are: ", end="")

    for word in range(len(tf_idf_array)):  # Iterate through every single word
        total_score = 0  # Stocks the sum of the words tf_idf score throughout all the files

        for tf_idf_score in range(len(list_of_files(directory, "txt"))):  # Iterate through all the scores
            total_score += tf_idf_array[word][tf_idf_score]

        if total_score <= level:
            print(all_words[word], end=", ")


def request_highest_tf_idf(directory):
    """
    Finds the most important word, meaning the word who has the most important tf_idf score throughout the files
    :param directory:
    :return: Str containing the most "important" word
    """

    list_highest_sums = [0]
    highest_tf_idf = 0

    for word in range(len(tf_idf_array)):  # Iterate through all the words
        total_score_word = 0  # Store the sum of all the tf_idf scores for this word

        for score_tf_idf in range(len(list_of_files(directory, "txt"))):  # Iterate through each of it's tf_idf scores
            total_score_word += tf_idf_array[word][score_tf_idf]

        if total_score_word > highest_tf_idf:  # We've found a new highest sum of tf_idf scores
            list_highest_sums = [all_words[word]]  # Add the word to the list
            highest_tf_idf = total_score_word  # Stock the new highest sum
        elif total_score_word == highest_tf_idf:  # We've found a word with the same total score
            list_highest_sums.append(all_words[word])

    print("The word(s) with the highest TF-IDF score in corpus is/are: ", end="")
    for word in list_highest_sums:
        print(word, end=";")
    print()


def request_most_repeated_word(directory: str, president: str):
    """
    Finds the most repeated word(s) said by any president
    :param directory:
    :param president: Str
    :return: Str
    """

    total_speeches = tf_idf_related.process_TF_by_president(list_of_files(directory, "txt"), "Chirac")
    # If the president has given multiple speeches then we will combine the TF scores of all of his speeches
    frequent_words = []
    highest_value = None
    for key in total_speeches.keys():   # Throughout all the words in all his speeches

        if highest_value is None:   # Only for the first iteration
            frequent_words.append(key)
            highest_value = total_speeches[key]
        elif total_speeches[key] > highest_value:   # Add it to the list if we find a new highest value
            frequent_words = [key]
            highest_value = total_speeches[key]
        elif highest_value == total_speeches[key]:  # Incase there are multiple words
            frequent_words.append(total_speeches[key])

    if len(frequent_words) > 1:
        print("The most repeated words by president", president, "were:", end=" ")
        for word in range(len(frequent_words) - 1):
            print(word, end=", ")
        print(frequent_words[-1], "| They were all said", highest_value, "times.")
    else:
        print("The most repeated word by president", president, "was:", frequent_words[0], "| It was said",
              highest_value, "times.")










director = "./cleaned/"
all_words = tf_idf_related.list_words(director)
tf_idf_array = tf_idf_related.process_final_2DArray(director)
tf_idf_dict = tf_idf_related.process_TF_IDF(director)
list_fill_names = list_of_files(director, "txt")
