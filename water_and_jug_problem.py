"""You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.
If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.
Operations allowed:
Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

最开始时，想到了问题本质是找到 m * x + n * y = z(m, n为正是，表示装满水壶，为负表示清空水壶)中的m, n。
想着设置两个循环，让m, n遍历固定的数值，只要找到满足条件的m, n即可解题。
但这种思路存在两个问题：一是m, n遍历的范围怎么确定，二是题目需要回答的是是否可行，并非要过程。
果不其然，即使让m, n在-100到100之间遍历，仍无法解决问题

https://www.math.tamu.edu/~dallen/hollywood/diehard/diehard.htm
通过此网址，找到了解题思路，只要x, y 最大公约数为1，可以生成0-(x + y)之间的所有数字。返回True，
提交后发现2, 6, 8返回的是True。并考虑到一些特殊情况。生成了最终的代码
"""

class Solution:
    def gcd(self, x, y):
        """求解最大公约数"""
        if y == 0:
            return x
        else:
            return self.gcd(y, x % y)

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # 特殊情况的处理
        if z == 0 or z == x or z == y:
            return True
        if z > x + y:
            return False
            
        d = self.gcd(x, y)  
        if d != 0 and z % d == 0:
            return True

        return False
