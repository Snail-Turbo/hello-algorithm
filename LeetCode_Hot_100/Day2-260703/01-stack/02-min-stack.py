"""
LeetCode 155. 最小栈
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
实现 MinStack 类:
MinStack() 初始化堆栈对象。
void push(int val) 将元素 val 推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
输入：
7
push -2
push 0
push -3
getMin
pop
top
getMin
输出：
-3
0
-2
约束条件：
-2^31 <= val <= 2^31 - 1
pop、top 和 getMin 操作总是在非空栈上调用
push, pop, top, and getMin 最多被调用 3 * 10^4 次
"""

# 主要思路
#
# 维护一个min_stack，里面存局部最小值
#
# push的时候，如果当前值小于等于min_stack的栈顶，就把当前值也push到min_stack中
# pop的时候，如果当前值等于min_stack的栈顶，就把min_stack的栈顶也pop掉，这样min_stack的栈顶就是当前栈的最小值。


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:  # <=的原因是为了处理重复的最小值情况
            self.min_stack.append(val)

    def pop(self) -> int:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None


if __name__ == "__main__":

    """
    input_string=
    7
    push -2
    push 0
    push -3
    getMin
    pop
    top
    getMin

    """

    count_operations = int(input())
    min_stack = MinStack()
    for _ in range(count_operations):
        operation = input().split()
        if operation[0] == "push":
            min_stack.push(int(operation[1]))
        elif operation[0] == "pop":
            min_stack.pop()
        elif operation[0] == "top":
            print(min_stack.top())
        elif operation[0] == "getMin":
            print(min_stack.getMin())
