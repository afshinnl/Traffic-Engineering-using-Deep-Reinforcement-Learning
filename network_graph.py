import networkx as nx

from typing import List
from itertools import islice

TOPOLOGY_FILE_NAME = 'topology_arpanet.txt'
K_PATHS = 5
switch_list = []

def build_graph() :
    graph = nx.Graph()
    global switch_list

    with open(TOPOLOGY_FILE_NAME, 'r') as topo:
        for row in topo.readlines():
            row_data : List[str] = row.split()[:2]

            for node in row_data:
                if not graph.has_node(node):
                    graph.add_node(node)
                    if node[:1] == 'S': #add switch number to a list
                        switch_list.append(node[1:])

            #ASSIGN PORTS
            #IP???

            if row_data[0][0] == 'H': #Host
                src_host_id : int = row_data[0].replace("H", "")
                src_host_mac : str = "00:00:00:00:00:{}".format(src_host_id.zfill(2))

                if row_data[1][0] == 'S': #Host-Switch
                    graph.add_edge(row_data[0],row_data[1])
                    #graph.add_edge(row_data[1],row_data[0])   

            else: #Switch
                if row_data[1][0] == 'H': #Switch-Host
                    dst_host_id : int = row_data[1].replace("H", "")
                    dst_host_mac : str = "00:00:00:00:00:{}".format(dst_host_id.zfill(2))

                    graph.add_edge(row_data[0],row_data[1])
                    #graph.add_edge(row_data[1],row_data[0])

                    print(dst_host_mac)
                    #add edge

                else: #Switch-Switch
                    graph.add_edge(row_data[0],row_data[1])
                    #graph.add_edge(row_data[1],row_data[0])
                    #add edge with weights

#def find_paths(graph, src, dst):
#    return list(nx.shortest_simple_paths(graph, src, dst))

def find_shortest_paths(graph, source, target, k):
    try: 
        paths = list(islice(nx.shortest_simple_paths(graph, source, target), k))
    except nx.NetworkXNoPath:
        paths = []
        
    return paths
        