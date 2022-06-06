"""
@Author : zhang
@create : 2022/5/29 11:05
"""
"""
6.1 函数的功能
    - 可用于减少代码重复，并使程序更易于理解和维护
    - 模块化程序
6.4 函数和参数：令人兴奋的细节
    - 函数的定义：def <name>(<formal-parameters>):    <body>
    - 参数传递提供了一种初始化函数中变量的机制
        - 参数是函数的输入
    - 函数中使用另一函数中的变量：将变量作为参数传入
    - 函数调用过程：
        1. 调用程序在调用点暂停执行
        2. 函数的行参获得由调用中的实参提供的值
        3. 执行函数体
        4. 控制返回到函数被调用之后的点
    - 函数完成时，会回收局部函数变量占用的内存。局部变量不保留从一个函数执行到下一个函数执行的任何值。
    - 当函数定义具有多个参数时，实参按照位置与行参匹配。
        - 可以利用关键字修改此行为，这些参数通过名称匹配（如调用print中的end=""）
    - Python"按值"传递所有参数
        - 通过return语句可修改实参的值
        - 如果传递的值是可变对象，则对象所做的更改会对调用者可见
6.5 返回值的函数
    - 当Python遇到return时，它会立即退出当前函数，并将控制返回到函数被调用之后的点
        - return语句中提供的值作为表达式结果发送到调用者
    - 函数需返回多个返回值：在return语句中列出多个表达式来完成
    - Python中的所有函数都有返回值，没有定义return语句的函数默认返回值为None
"""


# 函数的非正式讨论
def happy():
    print("Happy Birthday to you")


def sing(person):
    happy()
    happy()
    print("Happy birthday,dear", person + ".")
    happy()


def happySing():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Elmer")


# happySing()

# 带有函数的终值程序
from graphics import *


def drawBar(window, year, height):
    # draw a bar in window starting at year with given height
    bar = Rectangle(Point(year, 0), Point(year + 1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)


def createLableWindow():
    # create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), '0.0K').draw(win)
    Text(Point(-1, 2500), '2.5K').draw(win)
    Text(Point(-1, 5000), '5.0K').draw(win)
    Text(Point(-1, 7500), '7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)
    return win


# 借助drawBar函数，消除重复代码
def drawInvestment2():
    print("This program plots the growth of a 10-year investment.")
    principal = float(input("Enter the initial principal:"))
    apr = float(input("Enter the initial apr:"))
    # # create a graphics window with labels on left edge
    # win = GraphWin("Investment Growth Chart", 320, 240)
    # win.setBackground("white")
    # win.setCoords(-1.75, -200, 11.5, 10400)
    # Text(Point(-1, 0), '0.0K').draw(win)
    # Text(Point(-1, 2500), '2.5K').draw(win)
    # Text(Point(-1, 5000), '5.0K').draw(win)
    # Text(Point(-1, 7500), '7.5K').draw(win)
    # Text(Point(-1, 10000), '10.0K').draw(win)
    win = createLableWindow()
    # Draw bar for initial principal
    drawBar(win, 0, principal)
    # Draw bars for successive years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)
    # 在程序结束时添加一个输入语句，让其暂停，给用户一个读取结果的机会
    input("Press the <Enter> key to quit.")
    win.close()


# drawInvestment2()


# 利用distance函数，增强第四章中的交互三角形程序计算三角形的周长
import math


def square(x):
    return x ** 2


def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist


def drawByUser():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)
    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)
    # Calculate the perimeter of the triangle
    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText("The perimeter is: {0:0.2f}".format(perim))
    # Wait for another click to exit
    win.getMouse()
    win.close()


# drawByUser()

# 函数的应用
def happy2():
    return "Happy Birthday to you!\n"


def verseFor(person):
    lyrics = happy2() * 2 + "Happy birthday,dear" + person + ".\n" + happy2()
    return lyrics


def happySing2():
    outf = open("../happy.txt", "w")
    for person in ["Fred", "Lucy", "Elmer"]:
        print(verseFor(person), file=outf)
    outf.close()


# happySing2()

# 函数返回多个返回值
# 返回两个数的和与差
def sumDiff():
    x, y = input("Please enter two numbers(num1,num2)").split(",")
    return float(x + y), float(x - y)


# 修改实参的值
# addInterest函数中创建了新值，并且列表中的复制导致它引用新值；当Python执行垃圾收集时，原来的值被清除
# 变量amounts从未改变，它仍然引用相同的列表，只是列表的状态在addInterest函数已更改
def addInterest(balance, rate):
    for i in range(len(balance)):
        balance[i] = balance[i] * (1 + rate)


def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    addInterest(amounts, rate)
    print(amounts)
