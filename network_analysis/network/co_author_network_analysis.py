#-*- coding:utf-8

import traceback
from MyGraph import*
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
函数名:get_all_file
功能:获取目录下的所有文件
@root_path:目标目录
@dir_list:返回目录文件
@file_list:返回非目录文件
"""
def get_all_file(root_path):
    try:

        # 获取该目录下所有文件
        all_files = os.listdir(root_path)

        # 获取目录文件 非目录文件
        dir_list = [root_path + file for file in all_files if os.path.isdir(root_path + file)]
        file_list = [root_path + file for file in all_files if os.path.isfile(root_path + file)]

        return dir_list, file_list

    except Exception, e:
        print traceback.print_exc()

"""
函数名:get_all_feature
功能:获取所有文章的作者特征，每篇文章的所有作者，作为一篇文章的特征
@feature_input_path:特征路径
@feature_list:所有特征列表
"""
def get_all_feature( feature_input_path ):
    try:

        _, file_path_list = get_all_file(feature_input_path)
        file_path_list.sort()

        feature_list = []
        for file_path in file_path_list:
            infile = open(file_path, "r")
            for line in infile:
                feature = line.rstrip('\n').split(',')
                feature_list.append(feature)
            infile.close()

        return feature_list
    except Exception,e:
        print traceback.print_exc()

"""
函数名:network_analysis
功能:对合著作者网络进行分析
@clique_list:特征集合
@output_path:网络输出路径
"""
def network_analysis(clique_list, output_path):
    try:

        # construct the graph according to the clique_list
        graph = MyGraph()
        graph.construct_graph(clique_list)
        graph.set_output_path(output_path)

        '''
        # 基本统计指标
        graph.cal_num_of_nodes()
        graph.cal_num_of_edges()

        #graph.cal_degree_distribution() 下面的这个版本是新版本，更好用
        graph.save_degree_distribution()
        graph.cal_density()
        graph.draw_graph("coauthored network")
        graph.cal_k_core_distribution()
        '''



        # 最大联通子图的性质
        graph.set_max_connected_component_subgraph()
        graph.draw_max_connected_component_subgraph()
        #graph.cal_average_shortest_path_length_in_max_connected_component_subgraph()
        #graph.cal_average_clustering_in_max_connected_component_subgraph()


        #graph.write_to_pajek_net1()


    except Exception,e:
        print traceback.print_exc()

if __name__ == '__main__':
    FEATURE_INPUT_PATH = "../../../output/feature_author_list/"
    OUTPUT_PATH = "../../../output/network_analysis/"

    feature_list = get_all_feature(FEATURE_INPUT_PATH)
    network_analysis(feature_list, OUTPUT_PATH)

