'''Generates scale-free graphs using the Barabasi-Albert model.
Generated graphs have n vertices and m edges added at each step.
A graph is generated for each value of m in the list mvals.
The .txt file contains the edge list and the .grh file contains the adjacency list.
Each line in the .grh file is a comma-separated list of the vertices adjacent to the vertex corresponding to that line number (zero-indexed).
The files are saved in the 'tests' subdirectory as'test1.txt', 'test2.txt', ...... , 'testn.txt'.
Does not overwrite existing files.'''

import os
import networkx as nx
from networkx.generators.random_graphs import barabasi_albert_graph

n = 75
mvals = [5]


def barabasi_albert_graph_ext(n, m, seed):
    return barabasi_albert_graph(n, m, seed)


def scale_free_graph():
    overwrite = True

    if not os.path.exists('tests'):
        os.makedirs('tests')

    for m in mvals:
        g = barabasi_albert_graph_ext(n, m, None)
        edges = g.edges()

        i = 1
        if not overwrite:
            while os.path.exists('tests/test'+str(i)+'.txt'):
                i += 1

        file_name = 'tests/test'+str(i)+'.txt'
        with open(file_name, 'w') as fp:
            fp.write('\n'.join('{} {}'.format(x[0], x[1]) for x in edges))

        grh_file_name = 'tests/test'+str(i)+'.grh'
        with open(grh_file_name, 'w') as fp:
            for v in g.nodes():
                fp.write(','.join(str(u) for u in g.neighbors(v)) + '\n')


scale_free_graph()
