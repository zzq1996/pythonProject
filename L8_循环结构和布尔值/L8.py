"""
@Author : zhang
@create : 2022/6/6 10:00
"""
"""
8.1 for循环：快速回顾——有限循环
    - for <var> in <sequence>:<body>
        - 循环索引变量var依次取序列中的每个值，循环体中的语句针对每个值执行依次
8.2 不定循环（条件循环）
    - while <condition>:<body>
8.3 常见循环模式
    8.3.1 交互式循环
        - 允许用户根据需要重复程序的某些部分
    8.3.2 哨兵循环
        - 哨兵循环不断处理数据，直到遇到哨兵，表明迭代结束
    8.3.3 文件循环
        - 将文件对象作为for循环中的序列，按行读取文件
            - 在文件末尾，readline()返回一个空字符串
    8.3.4 嵌套循环
        - 先设计外层，不考虑内层的内容；然后设计内层的内容，忽略外层循环
8.4 布尔值计算
    - 在Python中用False和True表示
    - Python提供not、and和or三个布尔运算符（按优先级从高到低排序）
    - 可使用DeMorgan第一定律转换布尔表达式形式
8.5 其他常见结构（循环结构的替代结构）
    8.5.1 后测试循环（do-while）
        - 条件测试在循环体之后（必须至少执行一次循环体）
    8.5.2 循环加一半
        - 循环出口实际上位于循环体的中间
        - 可避免处理哨兵值
    8.5.3 布尔表达式作为判断
        - 对序列类型，空序列为假，任何非空序列为真
"""


# for循环
def average1():
    n = int(input("How many numbers do you have?"))
    total = 0.0
    for i in range(n):
        x = float(input("Enter a number >>"))
        total = total + x
    print("\nThe average of the numbers is", total / n)


# average1()

# 交互式循环
def average2():
    total = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = float(input("Enter a number >>"))
        total = total + x
        count = count + 1
        moredata = input("Do you have more numbers(yes or no)?")
    print("\nThe average of the numbers is", total / count)


# average2()

# 哨兵循环（不含负值）
def average3():
    total = 0.0
    count = 0
    x = float(input("Enter a number(negative to quit) >>"))
    while x >= 0:
        total = total + x
        count = count + 1
        x = float(input("Enter a number(negative to quit) >>"))
    print("\nThe average of the numbers is", total / count)


# average3()

# 哨兵循环（扩大可能的输入），将空字符串作为哨兵值
def average4():
    total = 0.0
    count = 0
    xStr = input("Enter a number(<Enter> to quit) >>")
    while xStr != "":
        x = float(xStr)
        total = total + x
        count = count + 1
        xStr = input("Enter a number(<Enter> to quit) >>")
    print("\nThe average of the numbers is", total / count)


# average4()

# 文件循环，累加每行数字
def average5():
    fileName = input("What file are the number in?")
    infile = open(fileName, "r")
    total = 0.0
    count = 0
    for line in infile:
        total = total + float(line)
        count = count + 1
    print("\nThe average of the numbers is", total / count)


# 文件循环，设置空行为哨兵值（对于空白行，有换行符"\n"!=""，故遇到空行，程序仍执行）
def average6():
    fileName = input("What file are the number in?")
    infile = open(fileName, "r")
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        total = total + float(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", total / count)


# average6()


# 允许一行输入多个数字（以逗号隔开），并计算其均值
# 处理一行中的数字的循环在文件处理循环内缩进，外层while循环对文件的每一行进行一次迭代
def average7():
    fileName = input("What file are the number in?")
    infile = open(fileName, "r")
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            total = total + float(xStr)
            count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", total / count)


# average7()


# 后测试循环
while True:
    number = float(input("Enter a positive number:"))
    if number >= 0:
        break  # Exit loop if number is valid
    else:
        print("The number you entered was not positive")

# 循环加一半
while True:
    number = float(input("Enter a positive number:"))
    if number >= 0:
        break  # Exit loop if number is valid
    print("The number you entered was not positive")

# event_loop3.py
#      Color changing window with clicks to enter text

from graphics import *


def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")


def handleClick(pt, win):
    # create an Entry for user to type in
    entry = Entry(pt, 10)
    entry.draw(win)
    # Go modal: wait until user types Return or Escape Key
    while True:
        key = win.getKey()
        if key == "Return":
            break
    # undraw the entry and draw Text
    entry.undraw()
    Text(pt, entry.getText()).draw(win)
    # clear (ignore) any mouse click that occurred during text entry
    win.checkMouse()


def evenLoop():
    win = GraphWin("Click and Type", 500, 500)
    # Event Loop: handle key presses and mouse clicks until the user
    #    presses the "q" key.
    while True:
        key = win.checkKey()  # 捕捉键鼠输入信号
        if key == "q":  # loop exit
            break
        if key:  # 相当于if key!=""
            handleKey(key, win)
        pt = win.checkMouse()
        if pt:  # 相当于if pt!=None
            handleClick(pt, win)
    win.close()

