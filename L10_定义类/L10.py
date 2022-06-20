"""
@Author : zhang
@create : 2022/6/9 17:10
"""
"""
10.1 对象的快速复习
    - 函数：使程序的"计算"结构化；对象：使程序使用的"数据"结构化
    - 一个对象包括：
        1. 一组相关的信息
        2. 操作这些信息的一组操作
10.2 示例程序：炮弹
    - 常规
    - 自顶向下——函数
    - 基于对象，构建可以代表抛体的类
        - 针对具有复杂行为的真实世界对象进行建模
10.3 定义新类
    - 类定义的形式：class <class-name>:<method-definitions>
    - 访问实例变量：<object>.<instance-var>
    - __init__：对象构造方法（构造函数），为对象的实例变量提供初始值；在类的外部，构造方法由类名来调用
    - self：每个方法定义的第一个参数。
        - self的实际参数是应用该方法的对象
        - 利用点表示法，self参数可用于访问对象的属性
10.4 用类处理数据
    - 用对象描述记录——一组描述人或事的信息
10.5 对象和封装
    - 10.5.1 封装：隐藏实现细节，只需关心对象可执行的操作
        - 允许独立地修改和改进类，而不用担心"破坏"程序的其他部分
    - 10.5.2 将类放入模块中
        - 将定义好的类变为模块文件，可以在不同的程序中使用
    - 10.5.3 模块文档
        - 文档字符串（docstring）：在模块、类或函数的第一行插入一个简单的字符串字面量，为该组件提供文档。
            - 文档字符串实际在执行时被放在名为__doc__的属性中
    - 10.5.4 使用多个模块
        - 当Python首次导入一个给定的模块时，他将创建一个包含模块中定义的所有内容的模块对象（命名空间）。
            - 如果模块导入成功（没有语法错误），则后续导入不会重新加载该模块，只会创建对已有模块的更多引用。
            - 即使某个模块已被更改（其源文件已被编辑），将其重新导入到正在进行的交互式的会话中也不会得到更新的版本
        - 可以使用标准库中imp模块的函数reload(<module>)来交互地替代模块对象
            - 但对于当前会话中已经引用的模块旧版本的对象，重新加载模块不会更改任何标识符的值
        - 避免混乱的方法：当模块被修改时，开启新的交互式会话
            - 在IDLE中，当选择run module时，会让shell重启
10.6 控件
    - 对象的用途——图形用户界面（GUI）的设计
    - 可通过定义合适的类来构建创新的GUI控件
10.7 炮弹动画
"""

from math import pi, sin, cos, radians


# chall1.py
def chall1():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))
    # convert angle to radians
    theta = radians(angle)
    # set the initial position and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    # loop until the ball hits the ground
    while ypos >= 0:
        # calculate position and velocity in time seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1) / 2.0
        yvel = yvel1
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))


# chall1()


#   Simulation of the flight of a cannonball (or other projectile)
#   This version uses functional (top-down) composition.
def cball2():
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0:
        xpos, ypos, yvel = updateCannonBall(time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))


def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t


def getXYComponents(vel, angle):
    radians = (angle * pi) / 180.0
    x = vel * cos(radians)
    y = vel * sin(radians)
    return x, y


def updateCannonBall(time, xpos, ypos, xvel, yvel):
    xpos = xpos + time * xvel
    yvel1 = yvel - 9.8 * time
    ypos = ypos + time * (yvel + yvel1) / 2.0
    return xpos, ypos, yvel1


# cball2()


# chall3.py
# Projectile是一个代表抛体的类，用来对具体情形建模
class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time  # 使用yvel1作为临时变量
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1  # 将yvel1存储到对象中，从而保存该新值

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos


def chall3():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.xpos))


# chall3()


# Program to find student with highest GPA
# 新建Student类描述学生记录信息
class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours


def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")  # 以制表符划分学生属性
    return Student(name, hours, qpoints)


def gpa():
    # open the input file for reading
    filename = input("Enter name the grade file: ")
    infile = open(filename, 'r')
    # set best to the record for the first student in the file
    best = makeStudent(infile.readline())
    # process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        s = makeStudent(line)
        # if this student is best so far, remember it.
        if s.gpa() > best.gpa():
            best = s
    infile.close()
    # print information about the best student
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())


# gpa()

# cball4.py
from projectile import Projectile


# print(Projectile.__doc__) 显示该模块的文档字符串
def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t


def cball4():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))


# cball4()


# roller.py
# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView.

from random import randrange
from graphics import GraphWin, Point
from button import Button
from dieview import DieView


def roller():
    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5, 1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()


# roller()

