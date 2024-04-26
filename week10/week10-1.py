#week10-1.py
N = int(input('請輸入N:'))
#以前是用 for迴圈寫，今天用函式呼叫函式來寫
def func(n):
  if n==1: return 1 # 終止條件， 像數學歸納法一樣
  return n * func(n-1)
ans = func(N)
print(ans)