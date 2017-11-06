#-*- coding: utf-8
import traceback

"""
函数名:get_name_str
功能:主要是为了生成R中脚本NAMES
@input_path:输入路径
@N:高频词个数
@output_path:输出路径
"""
def get_name_str( input_path, N, output_path ):
    try:

        cnt = 0
        name_str = ""

        infile = open(input_path, "r")
        for line in infile:
            line = line.rstrip('\n').split(',')
            word = line[0]

            word = '''"''' + word + '''"'''+','
            name_str += word

            cnt += 1
            if(cnt == N):
                break

        infile.close()
        name_str = name_str.rstrip(',')
        name_str = "c" + '(' + name_str + ')'

        outfile = open(OUTPUT_PATH, "w")
        outfile.write(name_str)
        outfile.close()

    except Exception,e:
        print traceback.print_exc()
if __name__ == '__main__':
    INPUT_PATH = "../../output/word_count/high_freq_word_fix.csv"
    N = 68
    OUTPUT_PATH = "../../output/name_str/name_str.txt"
    get_name_str(INPUT_PATH, N, OUTPUT_PATH)