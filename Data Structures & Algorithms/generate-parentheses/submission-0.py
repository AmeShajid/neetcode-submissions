class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack will hold the current parentheses being built
        stack = []

        # result will store all valid parentheses combinations
        result = []

        # helper function to build the parentheses recursively
        def backtrack(openN, closedN):
            # base case: if we've used all open and close brackets
            if openN == closedN == n:
                # join stack into string and add to result
                result.append("".join(stack))
                return

            # if we can still add open brackets, do it
            if openN < n:
                stack.append("(")            # choose an open bracket
                backtrack(openN + 1, closedN) # go deeper
                stack.pop()                  # undo the choice (backtrack)

            # if we can add a close bracket (only if open > close)
            if closedN < openN:
                stack.append(")")             # choose a close bracket
                backtrack(openN, closedN + 1) # go deeper
                stack.pop()                   # undo the choice (backtrack)

        # start the recursion with 0 open and 0 close used
        backtrack(0, 0)

        # return the final list of valid combinations
        return result




        