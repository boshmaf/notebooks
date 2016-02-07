import networkx as nx
import random
from sklearn.feature_extraction import DictVectorizer


def bfs_edges(G, size, source):
    """Produce edges in a breadth-first-search starting at source."""
    # Based on http://www.ics.uci.edu/~eppstein/PADS/BFS.py
    # by D. Eppstein, July 2004.
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

def get_vector(name, feature_names, full_vector):
    """Returns a complete feature vector"""
    name_features = {}
    name_features["last_letter"] = name[-1]
    name_features["last_two"] = name[-2:]
    name_features["last_is_vowel"] = 0 if name[-1] in "aeiouy" else 0

    vectorizer = DictVectorizer()
    small_vector = vectorizer.fit_transform(name_features).toarray()[0]
    small_feature_names = vectorizer.get_feature_names()

    hit_count = 0
    for index, feature_name in enumerate(feature_names):
        if feature_name in small_feature_names:
            full_vector[index] = small_vector[small_feature_names.index(feature_name)]
            hit_count += 1
        else:
            full_vector[index] = 0

    assert hit_count == len(small_feature_names) == small_vector.shape[0]
    assert full_vector.shape[0] == len(feature_names)

    return full_vector
