# from tkinter import *
#
# variant = 1629 % 26 + 1
# text = f"П.І,Б: Семенюк Марк Павлович\nМоя група: ІО - 16\nМій номер у групі: 29\nМій варіант: {variant}"
#
#
# class Main:
#     def __init__(self):
#         global text, root1
#         root1 = Tk()
#         root1.title("Вікно 1")
#         root1.geometry("300x200")
#         root1.resizable(False, False)
#         label = Label(root1, text=text, justify=LEFT)
#         label.grid(row=0, column=0)
#         label1 = Label(root1, text="Русский военный корабль", bg="blue", fg="yellow")
#         label2 = Label(root1, text="ІДІ НАХ*Й!", bg="yellow", fg="blue")
#         label1.grid(row=1, column=0, stick="we")
#         label2.grid(row=2, column=0, stick="we")
#
#         mainmenu = Menu(root1)
#         root1.config(menu=mainmenu)
#         mainmenu.add_command(label="Вікно 2", command=self.window2)
#         root1.mainloop()


from tkinter import *
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText
from math import factorial

variant = 1629 % 26 + 1
text = f"П.І,Б: Семенюк Марк Павлович\nМоя група: ІО - 16\nМій номер у групі: 29\nМій варіант: {variant}"

class Main():
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
        global root2
        root2 = Toplevel(root1)
        lbl_data = Label(root2, text="Задайте дані")
        lbl_data.grid(row=0, column=0, columnspan=2)
        lbl_elements_count = Label(root2, text="Кількість елементів")
        self.entry_elements_count = Entry(root2)
        lbl_elements_count.grid(row=1, column=0)
        self.entry_elements_count.grid(row=1, column=1)
        lbl_elements = Label(root2, text="Початкове сполучення")
        self.entry_elements = Entry(root2)
        lbl_elements.grid(row=2, column=0)
        self.entry_elements.grid(row=2, column=1)
        lbl_relations_count = Label(root2, text="Кільксть комбінацій")
        lbl_relations_count.grid(row=3, column=0)
        self.entry_relations_count = Entry(root2, text="Кільксть комбінацій")
        self.entry_relations_count.grid(row=3, column=1)
        btn_result = Button(root2, text="Сформувати сполучення", command=self.input_check)
        btn_result.grid(row=4, column=0, columnspan=2)

    def input_check(self):
        global min_elem, max_elem, elements
        number_relations = int(self.entry_relations_count.get())
        self.count = int(self.entry_elements_count.get())
        try:
            elements = self.entry_elements.get().split(", ")
            for i in range(len(elements)):
                elements[i] = int(elements[i])
            max_elem = max(elements)
            min_elem = min(elements)
        except ValueError:
            tkinter.messagebox.showerror("Помилка!", "Елементи мають бути введені за прикладом: int, int, ..., int")
        if int(self.entry_elements_count.get()) < 32:
            tkinter.messagebox.showerror("Помилка!", "Число n має бути більше за 32")
        elif max_elem > int(self.entry_elements_count.get()) or min_elem < 1:
            tkinter.messagebox.showerror("Помилка!", f"Число n має лежати в межах 0 < n <{self.count}")
        elif number_relations > factorial(len(elements)):
            tkinter.messagebox.showerror("Помилка!", f"число перестановок має бути не більше ніж факторіал потужності"
                                                     f"множини")
        else:
            self.algorithm()

    def algorithm(self):
        elements = self.entry_elements.get().split(", ")
        for i in range(len(elements)):
            elements[i] = int(elements[i])
        number_relations = int(self.entry_relations_count.get())
        lbl_set = Label(root2, text=f'Елементи загальної множини:\n(1, 2, 3, ..., {self.count})')
        lbl_set.grid(row=5, column=0, columnspan=2, rowspan=2)
        lbl_cur_set = Label(root2, text=f'Задана множина: {self.entry_elements.get()}')
        lbl_cur_set.grid(row=6, column=0, columnspan=2, rowspan=2)

        result = []
        temp_set = elements
        for i in range(number_relations):
            stop_1 = 0
            stop_2 = 0
            for j in range(len(elements) - 2, -1, -1):
                print(j)
                if stop_1 == -1:
                    break

                if temp_set[j] < temp_set[j + 1]:
                    for k in range(len(elements) - 1, j - 1, -1):
                        if stop_2 == -1:
                            break
                        counter = 0
                        if temp_set[j] < temp_set[k]:
                            temp_elem = temp_set[j]
                            temp_set[j] = temp_set[k]
                            temp_set[k] = temp_elem
                            temp_set_cut = temp_set[j + 1:len(elements)]
                            temp_set_cut.reverse()
                            for v in range(j + 1, len(temp_set)):
                                temp_set[v] = temp_set_cut[counter]
                                counter += 1
                                stop_1 = -1
                                stop_2 = -1
                            result.append(tuple(temp_set))
                            break
        str_output = ""
        for i in result:
            str_output += str(i)
            str_output += "\n"
        result_output = ScrolledText(root2, width=30, height=10)
        result_output.insert("1.0", f"{str_output}")
        result_output.grid(row=7, column=0, columnspan=2)


if __name__ == "__main__":
    Main()
