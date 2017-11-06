#-*- coding:utf-8

import traceback
from preprocess import get_all_file

"""
函数名:get_total_mesh_number
功能:统计所有mesh特征的数量，这个函数是我后写的
@input_path:输入文件，特征目录
@output_path:输出文件，存储统计词频值于词频为1的记录个数
"""

def get_total_mesh_number(input_path, cur_number):
    try:

        total = 0
        infile = open(input_path, "r")
        for line in infile:
            line = line.rstrip('\n').split(',')
            total += len(line)
        infile.close()

        return cur_number + total
    except Exception, e:
        print traceback.print_exc()

if __name__ == '__main__':
    # get xml file from 2006 to 2015

    ROOT_PATH = "../../output/feature_list/"
    #ROOT_PATH = "../../output/feature_author_list/"
    _, file_list = get_all_file(ROOT_PATH)
    file_list.sort()

    cur_total = 0
    for file_path in file_list:
        cur_total = get_total_mesh_number(file_path, cur_total)

    print "total mesh number is ", cur_total