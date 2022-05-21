"""
3.1 数值数据类型
      整数余与取余的关系：a=(a//b)(b)+(a%b)，
    
"""
print(type(3), type(3.14),  # 输出任何值的数据类型
      abs(-5),  # 取绝对值
      10 / 3, 10 // 3,  # 浮点除（总是返回一个浮点数）与整数除，结果的数据类型取决于操作数的类型
      2 ** 3,  # 指数
      10 % 3)  # 取余

"""
3.2 类型转换与舍入
      - 隐式类型转换
            - 在"混合类型表达式"中，Python会自动将int转为浮点数，并执行浮点运算以产生浮点数结果。
      - 显式类型转换
            - 强制转换：int（丢弃浮点值的小数部分，该值将被截断）和float函数
            - 四舍五入：round函数，结果为int值
            - 将浮点值舍入为另一个函数：指定round函数的第二个参数，确定小数点后的数字位数
            - 将数字字符串转为数字：int和float函数（替代eval从用户获取数字数据的另一种方式）
"""
print("5*0.2 =", 5 * 0.2, ",int(4.9) =", int(4.9), ",round(4.9) =", round(4.9),
      ",round(3.14159265358,2) =", round(3.14159265358, 2),
      ",int(\"32\") =", int("32"), ",float(\"9.8\") =", float(9.8))

print("Please enter the count of cion.")
dimes = int(input("Dimes:"))  # 在input语句中使用int而不是eval，可以确保用户只能输入有效的数字，避免代码注入攻击的风险

"""
3.3 使用math库
      - 库是一个模块，包含了一些有用定义
      - 常用库函数：pi，e，ln，log10，exp，ceil，floor
"""

import math

print("math.sqrt(26)=", math.sqrt(26))

"""
3.4 累计结果：阶乘
      - 借助range函数产生数字序列
            - range(n):生成数字序列0～n-1 
            - range(start,n):生成数字序列start～n-1
            - range(start,n,step):生成数字序列start～n-1，其中step为数字之间的增量
"""
print("list(range(10)):", list(range(10)), ",list(range(5,10)):", list(range(5, 10)),
      ",list(range(5,10,8)): ", list(range(5, 10, 3)))


# def getFactorial1():
#     n = int(input("Please enter a whole number:"))
#     fact = 1
#     for factor in range(n, 1, -1):
#         fact = fact * factor
#     print("The factorial of", n, "is", fact)

def getFactorial():
    n = int(input("Please enter a whole number:"))
    fact = n
    for factor in range(1, n, 1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

getFactorial()


"""
3.5 计算机算术的局限性
    - 因为底层数字是二进制的，只有2的幂的分数可以被精确表示
    - Python的int不是固定大小，而是扩展到适应任何值，唯一的限制是计算机的内存容量
"""