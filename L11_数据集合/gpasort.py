# gpasort.py
#    A program to sort student information into GPA order.

from gpa import Student, makeStudent


def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students


def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()),
              file=outfile)  # 使用字符串格式化方法来生成相应的输出行，\t表示制表符
    outfile.close()


def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    data.sort(key=Student.gpa)  # 指定使用sort函数进行列表排序时使用的键
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)


if __name__ == '__main__':
    main()
