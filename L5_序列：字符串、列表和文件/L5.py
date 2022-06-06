"""
@Author : zhang
@create : 2022/5/23 17:15
"""
"""
5.1 字符串数据类型
    - ""和''括起来的都是string类型
    - 通过索引(0~n-1)对单个字符进行操作：<string>[<expr>]
        - 索引返回对象的是字符串
        - 可由负索引获取字符串的最后一个字符
    - 字符串的截取（切片）：<string>[<start>:<end>]（切片产生从start直到（end-1）位置的字串）
            - 若任何一个表达式缺失，字符串的开始和结束都是假定的默认值
    - 连接（+）：将两个字符串粘合在一起构建字符串
    - 重复（*）：将字符串与自身连接构建字符串
    - len:返回字符串长度
"""

# input函数返回用户键入的任何字符串对象
firstName = input("Please enter your name:")
print("hello", firstName)
# 索引
print(firstName[0], firstName[2], firstName[-1])
# 切片
print(firstName[1:3], firstName[:])
# 连接与重复
print("hello" + "world!", firstName * 2, len(firstName))
# 遍历字符串
for ch in firstName:
    print(ch, end=" ")
print()

"""
5.2 简单字符串处理
"""


# generate usernames
def generateName():
    # 输出该提示后，多输出一个空行
    print("This program generates computer usernames.\n")
    first = input("enter your first name:")
    last = input("enter your last name:")
    # concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[:7]
    print("your username is", uname)


# generateName()

# print the abbreviation of a month,given its number
# 这里没有用判断，而是根据用户输入的数字适当的位置切出子字符(仅当字串都有相同的长度时才有效)
def printMonth1():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = int(input("enter a month number:"))
    pos = (n - 1) * 3
    monthAbbrev = months[pos:pos + 3]
    print("The month abbreviation is", monthAbbrev)


# printMonth1()


"""
5.3 列表作为序列
    - 字符串总为字符序列，列表可以是任何对象的序列（亦可混合）
    - 列表的索引：0～n-1
    - 列表中项的值可由赋值语句修改（列表是可变的），字符串不能在指定位置改变
    - 字符串和列表都是对象，都自带方法
    - append方法：用于在列表尾添加一项
"""
mList = ["hello", 1, "world", 2]
mList[2] = "change"
print(mList)
squares = []  # 表示空列表
for x in range(1, 101):  # 创建前100个自然数的平方的列表
    squares.append(x * x)
print(squares)


# 使用列表输出月份缩写
def printMonth2():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    n = int(input("enter a month number:"))
    print("The month abbreviation is", months[n - 1])


# printMonth2()


"""
5.4 字符串表示和消息编码
    - 字符串表示
        - ASCII（美国信息交换标准代码）
        - Unicode标准
            - 空格字符也有相应的Unicode编码，值为32
    - ord()函数和chr()函数，允许字符和数值之间切换
"""
print(ord("a"), chr(97))


# a program to convert a textual message into a sequence of numbers, utilizing the underlying Unicode encoding
def encoder():
    message = input("Please enter the message to ender:")
    print("\nHere are the Unicode codes:")
    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")


# encoder()

"""
5.5 字符串方法
    - split方法，默认遇到空格拆分字符串，返回值为列表
        - 可指定拆分字符作为参数
"""
myString = "Hello, string methods!"
print(myString.split())
print("32,34,32".split(","))  # 指定按照空格拆分
# 不用eval从用户获得多个输出
coords = input("Enter the point coordinates(x,y):").split(",")
x, y = float(coords[0]), float(coords[1])


# a program to convert a sequence of Unicode numbers into a string to text.
def decode():
    inString = input("Please enter the Unicode-encoded message:")
    chars = []  # 利用列表的append方法进行追加而不是字符串的连接操作（因为连接操作要先复制字符串，很慢）
    for numStr in inString.split():
        codeNum = int(numStr)  # convert digits to a number
        chars.append(chr(codeNum))  # accumulate new character
    message = "".join(chars)  # join操作将列表连接到字符串中
    print("\nThe decoded message is:", message)


# decode()


"""
5.7 从编码到加密
    - 替换密码：原始消息的每个明文被来自"密码字母表"的相应符号替换，生成"密文"
        - 由于每个字母总是相同的符号编码，因此解码器可以使用关于各种字母频率的统计信息和试错法测试来发现原始信息
    - 现代加密方法——密钥：现将信息转为数字，再用数学算法将这些数字转换为其他数字
        - 私钥（共享密钥）：通信双方知道，对外界保密
        - 公钥：加密密钥公开，解密密钥私有
        
5.8 输入/输出作为字符串操作
    - Python中的类型转换函数
        - float(<expr>)：将expr转换为浮点值
        - int(<expr>)：将expr转换为整数值
        - str(<expr>)：返回expr的字符串表示形式
        - eval(<string>)：将字符串作为表达式求值
    - 字符串格式化函数——format
        - 插槽说明总是具有一下形式：{<index>:<format-specifier>}
        - <宽度>.<精度><类型>
        - 左、右和中心对齐：<、>、^
"""


# convert a date in from "mm/dd/yyyy" to "month day, year"
def convertDate():
    dateStr = input("Enter a date(mm/dd/yyyy):")
    monthStr, dayStr, yearStr = dateStr.split("/")
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monStr = months[int(monthStr) - 1]
    print("The converted date is:", monStr, dayStr + ",", yearStr)


# convertDate()

# 格式说明符
print("hello {0} {1} , you may won ${2}".format("Mr.", "Smith", 1000))  # hello Mr. Smith , you may won $1000
print("compare {0} and {0:0.20}".format(3.14))  # compare 3.14 and 3.1400000000000001243
print("left justification:{0:<5}".format("hi")
      , "\nright justification:{0:>5}".format("hi")
      , "\ncentered justification:{0:^5}".format("hi"))


# a better calculate
# 因为计算机不能准确表示浮点数，故将货币值转为int型记录
def betterCal():
    print("Change Counter\n")
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies
    # 美分的值用格式说明符"0>2"打印，前面的调整字符0告诉python用0来填充字符（如果必要）而不是空格。
    # 这确保10美元5美分打印出来为10.05而不是10.5
    print("The total value of your change is ${0}.{1:0>2}"
          .format(total // 100, total % 100))


# betterCal()

"""
5.9 文件处理
    - 文件的输入和输出就是另一种形式的字符串处理
    5.9.2 文件处理
        - 用编辑语言处理文件：通过可以操作文件的对象直接访问文件本身
        - 应用程序处理文件：将文件读取到RAM中，真正改变的是内存中的数据而不是文件本身
        - Python提供的文件对象infile
            - 创建与文件相对应的文件对象：<variable>=open(<name>,<mode>)
                - mode可选字符"r"或"w"
            — <file>.read()将文件的全部剩余内容作为单个（可能是大的、多行的）字符串返回
            - <file>.readline()返回文件的下一行。即所有文本，直到并包括下一个换行符
            - <file>.readlines()返回文件中剩余行的列表。每个列表项都是一行，包括结尾处的换行符
    5.9.4 文件对话框（可选）
        - 标准Python安装中的tkinter GUI库提供了一些函数用于创建获取文件名的对话框(避免手动输入)
            - askopenfilename函数：询问用户打开文件的名称
            - asksaveasfilename函数：保存文件
    
"""
# 读取文件并输出其内容
infile = open("../main.py", "r")
data = infile.read()
print(data)

# 打印文件的前5行
for i in range(5):
    line = infile.readline()
    print(line[:-1])  # 利用切片去掉行尾的换行符

# Python将文件本身视为一系列行
for line in infile:
    # process the line here
    print(line, end=" ")  # 打印整行

# 打开用于写入的文件
outfile = open("../main.py", "w")
# 使用print文件写入
print("# 写入文件测试", outfile)


# a program to create a file of username in batch mode.
# 一个函数同时操作两个文件
def createName():
    # get the file names
    infileName = input("What file are the names in?")
    outfileName = input("What file should the username go in?")
    # open the file
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the username
        uname = (first[0] + last[:7]).lower()  # 确保用户名全是小写
        # write it to the output file
        print(uname, file=outfile)
    # close both files
    infile.close()
    outfile.close()


# createName()

# from语句允许从库模块加载特定的定义，可列出要导入定义的名称，也可使用星号导入模块中定义的所有内容
# 导入的命令可直接使用，而无需使用模块名称前缀
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

infilename = askopenfilename()
outfilename = asksaveasfilename()
