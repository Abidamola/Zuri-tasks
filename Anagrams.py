# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

# [assignment] Add your code here
def find_anagrams(s1, s2):
    if (sorted(s1) == sorted(s2)):
        return True
    else:
        return False


