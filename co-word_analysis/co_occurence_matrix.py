#-*- coding:utf-8
import traceback
from preprocess import get_all_file
from math import sqrt

"""
函数名:check(u, v, feature_set_list)
功能:计算共词对(u,v)的共现次数
@u:单词u
@v:单词v
@feature_set_list:特征向量集合
@cnt:共现次数
"""
def check(u, v, feature_set_list):
    cnt = 0
    for feature_set in feature_set_list:
        if u in feature_set and v in feature_set:
            cnt += 1
    return cnt

"""
函数名:cal_co_occurence_matrix
功能:计算共现矩阵
@feature_input_path:特征根目录路径
@high_freq_word_intput_path:高频词路径
@output_path:共现矩阵路径
"""
def cal_co_occurence_matrix(feature_input_path, high_freq_word_intput_path, output_path):
    try:

        # 获取所有特征列表，存储在集合中
        _, file_path_list = get_all_file(feature_input_path)
        file_path_list.sort()

        feature_set_list = [] # 每一篇文章的mesh列表是一个feature，用它创建一个feature_set，所有的特征存储在feature_set_list
        for file_path in file_path_list:

            infile = open(file_path, "r")

            for line in infile:
                feature = line.rstrip('\n').split(',')
                feature_set = set(feature)
                feature_set_list.append(feature_set)

            infile.close()

        # 获取高频词
        high_freq_word_list = []
        infile = open(high_freq_word_intput_path, "r")
        for line in infile:
            line = line.rstrip('\n').split(',')
            word = line[0]
            high_freq_word_list.append(word)
        infile.close()

        # 构建共词矩阵
        co_occurence_matrix = []
        for u in high_freq_word_list:
            vector = []
            for v in high_freq_word_list:
                co_occurence_cnt = check(u, v, feature_set_list)
                vector.append(co_occurence_cnt)
            co_occurence_matrix.append(vector)

        # 写回文件
        outfile = open(output_path, "w")
        for row in co_occurence_matrix:

            line = ""
            for item in row:
                line = line + str(item) + ' '
            line = line.rstrip(' ')
            outfile.write(line + '\n')

        outfile.close()

    except Exception,e:
        print traceback.print_exc()

"""
函数名:ochiai_similarity(u, v, feature_set_list, word_counter)
功能:计算共词对(u,v)的ochiai_similarity
@u:单词u
@v:单词v
@feature_set_list:特征向量集合
@word_counter: 高频词-次数字典
@ochiai_index: 词对(u,v)的ochiai系数
"""
def ochiai_similarity(u, v, feature_set_list, word_counter):
    cnt_u_and_v = 0
    for feature_set in feature_set_list:
        if u in feature_set and v in feature_set:
            cnt_u_and_v += 1

    cnt_u = word_counter[u]
    cnt_v = word_counter[v]
    ochiai_index = 1.0 * cnt_u_and_v / sqrt(cnt_u) / sqrt(cnt_v)
    return ochiai_index

"""
函数名:cal_co_occurence_matrix_ochiai
功能:计算用ochiai系数归一化之后的共现矩阵
@feature_input_path:特征根目录路径
@high_freq_word_intput_path:高频词路径
@output_path:共现矩阵路径
"""
def cal_co_occurence_matrix_ochiai(feature_input_path, high_freq_word_intput_path, output_path):
    try:

        # 获取所有特征列表，存储在集合中
        _, file_path_list = get_all_file(feature_input_path)
        file_path_list.sort()

        feature_set_list = [] # 每一篇文章的mesh列表是一个feature，用它创建一个feature_set，所有的特征存储在feature_set_list
        for file_path in file_path_list:

            infile = open(file_path, "r")

            for line in infile:
                feature = line.rstrip('\n').split(',')
                feature_set = set(feature)
                feature_set_list.append(feature_set)

            infile.close()

        # 获取高频词
        high_freq_word_list = []
        word_counter = {}
        infile = open(high_freq_word_intput_path, "r")
        for line in infile:
            line = line.rstrip('\n').split(',')

            word = line[0]
            word_cnt = int(line[1])

            high_freq_word_list.append(word)
            word_counter[word] = word_cnt

        infile.close()

        # 构建共词矩阵
        co_occurence_matrix = []
        for u in high_freq_word_list:
            vector = []
            for v in high_freq_word_list:
                ochiai_index = ochiai_similarity(u, v, feature_set_list, word_counter)
                vector.append(ochiai_index)
            co_occurence_matrix.append(vector)

        # 写回文件
        outfile = open(output_path, "w")
        for row in co_occurence_matrix:

            line = ""
            for item in row:
                line = line + str(item) + ' '
            line = line.rstrip(' ')
            outfile.write(line + '\n')

        outfile.close()

    except Exception,e:
        print traceback.print_exc()

if __name__ == '__main__':
    FEATURE_INPUT_PATH = "../../output/feature_list/"
    HIGH_FREQ_WORD_INPUT_PATH = "../../output/word_count/high_freq_word_fix1.csv"
    OUTPUT_PATH = "../../output/co_occurence_matrix/co_occurence_matrix_ochiai.dat"
    cal_co_occurence_matrix_ochiai(FEATURE_INPUT_PATH, HIGH_FREQ_WORD_INPUT_PATH, OUTPUT_PATH)
