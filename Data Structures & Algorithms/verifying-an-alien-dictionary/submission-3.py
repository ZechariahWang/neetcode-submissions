class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    order1 = order.index(word1[j])
                    order2 = order.index(word2[j])

                    if order1 > order2: # wrong order ()
                        return False
                    else: # correct order, exit early
                        break
            else: # never found a different character, only deciding factor left is length
                if len(word1) > len(word2):
                    return False

        return True


        

        
        