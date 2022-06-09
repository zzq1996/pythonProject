"""
@Author : zhang
@create : 2022/6/8 13:53
"""
"""
9.1 模拟短柄壁球
    - 计算机可以对现实世界的过程建模，以提供其他方法无法获取的信息。
9.2 伪随机数
    - 模拟程序不得不处理不确定的事件。
        - 蒙特卡罗模拟：依靠概率或机会事件的模拟技术
    - 伪随机数发生器从某个"种子"值开始工作，生成数字序列
        - 若种子值相同、生成函数相同，则结果相同
    - randrange()和random()函数：根据模块加载的日期和时间推导出初始种子值
        - randrange(m,n,k):生成(m,n)之间k的倍数的值，生成随机数满足均匀分布
        - random():生成[0,1)之间的伪随机浮点值
9.3 自顶向下的设计
    - 从总问题开始，尝试用较小的问题来表达解决方案，然后将小问题汇总。
        1. 将算法表示为一系列较小的问题
        2. 为每个小问题开发一个接口
        3. 用较小问题的接口来表示该算法，从而描述算法的细节
        4. 对每个较小的问题重复此过程
    - 抽象：确定某些重要特征并忽略其他细节的一般过程。

9.4 自底向下的实现
    - 一次设计一小块程序比尝试一次处理整个问题更容易，同样，实现也最好一点点来
    - 9.4.1 单元测试
        - 独立检验较大程序中每个组件的过程
        - 通过单元测试实现关注点分离，能够实现和调试复杂的程序

9.5 其他设计技术
    - 9.5.1 原型与螺旋式开发
        - 从程序或程序组件的简单版本开始，然后尝试逐渐添加功能，直到满足完整的规格说明
    - 9.5.2 设计的艺术
        - 螺旋式开发不是自顶向下的替代品，两者是互补的办法
            - 在设计原型中，仍会用到自顶向下的技术
        - 面向对象的设计方法
    - 设计是艺术与科学的结合
    
"""

# rball.py
#    Simulation of a racquetball game

from random import random


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")


def getInputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a == 15 or b == 15


def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))  # 类型指示符%可用于打印百分比
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))


if __name__ == '__main__':
    main()
