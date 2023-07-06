import networkx as nx
from dz_19_1_kozhemiakin_kostiantyn import read_csv


def find_best_way(my_graph, start, finish):
    try:
        shortest_path = (nx.shortest_path(my_graph, start, finish, weight='weight'))
        shortest_path_length = (nx.shortest_path_length(my_graph, start, finish, weight='weight'))
        return shortest_path, shortest_path_length
    except:
        print('Search failed')

if __name__ == "__main__":
    cities = read_csv('cities')

    g = nx.Graph()
    for edge in cities:
        g.add_edge(edge[0], edge[1], weight=int(edge[2]))

    print(find_best_way(g, 'Rivne', 'Zhytomyr'))
