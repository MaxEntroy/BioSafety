#-*- coding:utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import traceback

'''
我对networkx 的封装
还是一个图操作-工具类
'''

class GraphOperation:

    #-----------------graph operation-----------------

    # construct a graph - undirected graph if default
    def __init__(self):

        self.graph = nx.Graph()

    def convert_to_directed_graph(self):
        self.graph = nx.DiGraph()

    def convert_to_multi_graph(self):
        self.graph = nx.MultiGraph()

    # only directed graph can do this operation
    def convert_to_undirected_graph(self):
        self.graph = nx.Graph()

    # clear the graph
    def clear_graph(self):
        try:
            self.graph.clear()
        except Exception, e:
            print traceback.print_exc()

    #------------------node operation----------------------------

    # add a node
    def add_node(self, node):
        try:
            self.graph.add_node(node)
        except Exception,e:
            print traceback.print_exc()

    # add a list of nodes
    def add_nodes_by_list(self, node_list):
        try:
            self.graph.add_nodes_from(node_list)
        except Exception,e:
            print traceback.print_exc()


    # remove a node
    def remove_node(self, node):
        try:
            self.graph.remove_node(node)
        except Exception,e:
            print traceback.print_exc()

    # remove a list of nodes
    def remove_nodes_by_list(self, node_list):
        try:
            self.graph.remove_nodes_from(node_list)
        except Exception,e:
            print traceback.print_exc()


    # get number of nodes
    def get_number_of_nodes(self):
        try:
            return self.graph.number_of_nodes()
        except Exception, e:
            print traceback.print_exc()

    # get nodes, return a list of nodes
    def get_nodes(self):
        try:
            return self.graph.nodes()
        except Exception, e:
            print traceback.print_exc()


    # get neighbors of v, return a list of nodes which is the neighbor of v
    def get_neighbors(self, v):
        try:
            return self.graph.neighbors(v)
        except Exception, e:
            print traceback.print_exc()

    #---------------edge operation------------------------------

    # add an edge
    def add_edge(self,u,v):
        try:
            self.graph.add_edge(u,v)
        except Exception,e:
            print traceback.print_exc()

    # add an edge by a tuple
    def add_edge_by_tuple(self,e):
        try:
            self.add_edge(*e) # unpack edge tuple
        except Exception,e:
            print traceback.print_exc()

    # add edges by list which is compromised of tuples, every tuple is an edge
    def add_edges_by_list(self, edge_list):
        try:
            self.graph.add_edges_from(edge_list)
        except Exception,e:
            print traceback.print_exc()


    # remove an edge
    def remove_edge(self,u ,v ):
        try:
            self.graph.remove_edge(u, v)
        except Exception,e:
            print traceback.print_exc()

    # remove an edge by tuple
    def remove_edge_by_tuple(self, e):
        try:
            self.remove_edge(*e)
        except Exception,e:
            print traceback.print_exc()

    # remove edges by list which is compromised of tuples
    def remove_edges_by_list(self, edge_list):
        try:
            self.remove_edges_from(edge_list)
        except Exception, e:
            print traceback.print_exc()


    # get number of edges
    def get_number_of_edges(self):
        try:
            return self.graph.number_of_edges()
        except Exception, e:
            print traceback.print_exc()

    # get edges, return a list of tuple which is a presentation of an edge
    def get_edges(self):
        try:
            return self.graph.edges()
        except Exception, e:
            print traceback.print_exc()


    # add weighted list by a list which is compromised of tuples
    def add_weighted_edge(self, weighted_edge_list):
        try:
            self.graph.add_weighted_edges_from(weighted_edge_list)
        except Exception, e:
            print traceback.print_exc()

    # get weighted edge
    def get_weighted_edge(self):
        try:
            return self.graph.edges(data='weight')
        except Exception, e:
            print traceback.print_exc()

    #---------------degree analysis-------------------------------------------------------------

    # get the degree of all nodes, return a dict<node, degree>.
    # directed graph work well, undirected graph does not test.
    def get_degree(self):
        try:
            return self.graph.degree()
        except Exception, e:
            print traceback.print_exc()

    # get the degree of a node, return an interger
    def get_degree_by_node(self, node_id):
        try:
            return self.graph.degree(node_id)
        except Exception, e:
            print traceback.print_exc()

    # get the degree of a node, but the degree is not viewed as sum of edges
    # instead the degree is viewed as sum of the weight of edges
    # eg: (1,2,0.5),(3,1,0.75) the degree based on weight of node 1 is 0.5+0.75 = 1.25(not 2)
    def get_degree_based_on_weight_by_node(self, node_id):
        try:
            return self.graph.degree(node_id, weight="weight")
        except Exception, e:
            print traceback.print_exc()

    # get sorted degrees, return a list. the item of a list is degree value of a node
    def get_sorted_degrees(self):
        try:
            return sorted(nx.degree(self.graph).values(), reverse=True)
        except Exception, e:
            print traceback.print_exc()



    # get the indegree of all nodes.
    def get_in_degree(self):
        try:
            return self.graph.in_degree()
        except Exception, e:
            print traceback.print_exc()

    # get the indegree of a node
    def get_in_degree_by_node(self, node_id):
        try:
            return self.graph.in_degree(node_id)
        except Exception, e:
            print traceback.print_exc()

    def get_in_degree_based_on_weight_by_node(self, node_id):
        try:
            return self.graph.in_degree(node_id, weight = "weight")
        except Exception, e:
            print traceback.print_exc()

    # get the outdegree of all nodes
    def get_out_degree(self):
        try:
            return self.graph.out_degree()
        except Exception, e:
            print traceback.print_exc()

    # get the outdegree of a node
    def get_out_degree_by_node(self, node_id):
        try:
            return self.graph.out_degree(node_id)
        except Exception, e:
            print traceback.print_exc()

    def get_out_degree_based_on_weight_by_node(self, node_id):
        try:
            return self.graph.out_degree(node_id, weight="weight")
        except Exception, e:
            print traceback.print_exc()



    # ----------component analysis-----------------

    # get connected components - return a list of set which is a component
    def get_connected_components(self):
        try:
            return nx.connected_components(self.graph)
        except Exception, e:
            print traceback.print_exc()

    # ----------drawing graph-----------------------
    def draw_graph(self,title):
        try:

            plt.title(title)
            nx.draw(self.graph)

            plt.show(title)
        except Exception, e:
            print traceback.print_exc()

    def draw_network(self):
        try:
            nx.draw_networkx(self.graph, nx.spring_layout)
            plt.show()
        except Exception,e:
            print traceback.print_exc()


    def draw_graph_random_layout(self):
        try:
            nx.draw_random(self.graph)
            plt.show()
        except Exception,e:
            print traceback.print_exc()


    def draw_graph_spring_layout(self):
        try:
            nx.draw_spring(self.graph)
            plt.show()
        except Exception,e:
            print traceback.print_exc()


    # ---------- Graph methods--------------------------

    # return a list of the frequency of each degree value
    # 这个函数我说明一下，之前的degree函数返回的是每个节点的度，但是度分布则是统计了度为某个值的个数。下面的函数
    # 很好的完成了这个任务，就是统计了度分布，当然最后一项是还有值的情形
    def get_degree_distribution(self):
        try:
            return nx.degree_histogram(self.graph)
        except Exception,e:
            print traceback.print_exc()
    def draw_degree_distribution(self):
        try:
            degree = nx.degree_histogram(self.graph)
            x = range(len(degree))
            y = [ z/float(sum(degree)) for z in degree ]
            plt.loglog(x,y,color="blue", linewidth=2)
            plt.show()
        except Exception,e:
            print traceback.print_exc()


    def get_density(self):
        try:
            return nx.density(self.graph)
        except Exception,e:
            print traceback.print_exc()

    # get the transitivity - global clustering coefficient
    def get_transitivity(self):
        try:
            return nx.transitivity(self.graph)
        except Exception,e:
            print traceback.print_exc()

    def get_averate_clustering(self):
        try:
            return nx.average_clustering(self.graph)
        except Exception,e:
            print traceback.print_exc()

    def get_average_shortest_path_length(self):
        try:
            return nx.average_shortest_path_length(self.graph)
        except Exception,e:
            print traceback.print_exc()


    def write_to_pajek(self, pajek_net_path):
        try:
            nx.write_pajek(self.graph, pajek_net_path)
        except Exception,e:
            print traceback.print_exc()

    #--------------------------------------------------------
    #--------------centrality--------------------------------
    #--------------------------------------------------------

    # The degree centrality for a node v is the fraction of nodes it is connected to.
    def get_degree_centrality(self):
        try:
            return nx.degree_centrality(self.graph)
        except Exception,e:
            print traceback.print_exc()

    # Betweenness centrality of a node v is the sum of the fraction of all-pairs shortest paths that pass through v
    def get_betweenness_centrality(self):
        try:
            return nx.betweenness_centrality(self.graph)
        except Exception,e:
            print traceback.print_exc()

    # The load centrality of a node is the fraction of all shortest paths that pass through that node.
    def get_load_centrality(self):
        try:
            return nx.load_centrality(self.graph)
        except Exception,e:
            print traceback.print_exc()

    # Eigenvector centrality computes the centrality for a node based on the centrality of its neighbors.
    def get_eigenvector_centrality(self):
        try:
            return nx.eigenvector_centrality(self.graph)
        except Exception,e:
            print traceback.print_exc()


    def get_core_number(self):
        try:

            return nx.core_number(self.graph)

        except Exception,e:
            print traceback.print_exc()

    def get_k_core(self, k):
        try:

            kc = nx.k_core(self.graph, k=k)
            return kc

        except Exception,e:
            print traceback.print_exc()