"""
伴随文件：Python有时会在存储模块文件的文件夹中创建另一个名为pycache的文件夹，这里是Python存储伴随文件的地方，伴随文件的扩展名为.pyc


混沌：若输入中的非常小的变化导致结果的大变化，让它们看起来是随机的或不可预测的，则该数学模型被称为混沌。

"""


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
    input("Press the <Enter> key to quit.")  # 在程序结束时添加一个输入语句，让其暂停，给用户一个读取结果的机会


main()

"""
This program illustrates a chaotic function
Enter a number between 0 and 1:.25
0.73125
0.76644140625
0.6981350104385375
0.8218958187902304
0.5708940191969317
0.9553987483642099
0.166186721954413
0.5404179120617926
0.9686289302998042
0.11850901017563877
"""
