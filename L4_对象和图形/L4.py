"""
@Author : zhang
@create : 2022/5/21 12:16
"""

"""
4.1 概述
    - Python自带的标准GUI（图形用户界面）模块为Tkinter
    - graphics.py是Tkinter的一层包装，更适合新程序员
    
4.2 对象的目标
    - 面向对象开发的基本思想：将一个复杂的系统视为一些较简单"对象"的交互
        - 对象让数据与操作相结合。
        - 对象通过彼此发送消息来交互。(对象响应的信息集称为对象的"方法")
        - 消息就是请求，让对象执行它的一个操作。
        - 对象可以引用其他对象。
        
4.3 简单图形编程
    - 两种文件导入方式
        - import graphics；win=graphics.GraphWin()
        - from graphics import *；win = GraphWin()
            - from语句允许从库模块加载特定的定义，可列出要导入定义的名称，也可使用星号导入模块中定义的所有内容
            - 导入的命令可直接使用，而无需使用模块名称前缀
    - 图形窗口为像素的集合，通过控制每个像素的颜色，控制窗口显示的内容
"""

from graphics import *

win = GraphWin()
# 创建一个x=50，y=60的点
p = Point(50, 60)
# 将该点画在窗口上
p.draw(win)
p2 = Point(140, 100)
p2.draw(win)
win.close()

# 绘制图形到GraphWin中
win = GraphWin('Shapes')
# Draw a red circle centered at point (100,100) with radius 30
center = Point(100, 100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)
# Put a textual label in the center of the circle
label = Text(center, "Red Circle")
label.draw(win)
# Draw a square using a Rectangle object
rect = Rectangle(Point(30, 30), Point(70, 70))
rect.draw(win)
# Draw a line segment using a Line object
line = Line(Point(20, 30), Point(180, 165))
line.draw(win)
# Draw an oval using the Oval object
oval = Oval(Point(20, 120), Point(180, 199))
oval.draw(win)
win.close()

"""
4.4 使用图形对象
    - 类与对象
        - 类：描述了实例将具有的属性
        - 对象：是某个类的实例
    - 构造函数：<class-name> (<param1> , <param2> , ...)
    - 对象方法的调用：<object>.<method-name>(<param1>,<param2>, ...)
    
"""

# Incorrect way to create two circles，两个变量引用同一个对象称为"别名"
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = leftEye
rightEye.move(20, 0)

# Correct way to create two circles use clone
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = leftEye.clone()
rightEye.move(20, 0)

leftEye.clone()
rightEye.clone()

"""
4.5 绘制终值
    - 图形：提供数据的可视化表示
        - 在由坐标确定的像素点处绘制指定对象
"""


# 画出投资增长图
def drawInvestment1():
    print("This program plots the growth of a 10-year investment.")
    principal = float(input("Enter the initial principal:"))
    apr = float(input("Enter the initial apr:"))
    # create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), '0.0K').draw(win)
    Text(Point(20, 180), '2.5K').draw(win)
    Text(Point(20, 130), '5.0K').draw(win)
    Text(Point(20, 80), '7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)
    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))  # 从（40，230）到（65，230-principal*0.02）绘制一个矩形
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    # Draw bars for successive years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    # 在程序结束时添加一个输入语句，让其暂停，给用户一个读取结果的机会
    input("Press the <Enter> key to quit.")
    win.close()


# drawInvestment1()

"""
4.6 选择坐标
    - 设计终值图形程序：将真实世界问题的值变成窗口坐标（坐标变换）
        - 创建GraphWin时，可用setCoords为窗口指定坐标系，分别指定左下角和右上角坐标的四个参数，从而避免在坐标系之间显示转换
        - 进行图形编程时，应考虑选择一个坐标系，这将使实现更简单
"""

# 将窗口分为九个正方形
win = GraphWin("Tic-Tac-Toe")  # 默认为200*200
# 不借助计算像素点位置的方式来确定需画线的像素值，而是构造坐标系来完成
win.setCoords(0.0, 0.0, 3.0, 3.0)
Line(Point(1, 0), Point(1, 3)).draw(win)
Line(Point(2, 0), Point(2, 3)).draw(win)
Line(Point(0, 1), Point(3, 1)).draw(win)
Line(Point(0, 2), Point(3, 2)).draw(win)
win.close()


# 借助这种方法，简化图形终值程序
def drawInvestment2():
    print("This program plots the growth of a 10-year investment.")
    principal = float(input("Enter the initial principal:"))
    apr = float(input("Enter the initial apr:"))
    # create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), '0.0K').draw(win)
    Text(Point(-1, 2500), '2.5K').draw(win)
    Text(Point(-1, 5000), '5.0K').draw(win)
    Text(Point(-1, 7500), '7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)
    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    # Draw bars for successive years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    # 在程序结束时添加一个输入语句，让其暂停，给用户一个读取结果的机会
    input("Press the <Enter> key to quit.")
    win.close()


# drawInvestment2()


"""
4.7 交互式图形
    - 事件驱动编程
        - 用户点击按钮，从菜单中选择菜单项，并在屏幕文本框中输入信息与应用交互
    4.7.1 获取鼠标点击
        - 在GraphWin上调用getMouse()函数时，程序会暂停，并等待用户在图形窗口中某处单击鼠标，返回Point对象
    4.7.2 处理文本输入
        - 在GraphWin上调用getKey()函数时，返回字符串对象
        - GraphWin提供的Entry对象为可编辑的文本框
"""


# 允许用户通过点击图形窗口中的三个点来绘制一个三角形
def drawByUser():
    win = GraphWin()
    win.setCoords(0, 0, 10, 10)
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

    message.setText("Click anywhere to quit.")
    win.getMouse()


# drawByUser()

# 绘制GUI实现温度转换
def celsiusConverter():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    # draw the interface
    Text(Point(1, 3), "Celsius Temperature:").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature:").draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25, 1), "")
    outputText.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
    # wait for a mouse click
    win.getMouse()
    # convert input
    celsius = float(inputText.getText())
    fahrenheit = 9.0 / 5.0 * celsius + 32
    # display output and change button
    outputText.setText(round(fahrenheit, 2))
    button.setText("Quit")
    # wait for click and then quit
    win.getMouse()
    win.close()


# celsiusConverter()


# 在程序结束时添加一个输入语句，让其暂停，给用户一个读取结果的机会
input("Press the <Enter> key to quit.")
