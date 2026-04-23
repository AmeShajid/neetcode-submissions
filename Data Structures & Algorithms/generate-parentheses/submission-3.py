class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paren if opne < n
        #only add close paern if closed < n
        #valid if opne == clsoed == n 

        #hold our parenthesis
        stack = []
        #hold list of valid parenthesis 
        result = []

        #doing it recursively we dfont have to pass in stack and result 
        def backtrack(openN, closedN):
            #if we used all open and closed brackets then just do the result 
            if openN == closedN == n:
                result.append("".join(stack))
                return
            
            #if we can still add open then 
            if openN < n:
                #add a  open parent
                stack.append("(")
                #now start open at +1 
                backtrack(openN + 1, closedN)
                #undo the backtrack
                stack.pop()
            
            #if we can add a closing bracket then add it only if open > close
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                #undo the backtrack
                stack.pop()
        #start recursion at 0,0    
        backtrack(0,0)
        return result

        