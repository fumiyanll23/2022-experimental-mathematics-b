# レポート問題01
# 異なる n 個のものから r 個を選び出して並べる並べ方の総数 n_P_r を求めるプログラムを記述せよ

def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

def permutation(n: int, r: int) -> int:
    return factorial(n) // factorial(r)

n = int(input("整数nを入力してください："))
r = int(input("整数r (≦ n) を入力してください："))
print(f"n個のものからr個を選び出して並べる並べ方の総数は{permutation(n, r)}です")
