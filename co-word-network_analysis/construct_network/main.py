#-*- coding:utf-8 -*-
from XmlParser import*
from MyGraph import*

STOP_WORDS_PATH = "../file/stop_words.txt"

XML_PATH1 = "../data/PUBMED/LANCET/2006/lancet_2006_1570.xml"
XML_PATH2 = "../data/PUBMED/LANCET/2009/lancet_2009_1516.xml"
#OUTPUT_PATH1 = "../output/network_analysis/PUBMED/LANCET/2006/"
#OUTPUT_PATH2 = "../output/network_analysis/PUBMED/LANCET/2009/"
OUTPUT_PATH3 = "../output/src_output/edge.txt"

INPUT_PATH = "../data/src_input/citation.csv"
OUTPUT_PATH = "../output/src_output/"

# @xml_parser_obj:xml解析后的对象
# @OUTPUT_PATH:统计分析之后的输出路径
def statical_analysis( xml_parser_obj, OUTPUT_PATH ):
    try:
        xml_parser_obj.cal_word_occurence_in_article_abstract(OUTPUT_PATH)
        xml_parser_obj.cal_word_occurence_in_article_title(OUTPUT_PATH)

        print "[INFO]: statical_analysis is finished!"
    except Exception,e:
        print traceback.print_exc()

# @xml_parser_obj:xml解析后的对象
# @OUTPUT_PATH: 网络静态分析之后的输出路径
def author_collaboration_network_analysis( xml_parser_obj, OUTPUT_PATH ):
    try:

        # get the author clique list
        author_clique_list = xml_parser_obj.get_article_author()

        # construct the graph based on the author clique list
        graph = MyGraph()
        graph.construct_graph(author_clique_list)
        graph.set_output_path(OUTPUT_PATH)


        # calculate the statistics
        graph.cal_num_of_nodes()
        graph.cal_num_of_edges()

        graph.cal_degree_distribution()
        graph.cal_density()

        # the colloboration network is usually not connected
        #graph.cal_average_shortest_path_length()
        graph.cal_average_clustering()

        graph.write_to_pajek_net1()

        # 这个函数并不是真的画社团 只是把不同clique画出来而已 画的是整个的图
        graph.draw_community()

        graph.set_max_connected_component_subgraph()
        graph.draw_max_connected_component_subgraph()
        graph.cal_average_shortest_path_length_in_max_connected_component_subgraph()

        #graph.draw_graph()
        #graph.draw_graph_spring_layout()
        #graph.draw_graph_random()


        print "[INFO]: author_collaboration_network_analysis is finished!"
    except Exception,e:
        print traceback.print_exc()

def author_collaboration_network_analysis1( xml_parser_obj1, xml_parser_obj2, OUTPUT_PATH ):
    try:

        # get the author clique list
        author_clique_list = xml_parser_obj1.get_article_author()
        author_clique_list.extend(xml_parser_obj2.get_article_author())

        # construct the graph based on the author clique list
        graph = MyGraph()
        graph.construct_graph(author_clique_list)
        graph.set_output_path(OUTPUT_PATH)

        # calculate the statistics
        graph.cal_num_of_nodes()
        graph.cal_num_of_edges()

        graph.cal_degree_distribution()
        graph.cal_density()

        graph.cal_average_shortest_path_length()
        graph.cal_average_clustering()

        graph.write_to_pajek_net1()

        graph.draw_community()
        #graph.draw_graph()
        #graph.draw_graph_spring_layout()
        #graph.draw_graph_random()

        print "[INFO]: author_collaboration_network_analysis is finished!"
    except Exception,e:
        print traceback.print_exc()

def test_for_srx():
    try:

        graph = MyGraph()
        graph.set_output_path(OUTPUT_PATH)

        for line in file(INPUT_PATH, "r"):
            u = line.split(',')[0]
            v = line.split(',')[1]

            graph.add_edge(u, v)

        print "[INFO]: graph is finished!"


        graph.cal_average_clustering()
        graph.cal_average_shortest_path_length_in_max_connected_component_subgraph()
        graph.cal_degree_distribution()
        graph.cal_density()
        graph.cal_transitivity()


    except Exception,e:
        print traceback.print_exc()



def main():
    try:

        print "[INFO]: Programme is running......"

        # parse the xml and get the result
        #a_obj1 = XmlParser(XML_PATH1, STOP_WORDS_PATH)
        #a_obj2 = XmlParser(XML_PATH2, STOP_WORDS_PATH)

        #statical_analysis(a_obj1, OUTPUT_PATH1)
        #statical_analysis(a_obj2, OUTPUT_PATH2)

        #author_collaboration_network_analysis(a_obj1, OUTPUT_PATH1)


        print "[INFO]: Programme terminated successfully!"

    except Exception, e:
        print traceback.print_exc()


main()
