class Solution:
    def isValid(self, s: str) -> bool:
        # create an empty list to act like a stack
        stack = []

        # dictionary to map closing brackets to their matching opening brackets
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # go through each character in the input string
        for character in s:
            # if the character is a closing bracket
            if character in closeToOpen:
                # check if the stack is not empty and the top item matches the opening bracket
                if stack and stack[-1] == closeToOpen[character]:
                    # if it matches, pop the top item from the stack (bracket is balanced)
                    stack.pop()
                else:
                    # if it doesn't match, the string is invalid
                    return False
            else:
                # if it's an opening bracket, add it to the stack
                stack.append(character)

        # if the stack is empty, it means all brackets matched
        return len(stack) == 0

        