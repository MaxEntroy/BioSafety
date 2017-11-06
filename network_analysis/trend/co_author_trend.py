#-*- coding:utf-8
import traceback
from preprocess import get_all_file
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


"""
函数名:cal_co_author_ratio_and_nums_of_author_per_article
功能:计算每年的文章合著率以及每篇的合著人数
@feature_list_path:特征路径
@output_path_ratio:合著率存储路径
@output_path_nums:合著人数存储路径
"""
def cal_co_author_ratio_and_nums_of_author_per_article(feature_list_path,
                                                       output_path_ratio,
                                                       output_path_nums):
    try:

        co_author_ratio_list = []
        nums_of_author_per_article_list = []

        _, file_list = get_all_file(feature_list_path)
        file_list.sort()

        for file_path in file_list:
            infile = open(file_path, "r")

            article_only_one_author_num = 0
            total_author_num = 0
            feature_list = []
            for line in infile:
                feature = line.rstrip('\n').split(',')
                feature_list.append(feature)

                author_num_per_article = len(feature)
                total_author_num += author_num_per_article

                if author_num_per_article == 1:
                    article_only_one_author_num += 1

            total_article_num = len(feature_list)

            infile.close()

            co_author_ratio = 1 - 1.0 * article_only_one_author_num / total_article_num
            num_of_author_per_article = 1.0 * total_author_num / total_article_num

            co_author_ratio_list.append(co_author_ratio)
            nums_of_author_per_article_list.append(num_of_author_per_article)

        outfile = open(output_path_ratio, "w")
        for ratio in co_author_ratio_list:
            outfile.write(str(ratio) + '\n')
        outfile.close()

        outfile = open(output_path_nums, "w")
        for nums in nums_of_author_per_article_list:
            outfile.write(str(nums) + '\n')
        outfile.close()

    except Exception,e:
        print traceback.print_exc()


if __name__ == '__main__':
    FEATUR_LIST_PATH = "../../output/feature_author_list/"
    OUTPUT_PATH_RATIO = "../../output/co_author_ratio/co_author_ratio.dat"
    OUTPUT_PATH_NUMS = "../../output/nums_per_article/nums_per_article.dat"

    cal_co_author_ratio_and_nums_of_author_per_article(FEATUR_LIST_PATH,
                                                       OUTPUT_PATH_RATIO,
                                                       OUTPUT_PATH_NUMS)