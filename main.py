# Chatbot EFREI L1
# William ROBERT | Batur HAMZAOGULLARI

from extract_files import *
import text_treatment
import tf_idf_related

#------------------------------------------------Programme Principale--------------------------------------------------#

directory = ".\speeches"
file_names = list_of_files(directory, "txt")
