class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        #create an empty list for storage
        result= []
        #iterate through all words
        for word in words:
            #compare with the all the other words
            for other_word in words:
                #make sure we arent comparing the same word
                if word != other_word:
                    #if word IS IN the other word
                    if word in other_word:
                        #append the answer to list
                        result.append(word)
                        #stop 
                        break
        #return list
        return result
        