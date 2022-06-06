"""
@Author : zhang
@create : 2022/6/4 18:13
"""
"""
7.1 简单判断
    - 判断结构：允许程序针对不同的情况执行不同的序列
    - if<condition>:<body>
    7.1.3 条件程序执行
        - 无论何时导入模块，Python都会在该模块内部创建一个特殊的变量__name__，并为其分配一个表示模块名称的字符串。
            - import math; math.__name__=='math'
        - 如果模块被导入，那个模块中的代码将看到一个名为__name__的变量，其值是模块的名称。
        - 添加代码if __name__== '__main__':main()，保证调用程序时自动运行main，但若导入模块，就不会运行。
7.2 两路判断
    - if<condition>:<statements> else:<statements>
7.3 多路判断
    - if<condition1>:<case1 statements> elif<condition1>:<case2 statements>...else:<default statements>
7.4 异常处理
    - 在Python中，异常处理是通过类似于判断的特殊控制结构完成的
    - try:<body> expect <ErrorType>:<handler>
"""

import math


def celsiusToFahrenheit():
    celsius = float(input("What is the Celsius temperature?"))
    faulthandler = 9 / 5 * celsius + 32
    if faulthandler > 90:
        print("It's really hot out there.Be careful!")
    if faulthandler < 30:
        print("Brrrrr.Be sure to dress warmly!.")


# celsiusToFahrenheit()


def getRealRoots():
    print("This program finds the real solutions to a quadratic\n")
    a = float(input("Enter coefficient a:"))
    b = float(input("Enter coefficient b:"))
    c = float(input("Enter coefficient c:"))
    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real roots!")
    elif discrim == 0:
        root = (-b) / (2 * a)
        print("\nThere is a double root at:", root)
    else:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)


# getRealRoots()

def getRealRoots2():
    try:
        a = float(input("Enter coefficient a:"))
        b = float(input("Enter coefficient b:"))
        c = float(input("Enter coefficient c:"))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    except ValueError as excObj:  # 将该错误类型转换为一个字符串
        if str(excObj) == "math domain error":
            print("No real roots")
        else:
            print("\nThe equation has no real roots!")
    except:
        print("\nSomething went wrong, sorry!")
