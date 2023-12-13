<p align="center" width="100%">
    <img width="33%" src="https://github.com/Think-Bubbles/pychatbot-Robert-Hamzaogullari-A/blob/main/Image%20Efrei%20RM.png">
</p>


Welcome to our Chatbot project – a Python-based conversational agent capable of delivering personalized responses and extracting specific information from text files. This project combines the power of natural language processing and data interpretation to create an interactive and adaptable chatbot experience.


<p align="center" width="100%">
    | <a href="#features">Features</a> | <a href="#getting-started">Getting Started</a> | <a href="#installation">Installation</a> | <a href="#known-bugs">Known bugs</a> |
</p>

## Features
Custom Answers: Our chatbot is equipped to provide tailor-made responses based on custom questions, making interactions engaging and contextually relevant.

Information Extraction: Leveraging advanced text analysis techniques, the chatbot can sift through text files, extracting and interpreting specific information, enhancing its ability to provide insightful and accurate responses.

## Getting Started 

Our chatbot is capable of two seperate things, but in both cases it needs text files to extract the related information. 
Therefore the speeches and cleaned folders both contain the relevant text files.
When running the program, you will be presented with a number of options:
- Entering "0" will either end the program or return to a previous menu (each case will clearly be explained)
- Entering "1" will at first allow you to ask specific questions and get custom answers
  In other cases (once again this will clearly be explained) you will gain access to specific instructions
- Entering "2" will let you gain access to a number of specific utilities
Once again all of the instructions will clearly be explained when running the program

## Installation

TIn order to use this program, please insure that you have the following installed
- [Python](https://www.python.org/downloads/) version 3.9 or later
- [Math library](https://pypi.org/project/python-math/#files) in case you don't already have it

## Known bugs 

1.  When using the menu, it is possible that if you are asked to enter one of the presidents name but you write another word that was't instructed, then the program will fail. We have not yet added test cases for every parameter.

2. When calculating our IDF score, there is a + 1, it is still unclear why we have been instructed to add this, as it changes a few results (notable functionality number 1 and number 6)

## Contributors 

- Robert William
- HAMZAOGULLARI Batur
