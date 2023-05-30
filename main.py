import random
from tkinter import *
from tkinter import messagebox

from functs import *

global G, N, setA, setB, setC, setU, n, p, X, Y
n = 0
p = 0
setA = set
setB = set
setC = set
setU = set
G = 16
N = 29
X = set
Y = set
variant = (N + G % 60) % 30 + 1
text = f"П.І,Б: Семенюк Марк Павлович\nМоя група: ІО - {G}\nМій номер у групі: {N}\nМій варіант: {variant}"


class Window1:
    def __init__(self):
        global var, rdbtn1, rdbtn2, label, en1, en2, en3, en4, btn, result, btn1, btn2, btn3, btn4, root
        root = Tk()
        root.title("Вікно 1")
        root.geometry("400x400")
        root.resizable(False, False)
        label = Label(root, text="", justify=LEFT, font=("Arial", 10))
        result = Label(root, text="", justify=LEFT, font=("Arial", 10))
        label1 = Label(root, text=text, anchor=W, justify=LEFT)
        var = IntVar()
        rdbtn1 = Radiobutton(root, text="Random", value=0, variable=var, command=self.select)
        rdbtn2 = Radiobutton(root, text="Your values", value=1, variable=var, command=self.select)
        label3 = Label(root, text="A:")
        label4 = Label(root, text="B:")
        label5 = Label(root, text="C:")
        label6 = Label(root, text="U:")
        btn = Button(root, text="Дія", state=DISABLED, width=10, command=self.calculate)
        en1 = Entry(root, width=10, bd=3, state=DISABLED, font=("Arial", 10))
        en2 = Entry(root, width=10, bd=3, state=DISABLED, font=("Arial", 10))
        en3 = Entry(root, width=10, bd=3, state=DISABLED, font=("Arial", 10))
        en4 = Entry(root, width=10, bd=3, state=DISABLED, font=("Arial", 10))
        btn1 = Button(root, text="Вікно2", command=Window2, state=DISABLED)
        btn2 = Button(root, text="Вікно3", command=Window3, state=DISABLED)
        btn3 = Button(root, text="Вікно4", command=Window4, state=DISABLED)
        btn4 = Button(root, text="Вікно5", command=Window5, state=DISABLED)
        result.place(x=135, y=225)
        en1.place(x=40, y=160)
        en2.place(x=40, y=210)
        en3.place(x=40, y=260)
        en4.place(x=40, y=310)
        label.place(x=10, y=95)
        label1.place(x=10, y=0)
        rdbtn1.place(x=10, y=70)
        rdbtn2.place(x=100, y=70)
        label3.place(x=10, y=160)
        label4.place(x=10, y=210)
        label5.place(x=10, y=260)
        label6.place(x=10, y=310)
        btn.place(x=160, y=170)
        btn1.place(x=300, y=100)
        btn2.place(x=300, y=150)
        btn3.place(x=300, y=200)
        btn4.place(x=300, y=250)
        root.mainloop()

    def select(self):
        if var.get() == 0:
            label.config(text="Введіть потужності множин та\nінтервал")
            en1.config(state=NORMAL)
            en2.config(state=NORMAL)
            en3.config(state=NORMAL)
            en4.config(state=NORMAL)
            btn.config(text="Згенерувати\nмножини", state=NORMAL)
        else:
            label.config(text="Введіть множини")
            en1.config(state=NORMAL)
            en2.config(state=NORMAL)
            en3.config(state=NORMAL)
            en4.config(state=DISABLED)
            btn.config(state=NORMAL, text="Задавати\nмножину")

    def calculate(self):
        global powA, powB, powC, setA, setB, setC, setU
        if var.get() == 0:
            try:
                powA = int(en1.get())
                powB = int(en2.get())
                powC = int(en3.get())
            except:
                messagebox.showerror("Помилка!", "Неправильно введені дані")
            u = en4.get().split(" ")
            maxvalue = max(powA, powB, powC)
            if len(u) == 2:
                try:
                    u0 = int(u[0])
                    u1 = int(u[1])
                    if u0 > u1 or u1 > 255 or (u1 - u0 < maxvalue):
                        messagebox.showerror("Помилка!", "Неправильно введені дані")
                    else:
                        setU = list(i for i in range(u0, u1 + 1))
                        setA = random.sample(setU, powA)
                        setB = random.sample(setU, powB)
                        setC = random.sample(setU, powC)
                        setU = union(union(setA, setB), setC)
                        btn1.config(state=NORMAL)
                        btn2.config(state=NORMAL)
                        btn3.config(state=NORMAL)
                        btn4.config(state=NORMAL)
                        self.prints()
                except:
                    messagebox.showerror("Помилка", "Неправильно введені дані")
            else:
                messagebox.showerror("Помилка", "Неправильно введені дані")
        else:
            try:
                setA = set(en1.get().split(" "))
                setB = set(en2.get().split(" "))
                setC = set(en3.get().split(" "))
                maxvalue = max(int(max(setA)), int(max(setB)), int(max(setC)))
                minvalue = min(int(min(setA)), int(min(setB)), int(min(setC)))
                if maxvalue <= 255 and minvalue >= 0:
                    setU = union(union(setA, setB), setC)
                    btn1.config(state=NORMAL)
                    btn2.config(state=NORMAL)
                    btn3.config(state=NORMAL)
                    btn4.config(state=NORMAL)
                    self.prints()
                else:
                    messagebox.showerror("Помилка", "Неправильно введені дані")
            except:
                messagebox.showerror("Помилка", "Неправильно введені дані")

    def prints(self):
        global setA, setB, setC, setU
        result.config(text="A: " + str(setA) + "\nB: " + str(setB) + "\nC: " + str(setC) + "\nU: " + str(setU))


class Window2:
    def __init__(self):
        global root2
        root2 = Toplevel(root)
        root2.geometry("500x500")
        root2.title("Вікно 2")
        textLabel = "A: " + str(setA) + "\n\nB: " + str(setB) + "\n\nC: " + str(setC)
        sets = Label(root2, text=textLabel, justify=LEFT, font=("Arial", 12))
        steps = Button(root2, text="Крок ", width=20, font=("Arial", 12), command=self.steps)
        sets.place(x=0, y=0)
        steps.place(x=0, y=125)
        savebtn = Button(root2, text="Зберегти дані", font=("Arial", 12), command=self.savebtn1)
        savebtn.place(x=225, y=125)

    def savebtn1(self):
        global d
        with open(r"Результат вікна 2.txt", "w+") as save1:
            save1.write(d)
            messagebox.showinfo("", "Дані збережені!")

    def steps(self):
        global n, d
        steps1 = [
            '¬A =',
            'C ∪ ¬A =',
            'C ∪ A =',
            '(C ∪ A) ∩ (C ∪ ¬A) =',
            'B \\ ((C ∪ A) ∩ (C ∪ ¬A)) =',
            'A Δ (B \\ ((C ∪ A) ∩ (C ∪ ¬A))) ='
        ]

        res1 = noset(setA, setU)
        res2 = union(setC, res1)
        res3 = union(setC, setA)
        res4 = cross(res3, res2)
        res5 = dif(setB, res4)
        res6 = symdif(setA, res5)

        steps2 = [res1, res2, res3, res4, res5, res6]

        d = "D1 = " + str(sorted(list(res6)))
        if n <= 5:
            if len(steps2[n]) == 0:
                steps2[n] = "ø"
            label1 = Label(root2, text=str(steps1[n]) + str(steps2[n]), font=("Arial", 10))
            label1.place(x=0, y=160 + 25 * n)
            n += 1
        if n == 6:
            if len(steps2[5]) == 0:
                steps2[n] = "ø"
            label1 = Label(root2, text=d, font=("Arial", 10))
            label1.place(x=0, y=160 + 25 * (n + 1))


class Window3:
    def __init__(self):
        global root3
        root3 = Toplevel(root)
        root3.geometry("500x500")
        root3.resizable(False, False)
        root3.title("Вікно 3")
        textLabel = "A: " + str(setA) + "\n\nB: " + str(setB) + "\n\nC: " + str(setC)
        sets = Label(root3, text=textLabel, justify=LEFT, font=("Arial", 12))
        steps = Button(root3, text="Крок ", width=20, font=("Arial", 12), command=self.steps)
        sets.place(x=0, y=0)
        steps.place(x=0, y=125)
        savebtn = Button(root3, text="Зберегти дані", font=("Arial", 12), command=self.savebtn2)
        savebtn.place(x=225, y=125)

    def savebtn2(self):
        global d
        with open(r"Результат вікна 3.txt", "w+") as save2:
            save2.write(d)
            messagebox.showinfo("", "Дані збережені!")

    def steps(self):
        global p, res2
        steps1 = [
            'B \\ C =',
            'A Δ (B \\ C) ='
        ]

        res1 = dif(setB, setC)
        res2 = symdif(setA, res1)

        steps2 = [res1, res2]

        d = "D2 = " + str(sorted(list(res2)))
        if p <= 1:
            if len(steps2[p]) == 0:
                steps2[p] = "ø"
            label1 = Label(root3, text=str(steps1[p]) + str(steps2[p]), font=("Arial", 10))
            label1.place(x=0, y=160 + 25 * p)
            p += 1
        if p == 2:
            if len(steps2[1]) == 0:
                steps2[p] = "ø"
            label1 = Label(root3, text=d, font=("Arial", 10))
            label1.place(x=0, y=160 + 25 * (p + 1))


class Window4:
    def __init__(self):
        global root4, X, Y
        root4 = Toplevel(root)
        root4.title("Вікно 4")
        root4.geometry("500x500")
        root4.resizable(False, False)
        X = setA
        Y = noset(setC, setU)
        textLabel = "X: " + str(X) + "\n\nY: " + str(Y)
        sets = Label(root4, text=textLabel, justify=LEFT, font=("Arial", 12))
        steps = Button(root4, text="Крок", width=20, font=("Arial", 12), command=self.steps)
        sets.place(x=0, y=0)
        steps.place(x=0, y=100)
        savebtn = Button(root4, text="Зберегти дані", font=("Arial", 12), command=self.savebtn3)
        savebtn.place(x=225, y=100)

    def savebtn3(self):
        global z
        with open(r"Результат вікна 4.txt", "w+") as save3:
            save3.write(z)
            messagebox.showinfo("", "Дані збережені!")

    def steps(self):
        global z
        res = symdif(X, Y)
        res = set(res)
        if len(res) == 0:
            res = "ø"
        z = "Z = " + str(sorted(list(res)))
        label1 = Label(root4, text="Z = X Δ Y", font=("Arial", 12))
        label1.place(x=0, y=155)
        label2 = Label(root4, text=z, font=("Arial", 10))
        label2.place(x=0, y=180)


class Window5:
    def __init__(self):
        global root5, btnread1, btnread2, btnread3, btncalc, btncompD, btnresZ, labelw1, labelw2, labelw3, labelw4, \
            labelD, labelZ, X, Y
        X = set(X)
        Y = set(Y)
        root5 = Toplevel(root)
        root5.title("Вікно 5")
        root5.geometry("500x500")
        root5.resizable(False, False)
        labelw1 = Label(root5, text="", font=("Arial", 10))
        labelw1.place(x=0, y=0)
        labelw2 = Label(root5, text="", font=("Arial", 10))
        labelw2.place(x=0, y=50)
        labelD = Label(root5, text="", font=("Arial", 10))
        labelD.place(x=0, y=100)
        labelw3 = Label(root5, text="", font=("Arial", 10))
        labelw3.place(x=0, y=150)
        labelw4 = Label(root5, text="", font=("Arial", 10))
        labelw4.place(x=0, y=200)
        labelZ = Label(root5, text="", font=("Arial", 10))
        labelZ.place(x=0, y=250)
        btnread1 = Button(root5, text="Результат початкового виразу", font=("Arial", 10),
                          command=self.readfile1)
        btnread1.place(x=250, y=100)
        btnread2 = Button(root5, text="Результат спрощеного виразу", font=("Arial", 10),
                          command=self.readfile2)
        btnread2.place(x=250, y=150)
        btncompD = Button(root5, text="Порівняти D", font=("Arial", 10), command=self.compareD)
        btncompD.place(x=250, y=200)
        btnread3 = Button(root5, text="Відобразити множину Z", font=("Arial", 10), command=self.readfile3)
        btnread3.place(x=250, y=250)
        btnresZ = Button(root5, text="Відображення логічної операції Z", font=("Arial", 10), command=self.resultZ)
        btnresZ.place(x=250, y=300)
        btncompZ = Button(root5, text="Порівняти Z", font=("Arial", 10), command=self.compareZ)
        btncompZ.place(x=250, y=350)

    def resultZ(self):
        global X, Y, z2
        z2 = X.symmetric_difference(Y)
        labelw4.config(text="Z2 = " + str(sorted(list(z2))))
        z2 = str(sorted(list(z2)))

    def compareD(self):
        if (len(d1) != 0 and len(d2) != 0):
            if d1 == d2:
                labelD.configure(text="Множини D рівні")
            else:
                labelD.configure(text="Множини D не рівні")
        else:
            labelD.configure(text="Множини D не розраховані")

    def compareZ(self):
        if (len(z1) != 0 and len(z2) != 0):
            if z1 == z2:
                labelZ.configure(text="Множини Z рівні")
            else:
                labelZ.configure(text="Множини Z не рівні")
        else:
            labelZ.configure(text="Множини Z не розраховані")

    def readfile1(self):
        global d1
        read1 = open(r"Результат вікна 2.txt", "r")
        d1 = read1.readline()[5:]
        labelw1.config(text="D1 = " + str(d1))

    def readfile2(self):
        global d2
        read1 = open(r"Результат вікна 3.txt", "r")
        d2 = read1.readline()[5:]
        labelw2.config(text="D2 = " + str(d2))

    def readfile3(self):
        global z1
        read1 = open(r"Результат вікна 4.txt", "r")
        z1 = read1.readline()[4:]
        labelw3.config(text="Z1 = " + str(z1))


Window1()
