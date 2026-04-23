class Solution:
    def isValid(self, s: str) -> bool:
        #first create a stack 
        stack = []

        #next we need to create a dictinoary where closed are the keyt and open is value
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        #so now we need to iterate trhough s
        for character in s:
            #if the chracter is in clsoeto open
            if character in closeToOpen:
                #now we need to make sure the stack isnt empty AND the that the top of the stack is the same then pop it
                if stack and stack[-1] == closeToOpen[character]:
                    #if it matches then remove it
                    stack.pop()
                else:
                    #if it doesnt match then that means its invalid
                    return False
            else:
                stack.append(character)
        #if the stack is empty it means all brackets are matched
        #if len stack is 0 then its true
        return len(stack) == 0
        