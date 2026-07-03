
# 主要思路：维护一个单调递减栈，栈中存储的是【温度的索引】。
# 遍历温度数组，如果当前温度大于栈顶索引对应的温度，则弹出栈顶索引，直到栈为空或当前温度小于等于栈顶索引对应的温度。

# 然后将当前索引入栈。对于每个索引，如果栈不为空，则说明找到了一个更高的温度，计算天数差并存入答案数组中。
class Solution:
    def dailyTemperatures(self, temperatures:list)->list:
        temperatures_length = len(temperatures)
        stack = []
        answer = [0] * temperatures_length

        for i in range(temperatures_length-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                answer[i] = stack[-1] - i

            stack.append(i)

        return answer
    

if __name__ == "__main__":
    line = input()

    intput_list = list(map(int, line.split()[-1][1:-1].split(',')))
    so = Solution()
    result_list = so.dailyTemperatures(intput_list)

    print(f"[{','.join(map(str, result_list))}]")