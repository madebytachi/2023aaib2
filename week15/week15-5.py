#week15-5.py
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        N = len(s)
        j = 0 #尾巴j
        for i in range(N): #頭是i 先用 Python 把字串的迴圈寫出來
            maxCost -= abs( ord(s[i]) - ord(t[i]) ) #毛毛蟲的頭i 吃葉子
            while maxCost < 0:
                maxCost += abs( ord(s[i]) - ord(t[i]) )# 尾巴j 大便出來
                j += 1
            ans = max(ans, i-j+1) #頭i - 尾j +1 舊式毛毛蟲的長度
        return ans