from collections import Counter #dict subclass for counting hashable objects {(Key, value)}
#It is a collection where elements are stored as dictionary keys and 
# their counts are stored as dictionary values.


#we want to return the first time that a non repeating charactter is in the string (s)
#if none, return string with underscore



def first_not_repeating_character(s):
    counts = Counter(s) # a new counter, not empty, contains string (s) #ex: Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
    for character in s: #iterate through string
        if counts[character] == 1: #if counts of each charcter is equal to 1
            return character #that's the input we receive 
    return   "_" #else return None
"""
    T 0(n) -  where n is the number of unique characters
    Counter first goes through list o(n) + 
    for loop also goes through each char n times = 
    which means its an O(n) operation, 

    S 0(n) - 
    Storing in Counter n times where n is the number of unique character.

    find a o(1) situation ===== even though 0(n),we can make it go through the list once. - not possible
"""



"""
    - i knew there was a library from collections called Counter
    - Counter stores elements as keys and their corresponding counts as value (key,value)
    - Created a Counter where it kept track of the # of times each character appeared
    - key = character, value = # of times it appears
    - iterated through a given string
    - checked if character appeared once, and if it did, i wanted to return that first chracter
    - otherwise "_" if there is no instance of a non-repeating character 

"""

