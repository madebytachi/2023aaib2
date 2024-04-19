# 找出島(一堆1)的周長, 也就是繞一圈的長度。
# 想法很簡單: 從0變1、從1變0, 都是周長+=1
class Solution(object):
    def islandPerimeter(self, grid):
        ans = 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            if grid[i][0]==1: ans+=1 # 最左邊的邊界
            if grid[i][N-1]==1: ans+=1 # 最右邊的邊界
        for j in range(N):
            if grid[0][j]==1: ans+=1 # 最上面的邊界
            if grid[M-1][j]==1: ans+=1 # 最下面的邊界

        for i in range(M): # 左手i 對每一個格子
            for j in range(N): # 右手j
                # 如果可再看到下面鄰居、右邊鄰居 就看是否 0變1 或1變0
                if j+1<M and grid[i][j]+grid[i+1][j]==1: ans+=1
                if j+1<N and grid[i][j]+grid[i][j+1]==1: ans+=1
        return ans