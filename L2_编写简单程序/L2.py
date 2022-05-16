"""
2.3 程序要素

2.3.1 名称
    标识符：以字母或下划线开头，由字母、数字和下划线组成，区分大小写。
    关键字：['False', 'None', 'True', 'and', 'as', 'assert',
        'break', 'class', 'continue', 'def', 'del',
        'elif', 'else', 'except', 'finally', 'for', 'from',
        'global', 'if', 'import', 'in', 'is', 'lambda',
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
        'try', 'while', 'with', 'yield']

2.3.2 表达式：产生或计算新数据值的程序代码片段

"""

"""
2.4 输出语句：包含指定结束文本的关键字参数的print语句的模版：print(<expr>,<expr>,..., end="\n")
"""
print("The answer is:", end=" ")  # 这里print的输出空格结束，而不是默认的换行
print(3 + 4)

"""
2.5 赋值语句
    2.5.1 简单赋值：在对变量进行赋值时，赋值语句不会导致旧值被擦除和覆盖，而是将变量切换到引用新值。
"""
a = 10
b = 20
a = b
print(a)

"""
    2.5.2 赋值输入：
        文本输入：<variable>=input(<prompt>)
        数字输入：<variable>=eval(input(<prompt>))
            代码注入攻击：eval函数会对输入的任何内容进行求值，若输入恶意指令，可将恶意代码注入。
"""
ans = eval(input("Enter an expression:"))
print(ans)

"""
    2.5.3 同时赋值：<var1>,<var2>,...,<varN>=<expr1>,<expr2>,...,<exprN>
        变量交换时，赋值是同时的，避免擦除一个原始值
        也可用单个input从用户那里获取多个数字
"""
a, b = b, a


def main():
    print("This program computes the average of two exam scores.")
    score1, score2 = eval(input("Enter two scores separated by a comma:"))  # 输入两个数字，用逗号隔开
    average = (score1 + score2) / 2
    print("The average of the", score1, "and", score2, "is:", average)


main()

"""
    2.6 确定循环（计数循环）：for <var> in <sequence> <body>，其中<sequence>确定了循环执行的次数
"""
for i in range(10):
    print("hello")

for i in [0, 1, 2, 3]:
    print(i)
