# レポート問題02
# ファイルから入力された内容を表示するプログラム

# FILE_NAME = "./q01-02.txt"
# fp = open(FILE_NAME, "r")
# line = fp.readline()

# for _ in line:
#     print(line, end="")
#     line = fp.readline()
# fp.close()

# 以下のようにwith文を用いると、fp.close()を記述する必要がなくなり、ファイルの閉じ忘れを心配しなくて済む (https://www.python.jp/pages/with-statement-3.9.html)
FILE_NAME = "./q01-02.txt"
with open(FILE_NAME, "r") as fp:
    for line in fp.readlines():
        print(line, end="")
