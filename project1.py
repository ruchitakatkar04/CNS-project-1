import string

# Initializing Variables
num_sentences = 0
num_words = 0
the_num_sentences = 0
frequency_the = 0


# Task 0

with open('war_and_peace.txt', 'r') as f:  # opening and reading file
    for line in f:
        line = line.rstrip()  # removing the space on right side
        num_sentences += line.count('.') + line.count('!') + line.count('?')  # counting the sentences

with open('war_and_peace.txt', 'r') as f:
    for line in f:
        words = line.split(None)  # splitting into words and storing in list
        num_words += len(words)  # finding length of list

print("Number of sentences:", num_sentences)
print("Number of words:", num_words)


# Task 1

text = open('war_and_peace.txt', "r")  # Open the file in read mode

d = dict()  # Create an empty dictionary

for line in text:  # Loop through each line of the file

    line = line.strip()  # Remove the leading spaces and newline character

    # Convert the characters in line to

    line = line.lower()  # lowercase to avoid case mismatch

    line = line.translate(line.maketrans("", "", string.punctuation))  # Remove the punctuation marks from the line

    words = line.split(" ")  # Split the line into words

    for word in words:     # Iterate over each word in line

        if word in d:         # Check if the word is already in dictionary
            d[word] = d[word] + 1    # Increment count of word by 1
        else:
            d[word] = 1

sorted_by_value = sorted(d.items(), key=lambda kv: kv[1], reverse=True)  # sorting  dictionary as higher value first

with open('result.csv', 'w', newline='') as f:  # creating csv file
    for w in sorted_by_value:
        f.write(w[0] + "," + str(d[w[0]]) + "," + str(d[w[0]] / num_words) + '\n')  # writing in to csv file


# Task 2
with open('war_and_peace.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        the_num_sentences += (line.count(". the") + line.count("! the") + line.count("? the") +
                              line.count('. The') + line.count('! The') + line.count('? The'))
    print("Number of sentences starts with 'the' :", the_num_sentences)

frequency_the = the_num_sentences / num_sentences
print("Frequency of THE sentences:", frequency_the)


# Task 3

import re
from itertools import islice
from collections import Counter

s = open("war_and_peace.txt")  #opening file
g = s.read()
words = re.findall("\w+", g) #finding the reg-ex
letter = (Counter(zip(words, islice(words, 1, None))))    #counting The frequent two word combunations
print(letter.most_common()[0])
