"""矩阵向右顺时针转动90度，可以将矩阵理解为绕中心旋转的框子。
可以先更改将外框的数据，然后逐层推进，直到最里面
"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

N = len(matrix)
# 定义起始下标数值
i = 0

# 由外框向内逐层推进
while N > 0:
    # 1. 特殊情况处理
    if N == 1:
        break

    # 定义最大下标数值
    max_index = len(matrix) - 1 - i
    j = i

    while j < max_index:
        # 1> 顶部元素获得左侧元素的值，记得将顶部元素放在临时变量temp1里
        temp1 = matrix[i][j]
        matrix[i][j] = matrix[max_index - j + i][i]
        # 2> 右侧元素获得顶部元素的值，记得将右部元素放在临时变量temp2里
        temp2 = matrix[j][max_index]
        matrix[j][max_index] = temp1
        # 3> 底部元素获得右侧元素的值，记得将底部元素放在临时变量temp3里
        temp3 = matrix[max_index][max_index - j + i]
        matrix[max_index][max_index - j + i] = temp2
        # 4> 左侧元素获得右侧元素的值
        matrix[max_index - j + i][i] = temp3

        j += 1

    N -= 2
    i += 1

print(matrix)
