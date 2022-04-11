# Python_project

**Task description**
1. Print on the screen total number of words and sentences in the text.
 
2. Give a number of occurrences of each word and the frequency (number_of_occurrences / total_number_of_words) for this word. To do this you will have to first remove special characters/convert everything to lowercase and calculate the total number of words. I would use dictionaries that map each word to a value that you can then increment. There are might be some other ways to do it.

3. As an output a sorted list in csv format (as a separate csv file with name result.csv) of the most frequent word first followed by the second most frequent as well as the number of times that word appears and its overall % of words, so the words “a” “I” “an” should all appear frequently. Make sure that you don’t include spaces (“ “) and that they are filtered out. Look at your csv output to make sure it makes sense. Another possible problem area is apostrophes. You should filter “that’s” to “thats”, otherwise you will very likely get “s” as a very popular word.

Sample CSV output:

a,500,0.3

i,300,0.23

the,150,0.12
...

4. Give me the number of sentences and the frequency in the novel where the first word in the sentence is “the”, or “The” You will have to do some string comparisons (look for the “.” Or “?” or “!” Signaling the end of a sentence)

5. Find the most frequent two word combination in the text (e.g. “I am” or “synchrotron radiation”). Print it on the screen.
