# Problem Statement : Count the number of occurrences of a given word in a text file.

# My Solution
def count_occurences(file_name, word):
    try:
        stream = open(file_name)
        my_word_list = stream.read().replace(',',' ').replace('.',' ').upper().split()
        return my_word_list.count(word.upper())
        stream.close()
    except Exception as e:
        print(e)

Word_Count = count_occurences('new_file.txt','this')
print(Word_Count)

# My Approach
'''
- Clean the text → Remove punctuation so only words remain.
- Normalize case → Convert all words to uppercase (or lowercase) to avoid case sensitivity issues.
- Split into words → Use split() to create a list of words.
- Count occurrences → Use the count() method to count how many times the target word appears.
- Return result → Output the final count
'''

# Complexity Analysis
'''
- Time: O(n), where n = number of words in the file (we scan each word once).
- Space: O(n) if we store all words in a list.
'''

# Source : PCAP Python Essentials 2 Module : String Manipulation


