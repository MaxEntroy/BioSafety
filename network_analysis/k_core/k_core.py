#-*- coding:utf-8
import traceback
from matplotlib import pyplot as plt


"""
函数名:get_data
功能:加载K_core分布结果数据集
@input_path:k_core分布结果数据集路径
@X:k_core的值列表
@Y:相应k_core的节点个数(频数)
"""
def get_data(input_path):
    try:
        X = []
        Y = []

        cnt = 0
        infile = open(input_path, "r")
        for line in infile:
            line = line.rstrip('\n')
            y = int(line)
            X.append(cnt)
            Y.append(y)
            cnt += 1


        infile.close()

        '''
        data = []
        for idx, item in enumerate(Y):
            for cnt in range(item):
                data.append(idx)
        return data
        '''
        return X, Y
    except Exception,e:
        print traceback.print_exc()

def get_cumulative_distribution(X, Y):
    try:
        cumulative = []
        total = sum(Y)

        cur = 0
        for item in Y:
            cur += item
            cumulative.append(1.0*cur/total)

        return X, cumulative
    except Exception,e:
        print traceback.print_exc()

"""
函数名:draw_k_core_distribution
功能:画k_core分布
@X:k_core的值列表
@Y:相应k_core的节点个数(频数)
"""
def draw_k_core_distribution( X, Y ):
    try:
        plt.subplot(1,1,1)
        Y_FIX = [y / float(sum(Y)) for y in Y]
        plt.bar(X, Y_FIX)
        plt.xlim([-1, 30])
        #plt.xticks(X)
        plt.xlabel("k_core")
        plt.ylabel("frequency")
        plt.title("K_core distribution ")
        plt.show()
    except Exception,e:
        print traceback.print_exc()

"""
函数名:draw_cumulate_distribution
功能:画k_core累计分布
@X:k_core的值列表
@CUR:相应k_core的累积节点个数(频数)
"""
def draw_cumulate_distribution( X, CUR ):
    try:

        plt.subplot(1,1,1)
        plt.plot(X, CUR, 'bo-', markersize=10)

        plt.xlabel("k_core")
        plt.ylabel("CDF")
        plt.title("Cumulative distribution")
        plt.show()
    except Exception,e:
        print traceback.print_exc()

if __name__ == '__main__':
    #INPUT_PATH = "../../../output/network_analysis/k_core_distribution.txt"
    INPUT_PATH = "../../../output/cw/k_core_distribution.txt"
    X,Y = get_data(INPUT_PATH)
    draw_k_core_distribution(X, Y)
    X, CUMU = get_cumulative_distribution(X, Y)
    #print X
    #print CUMU
    draw_cumulate_distribution(X, CUMU)
