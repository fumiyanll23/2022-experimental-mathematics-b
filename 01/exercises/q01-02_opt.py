# レポート問題02 (オマケ)
# 50以下の素数をファイルに出力するプログラム
from math import sqrt

def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

N = 50
FILE_NAME = "./q01-02.txt"
with open(FILE_NAME, "w") as fp:
    for i in range(2, N-1):
        if is_prime(i):
            ## int型のままではファイルに書き込めないため、str型に変換する
            fp.write(f"{i}\n")
