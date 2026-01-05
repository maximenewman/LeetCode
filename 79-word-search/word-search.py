class Solution:
    """
    The adjacent nodes we can search are 
    Above (x, y+1)
    Below (x, y-1)
    Left  (x-1, y)
    Right (x+1, y)


    We perform DFS from each cell that matches the first character of the word.
    At each step, we check whether the current cell matches word[index].
    If it does, we temporarily mark the cell as visited and recursively search its four neighbors for the next character.
    If any path reaches index == len(word), we return true.
    Otherwise, we backtrack by restoring the cell and continue exploring other paths.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_index: int = 0
        def dfs(x:int, y:int, word_index:int):
            if(word_index == len(word)):
                return True

            if x >= len(board[0]) or x < 0:
                return False
            if y >= len(board) or y < 0:
                return False
            
            if board[y][x] != word[word_index]:
                return False

            tmp = board[y][x]
            board[y][x] = "#"
            
            found = (
                dfs(x,y+1, word_index + 1) or
                dfs(x,y-1, word_index + 1) or
                dfs(x-1,y, word_index + 1) or
                dfs(x+1,y, word_index + 1)
            )

            board[y][x] = tmp
            return found

        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[word_index]:
                    if dfs(x,y, word_index):
                        return True

        return False