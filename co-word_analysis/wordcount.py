#-*- coding:utf-8
import traceback
import os
from preprocess import get_all_file

"""
函数名:word_count
功能:统计特征的词频
@input_path:输入文件，特征目录
@output_path:输出文件，存储统计词频值于词频为1的记录个数
"""
def word_count( input_path, output_path ):
    try:

        _, file_list = get_all_file(input_path)
        file_list.sort()

        word_counter = {}

        for file_path in file_list:
            infile = open(file_path, "r")

            for line in infile:
                line = line.rstrip('\n').split(',')
                for word in line:
                    if word in word_counter:
                        word_counter[word] += 1
                    else:
                        word_counter[word] = 1

            infile.close()

        number_of_one = 0
        for key in word_counter:
            if word_counter[key] == 1:
                number_of_one += 1

        sorted_list = sorted(word_counter.items(), key=lambda item:item[1], reverse=True)

        outfile = open(output_path, "w")
        for aa in sorted_list:
            line = str(aa[0]) + ',' + str(aa[1])
            line = line.lstrip(' ')
            outfile.write(line + '\n')
        outfile.write("number of 1 : " + str(number_of_one) + '\n')
        outfile.close()

    except Exception,e:
        print traceback.print_exc()

"""
函数名:get_high_freq_record
功能:获取高频词记录
@input_path:输入文件，所有统计词频
@output_path:输出文件，保存高频统计词
@N:高频词于低频词的分界值
"""
def get_high_freq_record( input_path, output_path, N ):
    try:

        infile = open(input_path, "r")
        outfile = open(output_path, "w")

        for line in infile:
            new_line = line
            line = line.rstrip('\n').split(',')
            count = int(line[1])
            if count < N:
                break
            outfile.write(new_line)

        infile.close()
        outfile.close()

    except Exception,e:
        print traceback.print_exc()


if __name__ == '__main__':
    '''
    INPUT_PATH = "../../output/feature_list/"
    OUTPUT_PATH = "../../output/word_count/word_count_result.csv"
    word_count(INPUT_PATH, OUTPUT_PATH)
    '''

    INTPUT_PATH = "../../output/word_count/word_count_result.csv"
    OUTPUT_PATH = "../../output/word_count/high_freq_word.csv"
    N = 16
    get_high_freq_record(INTPUT_PATH, OUTPUT_PATH, N)