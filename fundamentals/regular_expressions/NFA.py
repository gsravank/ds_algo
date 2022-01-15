from DirectedDFS import DirectedDFS
import matplotlib.pyplot as plt
import string
import math
from fundamentals.directed_graphs.DiGraph import DiGraph


class NFA:
    def __init__(self, reg_exp):
        assert len(reg_exp) >= 2 and reg_exp[0] == '(' and reg_exp[-1] == ')'
        self.reg_exp = reg_exp
        self.meta_chars = set('()*|')

        self.digraph = self.build_epsilon_transition_digraph()
        return

    def recognizes(self, text):
        # Simulation of NFA
        m = len(self.reg_exp)
        n = len(text)

        # Start at state 0
        # Get reachable states from start, even before scanning any character from the text
        dfs = DirectedDFS(self.digraph, [0])
        states = [x for x in range(m + 1) if dfs.marked(x)]

        for idx in range(n):
            # Scan text
            matched = list()
            for v in states:
                if self.reg_exp[v] == '.' or self.reg_exp[v] == text[idx]:
                    matched.append(v + 1)

            # Make epsilon transitions
            dfs = DirectedDFS(self.digraph, matched)
            states = [x for x in range(m+1) if dfs.marked(x)]

        return m in states

    def build_epsilon_transition_digraph(self):
        # Construction of NFA
        m = len(self.reg_exp)
        digraph = DiGraph(m + 1)
        stack = list()

        for i in range(m):
            curr_char = self.reg_exp[i]

            if curr_char not in self.meta_chars:
                # Alphabet or .
                # digraph.add_edge(i, i+1)
                if i < m-1 and self.reg_exp[i + 1] == '*':
                    digraph.add_edge(i, i+1)
                    digraph.add_edge(i+1, i)
            else:
                # Process each metacharacter appropriately
                if curr_char == '(':
                    digraph.add_edge(i, i+1)
                    stack.append(i)
                elif curr_char == '|':
                    stack.append(i)
                elif curr_char == '*':
                    digraph.add_edge(i, i+1)
                else:
                    digraph.add_edge(i, i+1)
                    if len(stack) == 1:
                        # No | in between
                        op_loc = stack.pop()
                    else:
                        # | in between
                        or_loc = stack.pop()
                        op_loc = stack.pop()

                        digraph.add_edge(op_loc, or_loc + 1)
                        digraph.add_edge(or_loc, i)

                    if i < m-1 and self.reg_exp[i + 1] == '*':
                        digraph.add_edge(op_loc, i + 1)
                        digraph.add_edge(i + 1, op_loc)

        return digraph


if __name__ == '__main__':
    rexp = '((a*b|ac)*d)'
    nfa = NFA(rexp)

    m = len(rexp)

    vertex_point_map = dict()
    sorted_vertices = list(range(m + 1))
    points = DiGraph._get_circle_points([0.5, 0.5], 0.4, 2 * m + 1)
    vertex_point_map = dict(zip(sorted_vertices[::-1], points))
    # vertex_point_map = dict(zip(list(range(m + 1)), [[idx * 0.5, 0.0] for idx in range(m+1)]))

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    nfa.digraph.plot(ax, 'o', 'k', 'r', vertex_point_map=vertex_point_map, texts=rexp + '$')
    plt.show()

    texts = ['abd', 'bd', 'bacd', 'aaabd', 'aaabac', 'aaabacd']
    for text in texts:
        print(f"{text} {nfa.recognizes(text)}")