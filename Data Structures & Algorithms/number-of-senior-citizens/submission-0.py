class Solution:
    def countSeniors(self, details: List[str]) -> int:
        #start a count 
        count = 0
        #iterate through strings
        for person in details:
            #index the strings
            age = person[11:13]
            #convert into int
            age = int(age)
            #if the nums over 60
            if age > 60:
                #add 1 to count
                count += 1
        #return counbt
        return count
        