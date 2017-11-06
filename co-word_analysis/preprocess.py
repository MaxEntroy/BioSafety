#-*- coding:utf-8
import traceback
import os
import xml.etree.ElementTree as et

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
函数名:get_feature
功能:解析xml_path所指向的目标文件，提取改文件当中每一篇文章的mesh词特征
@xml_path:xml文件路径
@feature_list:返回所有文章的mesh特征列表
"""
def get_feature( xml_path ):
    try:
        tree = et.parse(xml_path)
        root = tree.getroot()

        feature_list = []

        for article in root:
            medline_citation = article.findall("MedlineCitation")[0]
            mesh_heading_list_label = medline_citation.findall("MeshHeadingList")[0]
            mesh_heading_list = mesh_heading_list_label.findall("MeshHeading")

            feature = []
            for mesh_heading in mesh_heading_list:
                descriptor = mesh_heading.find("DescriptorName")
                feature.append( str(descriptor.text) )

            feature_list.append(feature)

        return feature_list

    except Exception,e:
        print traceback.print_exc()

"""
函数名:save_feature
功能:将获取的特征保存本地
@save_path:保存文件路径
@feature_list:特征列表
"""
def save_feature(save_path, feature_list):
    try:
        outfile = open(save_path,"w")

        for feature in feature_list:
            str = ""
            for item in feature:
                str = str + item + ','
            str = str.rstrip(',')

            outfile.write(str + '\n')

        outfile.close()

    except Exception,e:
        print traceback.print_exc()

"""
函数名:preprocess
功能:提取特征保存至本地
"""
def preprocess():
    try:
        # get xml file from 2006 to 2015
        ROOT_PATH = "../../data/2006-2015/"
        _, file_list = get_all_file(ROOT_PATH)
        file_list.sort()

        # get feature list and save to local file
        save_path_header = "../../output/feature_list/"
        year = 2006
        for xml_path in file_list:

            feature_list = get_feature(xml_path)
            save_path = save_path_header + "feature_" + str(year) + ".csv"
            save_feature( save_path ,feature_list)

            year += 1

    except Exception,e:
        print traceback.print_exc()


if __name__ == '__main__':
    preprocess()