class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # This list holds the current parentheses string being built, step by step
        stack = []

        # This list will hold all the final valid parentheses strings
        result = []

        # This function will explore all possible valid combinations using recursion and backtracking
        def backtrack(openN, closedN):
            # ✅ BASE CASE:
            # If we've used all n open and n close brackets, the string is complete and valid
            if openN == closedN == n:
                # Convert the list of characters into a string and save it
                result.append("".join(stack))
                return  # 🛑 Done with this path — go back up one level (backtrack)

            # 🔁 CHOICE 1: Add an open bracket if we still can (i.e., haven't used all n opens)
            if openN < n:
                stack.append("(")               # Push '(' to our stack (make a choice)
                backtrack(openN + 1, closedN)    # 🔽 Recurse deeper with one more open used
                stack.pop()                      # ⬅️ After recursion returns, undo the last choice (backtrack)

            # 🔁 CHOICE 2: Add a close bracket if there are open brackets to match with
            if closedN < openN:
                stack.append(")")               # Push ')' to our stack (make a choice)
                backtrack(openN, closedN + 1)    # 🔽 Recurse deeper with one more close used
                stack.pop()                      # ⬅️ After recursion returns, undo the last choice (backtrack)

        # 🚀 Kick off the recursive process with 0 open and 0 close brackets used
        backtrack(0, 0)

        # ✅ All combinations are now stored in result
        return result


#Okay so basically
#first it runs through the function, then it goes into another function. 
#Now remember this ITS A FUNCTINO IN A FUNCTION
#The pop doesnt' run until we are done with our paranthesis being made BECAUSE of how recursion works
#So once we append, then we call the functoin AGAIN.
#NOW when we go back into the funcrion it has to check through all the checks again, 
#This include checking if they all equal, or openN < n or closedN < openN
#Thats how its able to go into both if statements. 
#then once thats done, it goes back into the stack pop



        