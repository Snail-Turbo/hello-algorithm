
# If you need to import additional packages or classes, please import here.

def func():

    str1 = input()
    str2 = input()

    len_str_1 = len(str1)
    len_str_2 = len(str2)

    dp = [[0] * (len_str_2 + 1) for _ in range(len_str_1 + 1)]

    for i in range(len_str_1+1):
        dp[i][0] = i

    dp[0] = [j for j in range(len_str_2 + 1)]

    for i in range(1, len_str_1 + 1):
        for j in range(1, len_str_2 + 1):

            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                continue

            tmp_0 = dp[i][j-1]
            tmp_1 = dp[i-1][j]
            tmp_2 = dp[i-1][j-1]

            # choices = (tmp_0, tmp_1, tmp_2)

            dp[i][j] = min(tmp_0, tmp_1, tmp_2) + 1

    print(dp[-1][-1])


def func_insert(str1: str, str2: str):
    len_str1 = len(str1)
    len_str2 = len(str2)

    dp = [0] * (len_str2 + 1)

    dp[0] = len_str1

    0, 1, 2, 3, 4, 5
    1, 
    2
    3
    4
    5


if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()

    func()
