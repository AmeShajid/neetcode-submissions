class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                box_id = (r // 3, c // 3)

                if r not in rows:
                    rows[r] = []

                if c not in cols:
                    cols[c] = []

                if box_id not in boxes:
                    boxes[box_id] = []

                # Check Row
                if num in rows[r]:
                    return False

                # Check Column
                if num in cols[c]:
                    return False

                # Check Box
                if num in boxes[box_id]:
                    return False

                # Add the number to all 3
                rows[r].append(num)
                cols[c].append(num)
                boxes[box_id].append(num)

        return True

            