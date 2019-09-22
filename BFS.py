try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
from Node import Node
from Printer import Printer

class BFS:
    P = Q.PriorityQueue()
    Q = []
    T = None
    A = None
    n0 = None

    def __init__(self, n0_value, A, T):
        self.T = Node(T, None, T, None)
        self.A = A
        self.n0 = Node(n0_value, None, T, None)

    def search(self):
        self.P.put(self.n0)
        while (self.T not in self.P.queue ) and not ( self.P.empty() ):
            u = self.P.get()
            self.Q.append(u)
            expanded_nodes = u.expand(self.T.value, self.A)
            self.add_pending_nodes(expanded_nodes)

        if not self.P.empty():
            print()
            print("FOUND A SOLUTION! :)")
            Printer().print(self.get_path(self.P.get()))

        else:
            print("NO SOLUTION :(")

    def add_pending_nodes(self, node_list):
        for node in node_list:
            if not (node in self.Q) and not (node in self.P.queue):
                self.P.put(node)

    def get_path(self, last_node):
        aux_node = last_node
        path = list()
        while aux_node.father is not None:
            path.insert(0, aux_node)
            aux_node = aux_node.father
        path.insert(0, aux_node)
        return path


