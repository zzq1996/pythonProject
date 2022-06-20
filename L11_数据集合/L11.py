"""
@Author : zhang
@create : 2022/6/15 14:36
"""
"""
11.1 示例问题：简单统计
    - 许多程序需要处理大量相似信息的集合（Python中称为列表，对应其他编程语言中的数组）
11.2 应用列表（stats.py）
    - Python列表是任意对象的可变序列，是存储为单个对象的一系列数据项
    - 通过索引访问列表中的数据项，通过切片访问子列表
    - 列表是可变的，单个数据项或整个切片可以通过赋值语句来替换
    - 列表的操作
        - 连接：<seq> + <seq>
        - 重复：<seq> * <int-exp>
        - 索引：<seq>[]
        - 长度：len(<seq>)
        - 切片：<seq>[:]
        - 迭代：for <var> in <seq>:
        - 成员检查（返回布尔值）：<expr> in <seq>
        - 添加元素x到列表末尾：<list>.append(x)
        - 对列表进行排序：<list>.sort()
        - 反转列表：<list>.reverse()
        - 返回x第一次出现的索引：<list>.index(x)
        - 在索引i处将x插入列表：<list>.insert(i,x)
        - 返回x在列表中出现的次数：<list>.count(x)
        - 删除列表中第一次出现的x：<list>.remove(x)
        - 删除列表中第i个元素并返回它的值：<list>.pop(i)
11.3 记录的列表（gpasort.py）
    - 将存储记录的集合用列表操作
    - 内置sort函数通过指定关键字参数key来确定排序列表时使用的键
11.4 用列表和类设计（dieview2.py）
    - 改进DieVie类的实现
11.5 案例分析：Python计算器（calc.pyw）
    - 创建界面
        - 显示界面由一个显示控件和一堆按钮组成
    - 用户交互
        - 通过一组操作控件的方法进行管理
11.6 案例研究：更好的炮弹动画（animation2.py）
11.7 无顺序集合
    - Python中表示集合的数据类型：列表（数组）、字典（键值对/映射）
        - 列表：从顺序集合中存储和检索项目
        - 字典：可变集合，实现从键到值的映射。多用于表示非顺序集合
    - 字典的操作
        - <key> in <dict>:返回字典中是否包含指定的键
        - <dict>.keys():返回键的序列
        - <dict>.values():返回值的序列
        - <dict>.items():返回键值对的序列（元组）
        - <dict>.get(<key>,<default>):如包含键key就返回他的值，否则返回default
        - del <dict>[<key>]:删除指定的条目
        - <dict>.clear():删除所有条目
        - for <var> in <dict>:循环遍历所有键
    
"""

passwd = {"key1": "pw1", "key2": "pw2", "key3": "pw3"}
print(passwd)
passwd["key1"] = "npw1"
print(passwd)


# wordfreq.py

def byFreq(pair):
    return pair[1]


def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.\n")

    # get the sequence of words from the file
    fname = input("File to analyze: ")
    text = open(fname, 'r').read()
    text = text.lower()  # 将所有单词转为小写
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(ch, ' ')
    words = text.split()

    # construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    # output analysis of n most frequent words.
    n = int(input("Output analysis of how many words? "))
    items = list(counts.items())
    items.sort()  # Python中的排序算法是稳定的，先按单词排序
    items.sort(key=byFreq, reverse=True)  # 再按词频排序，设置reserve使其从高到低排序
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))  # 单词在十五个空格中左对齐印刷，接着是在五个空格中右对齐的数字


if __name__ == '__main__':  main()
