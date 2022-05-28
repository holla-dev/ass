# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagrams(word,anagram):
    # [assignment] Add your code here
    word_list = list(word)
    anagram_list = list(anagram) 
    if sorted(word_list) == sorted(anagram_list):
        print('True')
    else:
        print('False')

        
find_anagrams("below","elbow")




# word = "imagine"
# dev  = "magiine"
# list2 = list(dev)
# list = list(word)
# print(sorted(list))
# print(sorted(list2))
# if sorted(list) == sorted(list2):
#     print("true")

