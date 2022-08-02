# レポート問題03
# 適当に与えた4次正方行列をテキストファイルに出力するプログラムを記述せよ

## 行数 (== 列数)
N = 4
## 入力を受け取るためにゼロ行列を用意する
matss = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        matss[i][j] = int(input(f"({i+1},{j+1})成分を入力してください："))
print("入力された行列は")
print("[ ", end="")
for i in range(N):
    if i == 0:
        print(*matss[i])
    elif i == N-1:
        print(" ", *matss[i], end="")
    else:
        print(" ", *matss[i])
print(" ]")
