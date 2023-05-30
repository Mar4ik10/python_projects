from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt

variant = 1629 % 6 + 1
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
        global text1, G
        root2 = Toplevel(root1)
        root2.title("Вікно 2")
        root2.geometry("300x200")
        label1 = Label(root2, text="Матриця суміжності")
        label1.grid(row=0, column=1, sticky=EW)
        label2 = Label(root2, text="""         v1
        v2
        v3
        v4
        v5
        v6
        v7
        v8""")
        label3 = Label(root2, text="v1   v2    v3    v4    v5    v6    v7    v8")
        label2.grid(row=2, column=0, sticky="ne")
        label3.grid(row=1, column=1, sticky="w")
        text1 = Text(root2, width=25, height=9)
        text1.insert(END,
                     "0  0  0  0  0  0  0  0\n0  0  0  0  0  0  0  0\n0  0  0  0  0  0  0  0\n"
                     "0  0  0  0  0  0  0  0\n0  0  0  0  0  0  0  0\n0  0  0  0  0  0  0  0\n"
                     "0  0  0  0  0  0  0  0\n0  0  0  0  0  0  0  0")
        text1.grid(row=2, column=1, sticky="wn")
        btn2 = Button(root2, text="Сформувати матрицю", command=self.make_matrix)
        btn2.grid(row=3, column=0, sticky=S)
        btn3 = Button(root2, text="Показати граф", command=self.ershov_alg)
        btn3.grid(row=3, column=1)

    def ershov_alg(self):
        color_list = ["blue", "red", "green", "orange"]
        color_cur = 1
        color_arry = [0 for i in range(len(graph))]

        def degforming():
            def getkey(item):
                return item[0]

            def degcount(d):
                degnum = 0
                for k in range(len(graph)):
                    degnum += graph[k][d]
                return degnum

            deg_arr = [[0 for i in range(2)] for j in range(len(graph))]
            for j in range(int(len(graph))):
                deg_arr[j][0] = degcount(j) * 100
                deg_arr[j][1] = j
                for i in range(int(len(graph))):
                    if graph[i][j] == 1:
                        deg_arr[j][0] += degcount(i)
            deg_arr.sort(key=getkey, reverse=True)
            return deg_arr

        def dyer(curcol, node):
            for k in range(int(len(graph))):
                if graph[node][k] == 0:
                    if color_arry[k] == 0:
                        color_arry[k] = curcol

        sortarr = degforming()
        for i in range(int(len(graph))):
            if not color_arry[sortarr[i][1]]:
                color_arry[sortarr[i][1]] = color_cur
                dyer(color_cur, sortarr[i][1])
                color_cur += 1
        print('Задана таблиця суміжності')
        for i in range(len(graph)):
            print(graph[i])
        G = nx.Graph()
        G.add_nodes_from(i for i in range(1, len(graph) + 1))
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] != 0:
                    G.add_edge(j + 1, i + 1)
        node_color = []
        for i in color_arry:
            node_color.append(color_list[i])
        node_color[-1] = "blue"
        nx.draw_spring(G, node_color=node_color, with_labels=True)
        plt.show()

    def make_matrix(self):
        global graph
        graph = []
        a = text1.get("1.0", END).split("\n")
        for i in a:
            if i:
                graph.append(i.split())
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                graph[i][j] = int(graph[i][j])


Main()
