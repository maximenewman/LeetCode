class Solution:
    """
    Idea is to add all the connected lands together
    Then, when we discover a new land that isn't connected we increment our count
    We can use dfs to traverse the grid

    For each node there are 4 possible neighbors.
    Above (x, y+1)
    Below (x, y-1)
    Left  (x-1, y)
    Right (x+1, y)

    We will run dfs on each in order to connect the islands
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        islands: int = 0

        def dfs(x:int , y:int):
            if x >= len(grid[0]) or x < 0:
                return
            if y >= len(grid) or y < 0:
                return
            if grid[y][x] == "0":
                return
            else:
                grid[y][x] = "0"

            dfs(x, y+1)
            dfs(x, y-1)
            dfs(x-1, y)
            dfs(x+1, y)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    islands += 1
                    dfs (x,y)
        return islands
