"""判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1. 判断数独每一行的数字是否符合要求
        for i in range(9):
            temp = []
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in temp:
                    temp.append(board[i][j])
                elif board[i][j] in temp:
                    return False
                
        # 2. 判断数独每一列
        for i in range(9):
            temp = []
            for j in range(9):
                if board[j][i] != '.' and board[j][i] not in temp:
                    temp.append(board[j][i])
                elif board[j][i] in temp:
                    return False
        
        # 3. 判断小方格   
        
        for r in range(3):  # 行的3个位置
            for c in range(3):  # 列的3个位置
                # 1> 生成小方格
                grid = [board[i][j] for i in range(3 * r, 3 * (r + 1)) for j in range(3 * c, 3 * (c + 1))]
                
                # 2> 判断小方格内的元素
                temp = []
                for ele in grid:
                    if ele != '.' and ele not in temp:
                        temp.append(ele)
                    elif ele in temp:
                        return False
        
        # 无重复项，返回True
        return True
