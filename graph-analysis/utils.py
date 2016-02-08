# Copyright (c) 2016 Yazan Boshmaf
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.


import networkx as nx
import random


def bfs_edges(G, size, source):
    """
    Produce edges in a breadth-first-search starting at source.
    Based on D. Eppstein implementation of BFS published in July, 2004.
    Reference: http://www.ics.uci.edu/~eppstein/PADS/BFS.py
    """
    visited=set([source])
    stack = [(source,iter(G[source]))]
    while stack and len(visited) != size:
        parent,children = stack[0]
        try:
            child = next(children)

            if child not in visited:
                yield parent,child
                visited.add(child)
                stack.append((child,iter(G[child])))

        except StopIteration:
            stack.pop(0)

def bfs_sample(G, size, source=None):
    if not source:
        source = random.choice(G.nodes())

    edges = bfs_edges(G, size, source)
    H = nx.Graph()
    for edge in edges:
        H.add_edge(*edge)
    return H
