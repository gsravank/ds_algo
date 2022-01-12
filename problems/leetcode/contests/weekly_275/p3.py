def diffTwoStrings(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    for i in range(min(l1, l2)):
        if s1[i] != s2[i]:
            break

    if s1[i + 1:] == s2[i:]:
        return 1
    else:
        return 2
    
print(diffTwoStrings('ackt', 'act'))


"""
import string

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        sorted_tw_map = dict()
        for word in targetWords:
            sorted_tw_map[''.join(sorted(word))] = word
        
        legit_tw_words = dict()
        for word in startWords:
            word_chars = set(word)
            for char in string.ascii_lowercase:
                if char not in word_chars:
                    curr_word = ''.join(sorted(word + char))
                    if curr_word in sorted_tw_map:
                        legit_tw_words[sorted_tw_map[curr_word]] = True
        
        count = 0
        for word in targetWords:
            if word in legit_tw_words:
                count += 1
        return count
            
        
            
        
"""