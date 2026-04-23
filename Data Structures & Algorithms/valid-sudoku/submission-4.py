class Solution:
    #in this code basically
    # first make storage
    #iterate through board
    #find what box its in
    #create the lists if they dont exist
    #if there is a duplicate return false
    #if its not in there add it
    #return
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #we need to store the row, column and box id
        row = {}
        column = {}
        boxes = {}

        #now we need to iterate through the rows and columns
        #we know its already 1-9 so the range is 9
        for r in range(9):
            for c in range(9):
                #then we need to grab the number that is in that square
                #its the board list
                num = board[r][c]

                #if we see a period it means its empty and we just continue
                if num == ".":
                    continue
                
                #then we need to get the location of this box as an id
                #its going to be coordinate style
                #floor down to smallest number
                box_id = (r // 3, c // 3)

                #now we need to check if that number is in our storages, if its not then we create a new list for that 
                if r not in row:
                    row[r] = []
                
                if c not in column:
                    column[c] = []

                if box_id not in boxes:
                    boxes[box_id] = []

                #now we need to check if the number is alreayd in the storage
                if num in row[r]:
                    return False
                
                if num in column[c]:
                    return False
                
                if num in boxes[box_id]:
                    return False

                #if its gets past that that means its not in there and we need to append this to our list
                row[r].append(num)
                column[c].append(num)
                boxes[box_id].append(num)
        return True


        
