# Problem Statement : find the longest word from an article.

sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.
Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

# My Solution
def get_longest_word(sen):
    my_list = sen.replace('.',' ').replace(',',' ').split() #, & . are ignored
    word = ''
    for i in my_list:
        if len(i) > len(word):
            word = i
        else:
            word
    print (word)

get_longest_word(sample_story)

# My Approach
'''
- Split the sentence into individual words using the split() function.
- Initialize a variable to keep track of the longest word found so far.
- Iterate through each word in the list:
- Compare its length with the current longest word.
- If it’s longer, update the variable.
- Continue until all words are checked.
- At the end, the variable holds the longest word.
'''
# Complexity Analysis
'''
- Time: O(n), where n is the number of words.
- Space: O(1), since we only store one variable for the longest word.
'''

# Source : PCAP Python Essentials 2 Module : String Manipulation
