class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(len(board[0]))]
        boxes = [set() for i in range(9)]
        for i in range(len(board)):
            current_row = set()
            for j in range(len(board[0])):
                element = board[i][j]
                try:
                    num = int(element)
                    box_index = (i//3)*3+(j//3)
                    if num in columns[j] or num in current_row or num in boxes[box_index]:
                        return False
                    current_row.add(num)
                    columns[j].add(num)
                    boxes[box_index].add(num)
                except:
                    continue
        return True
