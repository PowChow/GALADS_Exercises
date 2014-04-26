'''This is a short exercise designed to test your knowledge of basic natural
language processing (NLP) techniques in Python. 

In each of the parts below, I have provided a function definition (with the
correct arguments but no implementation) and some tests that will pass *if* 
you fill in the correct implementation for each function. If you run this file
 (i.e. run `python nlp_exercise.py` from your shell) and it does not throw
 any errors, then you have finished the exercise!

April 4, 2014 - PC Edited and completed exercise. The code sucessfully runs all tests! 
'''

# Question 1: Normalization and Tokenization
import nltk
import Levenshtein

def process_text(text):
    alphabetic_only = ''.join(c for c in text if c == ' ' or c.isalpha())
    words = [w.lower() for w in nltk.wordpunct_tokenize(alphabetic_only)]
    return words
            
# BEGIN TESTS
assert process_text('Python is SO AWESOME!!!!!! YAy!!!!@ I love programming in python!') == ['python', 'is', 'so', 'awesome', 'yay', 'i', 'love', 'programming', 'in', 'python']
# END TESTS


# Question 2: Count word occurences
def count_words(text):
    words = process_text(text)
    fdist = nltk.FreqDist(words)
    return dict(fdist.items()) 

# BEGIN TESTS
assert count_words('Python is SO AWESOME!!!!!! YAy!!!!@ I love programming in python!') == {'yay': 1, 'python': 2, 'is': 1, 'programming': 1, 'i': 1, 'so': 1, 'in': 1, 'love': 1, 'awesome': 1}
# END TESTS

# Question 3: Create a string distance function
def distance(text1, text2):
    return nltk.metrics.edit_distance(text1, text2)    
    

# BEGIN TESTS
assert distance('I love my mom', 'i love my daddy') < distance('I love my mom', 'I am a big boy now')
assert distance('some strings are similar to other strings', 'some strings') > distance('some strings are similar to other strings', 'some strings are similar')
assert distance('i hate hate hate noodles.', 'i hate hate noodles') < distance('i hate hate hate noodles.', 'i hate noodles.')
# END TESTS

print 'All tests passed. Congratulations!'
