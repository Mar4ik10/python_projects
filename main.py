import random
from tkinter import *
from tkinter import messagebox as ms

text = f"П.І,Б: Семенюк Марк Павлович\nМоя група: ІО - 16\nМій номер у групі: 29\nМій варіант: 16"


class Window1:
    def __init__(self):
        global text, root1
        root1 = Tk()
        root1.iconbitmap("flag-400.ico")
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
        mainmenu.add_command(label="Вікно 2", command=Window2)
        mainmenu.add_command(label="Вікно 3", command=Window3)
        mainmenu.add_command(label="Вікно 4", command=Window4)
        root1.mainloop()


class Window2:
    def __init__(self):
        global lb1, lb2, AorB, A, B, labelA, labelB, set1, set2
        set1 = ("Олег", "Олександр", "Артем", "Павло", "Марк", "Владислав", "Андрій", "Єгор", "Назар", "Вадим",
                "Василь", "Олександр", "Богдан", "Максим", "Денис")
        set2 = ("Анастасія", "Валерія", "Ксенія", "Наталія", "Юлія", "Катерина", "Ірина", "Оксана", "Ольга", "Марія",
                "Софія", "Дарина", "Вероніка", "Зоя", "Іванка")
        A = set()
        B = set()

        root2 = Toplevel(root1)
        root2.iconbitmap("flag-400.ico")
        root2.title("Вікно 2")
        root2.geometry("400x400")
        label1 = Label(root2, text="Множина жіночих імен")
        label2 = Label(root2, text="Множина чоловічих імен")
        label1.place(x=0, y=0)
        label2.place(x=200, y=0)
        strvar1 = StringVar(value=set1)
        strvar2 = StringVar(value=set2)
        lb1 = Listbox(root2, listvariable=strvar1, height=13, width=30, selectmode=EXTENDED)
        lb2 = Listbox(root2, listvariable=strvar2, height=13, width=30, selectmode=EXTENDED)
        lb1.place(x=0, y=20)
        lb2.place(x=200, y=20)
        AorB = IntVar()
        rdbA = Radiobutton(root2, text="Множина А", variable=AorB, value=1)
        rdbB = Radiobutton(root2, text="Множина В", variable=AorB, value=2)
        rdbA.place(x=20, y=230)
        rdbB.place(x=250, y=230)
        btn1 = Button(root2, text="Додати", command=self.add_to)
        btn1.place(x=160, y=230)
        labelA = Label(root2, text="A =")
        labelB = Label(root2, text="B =")
        labelA.place(x=0, y=270)
        labelB.place(x=0, y=330)
        btn2 = Button(root2, text="Очистити", command=self.clear_set)
        btn2.place(x=20, y=370)
        btn3 = Button(root2, text="Зберегти", command=self.save_to)
        btn3.place(x=250, y=370)

    def add_to(self):
        global lb1, lb2, AorB, A, B, labelA, labelB
        if AorB.get() == 1:
            for i in lb1.curselection():
                A.add(lb1.get(i))
            for j in lb2.curselection():
                A.add(lb2.get(j))

        elif AorB.get() == 2:
            for i in lb1.curselection():
                B.add(lb1.get(i))
            for j in lb2.curselection():
                B.add(lb2.get(j))
        labelA["text"] = f"A = {A}"
        labelB["text"] = f"B = {B}"

    def clear_set(self):
        global A, B, labelA, labelB
        A.clear()
        B.clear()
        labelA["text"] = "A ="
        labelB["text"] = "B ="
        with open("../../../../Учеба/2 семестр/Дискретка/Лаба 2/sets1.txt", "w") as f:
            f.write("")

    def save_to(self):
        global A, B, labelA, labelB
        with open("../../../../Учеба/2 семестр/Дискретка/Лаба 2/sets1.txt", "w") as f:
            f.write(str(A) + "\n")
            f.write(str(B))
        ms.showinfo("Інформація", "Ви зберегли дані у файл.")


class Window3:
    def __init__(self):
        global dict_aSB, dict_bSA, dict_aRB, dict_bRA, a_cholovikb, a_svekorb, T, Y, U, I, O
        root3 = Toplevel(root1)
        root3.iconbitmap("flag-400.ico")
        root3.title("Вікно 3")
        llabel1 = Label(root3, text=f"A = {A}")
        llabel2 = Label(root3, text=f"B = {B}")
        llabel1.place(x=0, y=0)
        llabel2.place(x=0, y=40)
        llabel3 = Label(root3, text="aSb", font=("Arial", 16))
        llabel3.place(x=250, y=70)

        canv1 = Canvas(root3, width=800, height=1000)
        canv1.create_text(250, 310, text="aRb", font=("Arial", 16))

        dict_aSB = {}
        dict_bSA = {}
        dict_aRB = {}
        dict_bRA = {}

        for i in range(len(A)):
            canv1.create_text(50 + 60 * i, 30, text=list(A)[i])
            canv1.create_oval(40 + 60 * i, 40, 70 + 60 * i, 70, fill="blue")
            dict_aSB[list(A)[i]] = (50 + 60 * i, 70)

            canv1.create_text(50 + 60 * i, 400, text=list(A)[i])
            canv1.create_oval(40 + 60 * i, 410, 70 + 60 * i, 440, fill="blue")
            dict_aRB[list(A)[i]] = (50 + 60 * i, 440)

        for j in range(len(B)):
            canv1.create_text(50 + 60 * j, 250, text=list(B)[j])
            canv1.create_oval(40 + 60 * j, 210, 70 + 60 * j, 240, fill="yellow")
            dict_bSA[list(B)[j]] = (50 + 60 * j, 210)

            canv1.create_text(50 + 60 * j, 680, text=list(B)[j])
            canv1.create_oval(40 + 60 * j, 640, 70 + 60 * j, 670, fill="yellow")
            dict_bRA[list(B)[j]] = (50 + 60 * j, 640)

        for b in self.a_svekorb():
            canv1.create_line(dict_aSB[b[0]], dict_bSA[b[1]], arrow=LAST)

        for b in self.a_cholovikb():
            canv1.create_line(dict_aRB[b[0]], dict_bRA[b[1]], arrow=LAST)
        canv1.place(x=0, y=100)

        T = R + S  # Об'єднання

        Y = []  # Перетин
        for i in R:
            if i in S:
                Y.append(i)

        U = []  # R \ S
        for i in R:
            if i not in S:
                U.append(i)

        I = []  # U \ R
        for i in A:
            for j in B:
                I.append([i, j])

        O = []
        for i in I:
            if i not in R:
                O.append(i)

    def a_svekorb(self):
        global svekor1, S
        a = set()
        for i in A:
            if i in set1:
                a.add(i)

        b = set()
        for i in B:
            if i in set1:
                b.add(i)

        u = 0
        svekor = list()
        svekor1 = list()
        S = list()
        while u < len(a) and len(b) != 0:
            one = random.choice(list(a))
            two = random.choice(list(b))
            numbsvekor = 0
            numbhus = 0
            for j in range(len(svekor)):
                if one in svekor[j]:
                    numbsvekor += 1
                if two in svekor[j]:
                    numbhus += 1
            if one != two and numbsvekor < 3 and numbhus < 3:
                S.append([one, two])
                svekor.append(one + two)
                svekor1.append(one)
                u += 1
                b.remove(two)
        return S

    def a_cholovikb(self):
        global R
        a = set()
        for i in A:
            if i in set1:
                a.add(i)

        b = set()
        for i in B:
            if i in set2:
                b.add(i)

        u = 0
        cholovik = list()
        druzina = list()
        R = list()
        while u < len(a) and len(b) != 0:
            one = random.choice(list(a))
            two = random.choice(list(b))
            if one not in svekor1:
                R.append([one, two])
                u += 1
                cholovik.append(one)
                druzina.append(two)
                a.remove(one)
                b.remove(two)
        return R


class Window4:
    def __init__(self):
        global canv2, root4
        root4 = Toplevel(root1)
        root4.iconbitmap("flag-400.ico")
        root4.title("Вікно 4")
        mainmenu1 = Menu(root1)
        root4.config(menu=mainmenu1)
        mainmenu1.add_command(label="R ∪ S", command=self.btn_union)
        mainmenu1.add_command(label="R ∩ S", command=self.btn_inter)
        mainmenu1.add_command(label=r"R \ S", command=self.btn_dif)
        mainmenu1.add_command(label=r"U \ R", command=self.dif_btn)
        mainmenu1.add_command(label="S⁻¹", command=self.btn_trans)
        canv2 = Canvas(root4, width=800, height=300)
        canv2.place(x=0, y=0)

    def btn_union(self):
        canv2.delete("all")
        canv2.create_text(250, 10, text="R ∪ S", font="Arial 16")

        dict_AB = {}
        for i in range(len(A)):
            canv2.create_text(50 + 60 * i, 30, text=list(A)[i])
            canv2.create_oval(40 + 60 * i, 40, 70 + 60 * i, 70, fill="blue")
            dict_AB[list(A)[i]] = (50 + 60 * i, 70)

        dict_BA = {}
        for j in range(len(B)):
            canv2.create_text(50 + 60 * j, 250, text=list(B)[j])
            canv2.create_oval(40 + 60 * j, 210, 70 + 60 * j, 240, fill="yellow")
            dict_BA[list(B)[j]] = (50 + 60 * j, 210)

        for b in T:
            canv2.create_line(dict_AB[b[0]], dict_BA[b[1]], arrow=LAST)

    def btn_inter(self):
        canv2.delete("all")
        canv2.create_text(250, 10, text="R ∩ S", font="Arial 16")

        dict_AB = {}
        for i in range(len(A)):
            canv2.create_text(50 + 60 * i, 30, text=list(A)[i])
            canv2.create_oval(40 + 60 * i, 40, 70 + 60 * i, 70, fill="blue")
            dict_AB[list(A)[i]] = (50 + 60 * i, 70)

        dict_BA = {}
        for j in range(len(B)):
            canv2.create_text(50 + 60 * j, 250, text=list(B)[j])
            canv2.create_oval(40 + 60 * j, 210, 70 + 60 * j, 240, fill="yellow")
            dict_BA[list(B)[j]] = (50 + 60 * j, 210)

        for b in Y:
            canv2.create_line(dict_AB[b[0]], dict_BA[b[1]], arrow=LAST)

    def btn_dif(self):
        canv2.delete("all")
        canv2.create_text(250, 10, text=r"R \ S", font="Arial 16")

        dict_AB = {}
        for i in range(len(A)):
            canv2.create_text(50 + 60 * i, 30, text=list(A)[i])
            canv2.create_oval(40 + 60 * i, 40, 70 + 60 * i, 70, fill="blue")
            dict_AB[list(A)[i]] = (50 + 60 * i, 70)

        dict_BA = {}
        for j in range(len(B)):
            canv2.create_text(50 + 60 * j, 250, text=list(B)[j])
            canv2.create_oval(40 + 60 * j, 210, 70 + 60 * j, 240, fill="yellow")
            dict_BA[list(B)[j]] = (50 + 60 * j, 210)

        for b in U:
            canv2.create_line(dict_AB[b[0]], dict_BA[b[1]], arrow=LAST)

    def dif_btn(self):
        canv2.delete("all")
        canv2.create_text(250, 10, text=r"U \ R", font="Arial 16")

        dict_AB = {}
        for i in range(len(A)):
            canv2.create_text(50 + 60 * i, 30, text=list(A)[i])
            canv2.create_oval(40 + 60 * i, 40, 70 + 60 * i, 70, fill="blue")
            dict_AB[list(A)[i]] = (50 + 60 * i, 70)

        dict_BA = {}
        for j in range(len(B)):
            canv2.create_text(50 + 60 * j, 250, text=list(B)[j])
            canv2.create_oval(40 + 60 * j, 210, 70 + 60 * j, 240, fill="yellow")
            dict_BA[list(B)[j]] = (50 + 60 * j, 210)

        for b in O:
            canv2.create_line(dict_AB[b[0]], dict_BA[b[1]], arrow=LAST)

    def btn_trans(self):
        canv2.delete("all")
        canv2.create_text(250, 10, text="S⁻¹", font="Arial 16")

        dict_AB = {}
        for i in range(len(A)):
            canv2.create_text(50 + 60 * i, 30, text=list(A)[i])
            canv2.create_oval(40 + 60 * i, 40, 70 + 60 * i, 70, fill="blue")
            dict_AB[list(A)[i]] = (50 + 60 * i, 70)

        dict_BA = {}
        for j in range(len(B)):
            canv2.create_text(50 + 60 * j, 250, text=list(B)[j])
            canv2.create_oval(40 + 60 * j, 210, 70 + 60 * j, 240, fill="yellow")
            dict_BA[list(B)[j]] = (50 + 60 * j, 210)

        for b in S:
            canv2.create_line(dict_BA[b[1]], dict_AB[b[0]], arrow=LAST)


Window1()
