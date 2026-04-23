class Solution:
    def isValid(self, s: str) -> bool:
        #first we need to create a stack
        stack = []

        #then we need to create our dictionary mapping
        mapping = {
            ")" : "(", 
            "]" : "[", 
            "}" : "{"
        }

        #now we need to iterate through s
        for character in s:
            #if our chracter is in our mapping
            if character in mapping:
                #if our stack is not empty AND the last thing in the stack is the same
                if stack and stack[-1] == mapping[character]:
                    #remove it
                    stack.pop()
                #else 
                else:
                    #that means its not in there and we can FALSE
                    return False
            #else
            else:
                #appened the chracter to the stack
                stack.append(character)
        #now return True if it got past everything ahd only when our len(stack) == 0
        return len(stack) == 0