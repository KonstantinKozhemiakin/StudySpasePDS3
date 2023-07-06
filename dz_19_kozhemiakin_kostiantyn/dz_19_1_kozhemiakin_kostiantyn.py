import networkx as nx
import matplotlib.pyplot as plt


def read_csv(file_name):
    with open(f"{file_name}.csv", "r") as f:
        new_list = []
        lines = f.read().splitlines()
        for i in range(len(lines)):
            if lines[i].split(sep=";") not in new_list:
                new_list.append(lines[i].split(sep=";"))
        return new_list


if __name__ == "__main__":
    cities = read_csv('cities')

    g = nx.Graph()
    for edge in cities:
        g.add_edge(edge[0], edge[1], weight=int(edge[2]))

    pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos, with_labels=False, node_size=10, alpha=0.4)
    plt.title("Cities")
    plt.show()
