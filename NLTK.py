# -*- coding: utf-8 -*-

import nltk
import gzip
from nltk.book import *

#Create a function percent(word, text) that calculates how often a given word occurs in a text. 
def percent(word,text):
    w = text.count(word)
    t = len(text)    
    return 100 * w / t
   

def words_lt_or_eq_five(text):
    return [word for word in text if len(word) <= 5]

#text = input("Enter value for text variable: ")
#Use any text in the nltk book (text1, text2, etc….)
text = nltk.book.text1

word = input("Enter value for word variable: ")

#1) Return the value of count for the selected text
print("\nThe total count of", word, "in", text, "is:")
print(text.count(word))
proceed = input("Press Enter to proceed: ")

#2) Return the percentage of counts out of the overall selected text
print("The total number of words in", text, "is:\n", len(text))
print("\nThe percentage of the word", word,"over the total number of words in", text, "is:\n", percent(word,text), "%")
proceed = input("Press Enter to proceed: ")

#3) Find words in the selected text that contains 5 characters or less
print("Words that contain 5 characters or last:", words_lt_or_eq_five(text))
proceed = input("Press Enter to proceed: ")

#4) Print the results in an output file named nltk_out.dat
with open("nltk_out.dat", "a") as f:
    print("\nThe total count of", word, "in", text, "is:", file=f)
    print(text.count(word), file=f)
    print("The total number of words in", text, "is:\n", len(text), file=f)
    print("\nThe percentage of the word", word,"over the total number of words in", text, "is:\n", percent(word,text), "%", file=f)
    print("Words that contain 5 characters or last:", words_lt_or_eq_five(text), file=f)
    print("Results have been saved to nltk_out.dat")
    proceed = input("Press Enter to proceed: ")

#5) Store the output as gzip or pickle
    f_in = open('nltk_out.dat', 'rb')
    f_out = gzip.open('nltk_out.dat.gz', 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()
    print("Output has been stored as a gzip file")
    proceed = input("Press Enter to to end the program: ")










    

