class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        """
        Runtime: 32 ms, faster than 78.04% of Python3 online submissions for Game of Life.
        Memory Usage: 14 MB, less than 17.17% of Python3 online submissions for Game of Life.
        """
        def in_board(x, y, row, col):
            return x >= 0 and y >= 0 and x < row and y < col
        
        def countNeighbor(board, row, col):
            neighbors = [[0] * col for _ in range(row)]
            all_dirs = [[-1, -1], [0, -1], [1, -1],
                        [-1, 0], [1, 0],
                        [-1, 1], [0, 1], [1, 1]]
            for x in range(row):
                for y in range(col):
                    for d in all_dirs:
                        x_neighbor, y_neighbor = x + d[0], y + d[1]
                        if in_board(x_neighbor, y_neighbor, row, col):
                            neighbors[x][y] += board[x_neighbor][y_neighbor]
            return neighbors
        
        row, col = len(board), len(board[0])
        counted = countNeighbor(board, row, col)
        for x in range(row):
            for y in range(col):
                if counted[x][y] == 3:
                    board[x][y] = 1
                elif counted[x][y] == 2 and board[x][y] == 1:
                    board[x][y] == 1
                else:
                    board[x][y] = 0
                            
            
