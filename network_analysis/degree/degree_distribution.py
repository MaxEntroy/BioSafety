#-*-coding:utf-8
import traceback
from matplotlib import pyplot as plt

"""
函数名:load_data
功能:加载度分布结果数据集
@input_path:度分布结果数据集路径
@X:度的值列表
@Y:相应度的节点个数
"""
def load_data(input_path):
    try:
        cnt = 0
        X = []
        Y = []

        infile = open(input_path, "r")
        for line in infile:
            line = line.rstrip('\n')
            value = int(line)
            X.append(cnt)
            Y.append(value)

            cnt += 1
        infile.close()
        return X,Y

    except Exception,e:
        print traceback.print_exc()

"""
函数名:draw_degree_distribution
功能:画度分布
@X:度的值列表
@Y:相应度的节点个数
"""
def draw_degree_distribution(X, Y):
    try:

        plt.subplot(1,1,1)
        plt.scatter(X,Y, s=50, label="degree")
        plt.xlabel("Degree")
        plt.ylabel("Number_of_vertices")
        plt.title("Degree distribution")
        plt.show()


        plt.subplot(1,1,1)
        plt.xlabel("Degree")
        #plt.ylabel("Number_of_vertices")
        plt.ylabel("Probablity")
        Y_FIX = [y / float(sum(Y)) for y in Y]
        #plt.loglog(X, Y_FIX, color="blue", marker='o', linewidth=2)
        plt.plot(X, Y_FIX, color="blue", linewidth=2)
        plt.title("Degree distribution")
        plt.show()
    except Exception,e:
        print traceback.print_exc()

if __name__ == '__main__':
    INPUT_PATH = "../../../output/network_analysis/degree_distribution.txt"
    X, Y = load_data(INPUT_PATH)
    draw_degree_distribution(X, Y)