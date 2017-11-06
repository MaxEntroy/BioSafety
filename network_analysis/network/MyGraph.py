#-*- coding:utf-8 -*-
from GraphOperation import*

'''
基于我自己的工具类MyGraph
写一个图的操作类，实现图的各种操作
'''

class MyGraph:

    # 构造函数 - 主要是为了定义成员变量
    def __init__(self):
        self.my_graph = GraphOperation()
        self.map_name_to_number = dict()
        self.map_number_to_name = dict()
        self.output_path = ""

        self.clique_list = [] # for draw_community

        self.max_connected_component_subgraph = None

    # 构造图 - 初始化两个mapper,并且构造图
    def construct_graph(self, clique_list):
        try:

            # convert the name to number and store the relation in map_name_to_number
            number = 1
            new_clique_list = []

            for clique in clique_list:
                new_clique = []
                for u in clique:
                    if u in self.map_name_to_number:
                        new_clique.append(self.map_name_to_number[u])
                    else:
                        self.map_name_to_number[u] = number
                        number += 1
                        new_clique.append(self.map_name_to_number[u])
                new_clique_list.append(new_clique)

            # convert the number to name and store the relation in map_number_to_name
            self.map_number_to_name = dict()
            for name, number in self.map_name_to_number.items():
                self.map_number_to_name[number] = name

            self.clique_list = new_clique_list
            # construct graph based on the new_clique_list
            for clique in new_clique_list:
                # add all edges

                for u in clique:
                    # add a single node in case there exists node itself
                    self.my_graph.add_node(u)

                    for v in clique:
                        if (u == v):
                            continue
                        e = (u, v)
                        self.my_graph.add_edge_by_tuple(e)

            print "[INFO]: construct_graph is finished!"
        except Exception,e:
            print traceback.print_exc()

    # 加入一条边
    def add_edge(self, u, v):
        try:

            self.my_graph.add_edge(u, v)

        except Exception,e:
            print traceback.print_exc()

    # 获得所有边
    def get_all_edges(self):
        try:

            return self.my_graph.get_edges()

        except Exception,e:
            print traceback.print_exc()

    # 设置网络特征的输出路径
    def set_output_path(self, output_path):
        try:
            self.output_path = output_path
            print "[INFO]: set_output_path is finished!"
        except Exception,e:
            print traceback.print_exc()

    # 获得最大联通分量
    # 由于必须是在整个图生成之后，才能获得最大联通分量
    # 所以这个方法必须写在封装的第二层，第一层的类写的不够好。不能直接封装
    def set_max_connected_component_subgraph(self):
        try:
            self.max_connected_component_subgraph = max(nx.connected_component_subgraphs(self.my_graph.graph), key=len)
            print "[INFO]: set_max_connected_component_subgraph is finished!"
        except Exception,e:
            print traceback.print_exc()

    # 返回的是原生的nx.Graph()
    def get_max_connected_component_subgraph(self):
        try:
            return self.max_connected_component_subgraph
        except Exception,e:
            print traceback.print_exc()
    #-----------------------------------------------------------------------
    #-----------------------draw the network--------------------------------
    #-----------------------------------------------------------------------



    # 按照不同的社团进行绘图 - 不同社团具有不同的颜色
    # 逻辑是 不同的社团分别加入进去，然后配置颜色，绘图
    # 因为少了一层封装，所以掉用的时候只能按照最底层的凡是去调用，这样其实不好。
    # 为此，还增加了成员变量，保存clique_list
    def draw_community(self):
        try:
            # 初始信息
            #pos = nx.spring_layout(self.my_graph.graph)
            pos = nx.spring_layout(self.my_graph.graph)
            node_size_ = 100
            color_list = ["red", "yellow", "blue", "green", "pink", "orange", "purple"]
            #color_list = ["red", "yello", "blue", "green"]
            color_list_len = len(color_list)

            # add node and edges
            for i, node_list in enumerate(self.clique_list):
                edge_list = self.get_edges_for_community(node_list)

                # 以下两个函数参数太多，先暂时不直接封装
                #nx.draw_networkx_nodes(self.my_graph.graph, pos, node_list, node_size=node_size_, node_color=color_list[i%color_list_len])
                nx.draw_networkx_nodes(self.my_graph.graph, pos, node_list, node_size=node_size_, node_color=color_list[i], label="hello")
                nx.draw_networkx_edges(self.my_graph.graph, pos, edge_list)

            #title = "Collaboration Network"
            title = "people relation by train"
            plt.title(title)
            plt.show()

            print "[INFO]: draw_community is finished!"
        except Exception,e:
            print traceback.print_exc()

    def get_edges_for_community(self, node_list):
        try:
            edge_list = []
            for u in node_list:
                for v in node_list:
                    if u == v:
                        continue
                    else:
                        edge_list.append((u,v))
            return edge_list
        except Exception,e:
            print traceback.print_exc()

    # 基本画图
    def draw_graph(self,title):
        try:
            self.my_graph.draw_graph(title)
            print "[INFO]: draw_graph is finished!"
        except Exception,e:
            print traceback.print_exc()

    def draw_network(self):
        try:
            self.draw_network()
        except Exception,e:
            print traceback.print_exc()

    def draw_graph_random_layout(self):
        try:
            self.my_graph.draw_graph_random()
        except Exception,e:
            print traceback.print_exc()

    def draw_graph_spring_layout(self):
        try:
            self.my_graph.draw_graph_spring_layout()
            print "[INFO]: draw_graph is finished!"
        except Exception,e:
            print traceback.print_exc()

    #-----------------------------------------------------------------------
    #-----------------------network analysis--------------------------------
    #-----------------------------------------------------------------------


    # 计算节点数
    def cal_num_of_nodes(self):
        try:
            num_nodes = self.my_graph.get_number_of_nodes()
            file_path = self.output_path+"number_of_nodes.txt"

            outfile = open(file_path, "w")
            outfile.write(str(num_nodes) + '\n')
            outfile.close()
            print "[INFO]: cal_num_of_nodes is finished!"
        except Exception,e:
            print traceback.print_exc()

    # 计算边数
    def cal_num_of_edges(self):
        try:
            num_edges = self.my_graph.get_number_of_edges()
            file_path = self.output_path + "number_of_edges.txt"

            outfile = open(file_path, "w")
            outfile.write(str(num_edges) + '\n')
            outfile.close()
            print "[INFO]: cal_num_of_edges is finished!"
        except Exception, e:
            print traceback.print_exc()

    # 计算度分布 - 这个函数很好，比下面的save_distribution好，因为下面的版本知识获得每个节点的度，没有真实统计
    def cal_degree_distribution(self):
        try:

            degree_distribution_list = self.my_graph.get_degree_distribution()
            file_path = self.output_path + "degree_distribution.txt"

            outfile = open(file_path, "w")
            for item in degree_distribution_list:
                line = str(item) + '\n'
                outfile.write(line)
            outfile.close()
            print "[INFO]: cal_degree_distribution is finished!"
        except Exception, e:
            print traceback.print_exc()
    def draw_degree_distribution(self):
        try:
            self.my_graph.draw_degree_distribution()

        except Exception,e:
            print traceback.print_exc()
    def get_degree(self):
        try:
            return self.my_graph.get_degree()
        except Exception,e:
            print traceback.print_exc()

    #
    def save_degree_distribution(self):
        try:

            degree_distribution = self.get_degree()
            degree_list = []

            for key in degree_distribution:
                value = degree_distribution[key]
                degree_list.append(value)

            file_path = self.output_path + "degree_distribution_fix.txt"
            outfile = open(file_path, "w")
            for item in degree_list:
                line = str(item) + '\n'
                outfile.write(line)
            outfile.close()

            print "[INFO]: save_degree_distribution is finished!"

        except Exception,e:
            print traceback.print_exc()
    # 计算网络密度
    def cal_density(self):
        try:
            density = self.my_graph.get_density()
            file_path = self.output_path + "graph_density.txt"

            outfile = open(file_path, "w")
            outfile.write(str(density) + '\n')
            outfile.close()
            print "[INFO]: cal_density is finished!"
        except Exception, e:
            print traceback.print_exc()

    # 计算聚集系数
    def cal_transitivity(self):
        try:
            transitivity = self.my_graph.get_transitivity()
            file_path = self.output_path + "transitivity.txt"

            outfile = open(file_path, "w")
            outfile.write(str(transitivity) + '\n')
            outfile.close()
            print "[INFO]: cal_transitivity is finished!"
        except Exception, e:
            print traceback.print_exc()

    def cal_average_clustering(self):
        try:
            average_clustering = self.my_graph.get_averate_clustering()
            file_path = self.output_path + "average_clustering.txt"

            outfile = open(file_path, "w")
            outfile.write(str(average_clustering) + '\n')
            outfile.close()
            print "[INFO]: cal_average_clustering is finished!"
        except Exception,e:
            print traceback.print_exc()

    # 计算平均距离
    def cal_average_shortest_path_length(self):
        try:
            aver_shortest_path = self.my_graph.get_average_shortest_path_length()
            file_path = self.output_path + "average_shortest_path_length.txt"

            outfile = open(file_path, "w")
            outfile.write(str(aver_shortest_path) + '\n')
            outfile.close()
            print "[INFO]: cal_average_shortest_path_length is finished!"
        except Exception, e:
            print traceback.print_exc()

    # 写入pajek格式文件
    def write_to_pajek_net(self):
        try:

            output_path = self.output_path + "graph_of_author_relation.net"

            # write to net file
            outfile = open(output_path, "w")

            nodes_num = self.my_graph.get_number_of_nodes()
            edges_num = self.my_graph.get_number_of_edges()
            first_line_of_node = "*Vertices " + str(nodes_num) + '\n'
            first_line_of_edge = "*Edges " + str(edges_num) + '\n'

            outfile.write(first_line_of_node)
            nodes_list = self.my_graph.get_nodes()
            for node in nodes_list:
                line = ""
                line += str(node) + ' ' + "\"" + str(self.map_number_name[node]) + "\"" + '\n'
                outfile.write(line)

            outfile.write(first_line_of_edge)
            edges_list = self.my_graph.get_edges()
            for edge in edges_list:
                line = ""
                line += str(edge[0]) + ' ' + str(edge[1]) + '\n'
                outfile.write(line)

            outfile.close()
            print "[INFO]: write_to_pajek_net is finished!"
        except Exception, e:
            print traceback.print_exc()

    def write_to_pajek_net1(self):
        try:
            pajek_net_path = self.output_path + "graph_of_author_relation.net"
            self.my_graph.write_to_pajek(pajek_net_path)

            print "[INFO]: write_to_pajek_net1 is finished!"
        except Exception, e:
            print traceback.print_exc()

    #--------------------------------------------------------
    #--------------centrality--------------------------------
    #--------------------------------------------------------
    def get_degree_centrality(self):
        try:
            return self.my_graph.get_degree_centrality()

            print "[INFO]: get_degree_centrality is finished!"
        except Exception,e:
            print traceback.print_exc()

    def get_betweenness_centrality(self):
        try:
            return self.my_graph.get_betweenness_centrality()

            print "[INFO]: get_betweenness_centrality is finished!"
        except Exception, e:
            print traceback.print_exc()

    def get_load_centrality(self):
        try:
            return self.my_graph.get_load_centrality()

            print "[INFO]: get_load_centrality is finished!"
        except Exception, e:
            print traceback.print_exc()

    def get_eigenvector_centrality(self):
        try:
            return self.my_graph.get_eigenvector_centrality()

            print "[INFO]: get_eigenvector_centrality is finished!"
        except Exception, e:
            print traceback.print_exc()

    # --------------------------------------------------------
    # --------------component--------------------------------
    # --------------------------------------------------------
    def draw_max_connected_component_subgraph(self):
        try:
            plt.figure(figsize=(10, 7), dpi=80)
            plt.subplot(1,1,1)
            nx.draw_networkx(self.get_max_connected_component_subgraph(),with_labels = False)
            title = "Max connected subgraph of related network"
            plt.title(title)

            '''
            plt.subplot(1,2,2)
            nx.draw_networkx(self.get_max_connected_component_subgraph(),with_labels = False)
            title = ""
            plt.title(title)
            '''

            plt.show()

            print "[INFO]: draw_max_connected_component_subgraph is finished!"
        except Exception, e:
            print traceback.print_exc()

    def get_average_shortest_path_length_in_max_connected_component_subgraph(self):
        try:

            res = nx.average_shortest_path_length(self.get_max_connected_component_subgraph())
            print "[INFO]: get_average_shortest_path_length_in_max_connected_component_subgraph is finished!"
            return res
        except Exception, e:
            print traceback.print_exc()

    def cal_average_shortest_path_length_in_max_connected_component_subgraph(self):
        try:
            aver_shortest_path = self.get_average_shortest_path_length_in_max_connected_component_subgraph()
            file_path = self.output_path + "average_shortest_path_length_in_max_connected_subgraph.txt"

            outfile = open(file_path, "w")
            outfile.write(str(aver_shortest_path) + '\n')
            outfile.close()
            print "[INFO]: cal_average_shortest_path_length_in_max_connected_component_subgraph is finished!"
        except Exception, e:
            print traceback.print_exc()

    def get_average_clustering_in_max_connected_component_subgraph(self):
        try:
            average_clustering = nx.average_clustering(self.get_max_connected_component_subgraph())
            return average_clustering
        except Exception,e:
            print traceback.print_exc()

    def cal_average_clustering_in_max_connected_component_subgraph(self):
        try:

            aver_clustering = self.get_average_clustering_in_max_connected_component_subgraph()
            file_path = self.output_path + "average_clustering_in_max_connected_component_subgraph.txt"

            outfile = open(file_path, "w")
            outfile.write(str(aver_clustering) + '\n')
            outfile.close()
            print "[INFO]: cal_average_clustering_in_max_connected_component_subgraphf is finished!"

        except Exception,e:
            print traceback.print_exc()
#----------------------------------------------------------------------------
    def get_core_number(self):
        try:
            return self.my_graph.get_core_number()
        except Exception,e:
            print traceback.print_exc()
    def cal_k_core_distribution(self):
        try:

            ret = self.get_core_number()
            for key in ret:
                value = ret[key]

            max = 0
            for key in ret:
                val = ret[key]
                if val > max:
                    max = val

            distribution = []
            for k in range(max+1):
                kc = self.my_graph.get_k_core(k)
                nums = len(kc.nodes())
                distribution.append(nums)

            file_path = self.output_path + "k_core_distribution.txt"

            outfile = open(file_path, "w")
            for item in distribution:
                outfile.write(str(item) + '\n')
            outfile.close()
            print "[INFO]: cal_k_core_distribution is finished!"
        except Exception,e:
            print traceback.print_exc()