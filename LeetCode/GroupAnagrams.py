# Given an array of strings, words, group the anagrams together and return them.
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedword = "".join(sorted(word))
        if sortedword in anagrams:
            anagrams[sortedword].append(word)
        else:
            anagrams[sortedword] = [word]
    return list(anagrams.values())
    
