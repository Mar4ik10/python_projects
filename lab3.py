from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict, defaultdict
from itertools import chain
from math import inf

variant = 1629 % 10 + 1
text = f"П.І,Б: Семенюк Марк Павлович\nМоя група: ІО - 16\nМій номер у групі: 29\nМій варіант: {variant}"


class Main:
    def __init__(self):
        global text, root1
        root1 = Tk()
        root1.title("Вікно 1")
        root1.geometry("300x200")
        root1.resizable(False, False)
        label = Label(root1, text=text, justify=LEFT)
        label.grid(row=0, column=0)
        label1 = Label(root1, text="Русский военный корабль", bg="blue", fg="yellow")
        label2 = Label(root1, text="ІДІ НАХ*Й!", bg="yellow", fg="blue")
        label1.grid(row=1, column=0, stick="we")
        label2.grid(row=2, column=0, stick="we")

        mainmenu = Menu(root1)
        root1.config(menu=mainmenu)
        mainmenu.add_command(label="Вікно 2", command=self.window2)
        root1.mainloop()

    def window2(self):
        global ent1, ent2, lb1, G, edges_list, seed
        root2 = Toplevel(root1)
        root2.title("Вікно 2")
        root2.geometry("300x200")
        label3 = Label(root2, text="Введіть дані ребра: \n[початок] [кінець] [вага]")
        label3.grid(row=0, column=0, sticky=N)
        ent1 = Entry(root2, bd=5)
        ent1.grid(row=1, column=0, columnspan=2, sticky=NW)
        lb1 = Listbox(root2, width=15)
        lb1.grid(row=0, column=1, rowspan=2)
        edges_list = []
        btn1 = Button(root2, text="Додати у список", command=self.move)
        btn1.grid(row=2, column=0, sticky=EW)
        G = nx.DiGraph()
        label4 = Label(root2, text="")
        label4.grid(row=3, column=0, columnspan=2, sticky=EW)
        seed = 1346
        btn2 = Button(root2, text="Показати граф", command=self.make_graph)
        btn2.grid(row=4, column=0, columnspan=2)
        ent2 = Entry(root2, bd=5)
        ent2.grid(row=6, column=0)
        btn3 = Button(root2, text="Показати шлях", command=self.show_the_way)
        btn3.grid(row=5, column=0, columnspan=2)

    def move(self):
        global edges, edges_list
        a = ent1.get()
        lb1.insert(END, a)
        b = a.split()
        b[2] = int(b[2])
        G.add_edge(b[0], b[1], weight=b[2])
        edges_list.append(tuple(b))

    def show_the_way(self):
        adj_list = defaultdict(list)
        for u, v, w in edges_list:
            adj_list[u].append((v, w))
        weight, path = self.levit_alg(adj_list, ent2.get()[0], ent2.get()[2])
        way = list(zip(path, path[1::]))
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_edges(G, pos, width=2, arrowsize=10, arrowstyle="->")
        nx.draw_networkx_labels(G, pos, font_size=20)
        nx.draw_networkx_edges(G, pos, edgelist=way, width=2, arrowsize=10, arrowstyle="->", edge_color="r")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def levit_alg(self, gr, start, goal):
        dist = defaultdict(lambda: inf)
        dist[start] = 0
        path = {start: (start, ())}
        m0 = set()
        m1, m1_urg = IndexedQueue.fromkeys([start]), IndexedQueue()
        m2 = set(chain.from_iterable((v for v, _ in from_u) for from_u in gr.values())) - {start}

        restore_path = lambda tup: (*restore_path(tup[1]), tup[0]) if tup else ()

        def relax(u, v, w):
            if (dist[v] > dist[u] + w):
                dist[v] = dist[u] + w
                path[v] = (v, path[u])
                return True
            return False

        while m1 or m1_urg:
            u = m1_urg.pop() if m1_urg else m1.pop()
            for v, c in gr.get(u, ()):
                if v in m2:
                    m1.push(v)
                    m2.discard(v)
                    relax(u, v, c)
                elif v in m1:
                    relax(u, v, c)
                elif v in m0 and relax(u, v, c):
                    m1_urg.push(v)
                    m0.discard(v)
            m0.add(u)

        if goal in path:
            return dist[goal], restore_path(path[goal])
        else:
            return inf, ()

    def make_graph(self):
        global pos, edge_labels, seed
        print(seed)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_edges(G, pos, width=2, arrowsize=10, arrowstyle="->")
        nx.draw_networkx_labels(G, pos, font_size=20)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()
        seed +=1


class IndexedQueue(OrderedDict):
    def push(self, item):
        self[item] = None

    def pop(self):
        return OrderedDict.popitem(self, last=False)[0]


Main()
