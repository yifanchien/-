from tkinter import *


class Calc(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidget()
        self.pack()

    def press_btn(self, btnval):
        self.__e.insert(END, btnval)

    def get_result(self):
        result = eval(self.__e.get())
        self.__e.delete(0, END)
        self.__e.insert(INSERT, result)

    def k(self):
        self.__e.delete(0, END)

    def createWidget(self):
        self.__e = Entry(self)
        self.__e.pack(side="top")
        self.__btnFrame = Frame(self)
        self.__btnFrame.pack(side="bottom")
        listbtn = []
        listbtn.append(["7", "8", "9", "/"])
        listbtn.append(["4", "5", "6", "*"])
        listbtn.append(["1", "2", "3", "-"])
        listbtn.append(["0", ".", "+"])
        btn = Button(self.__btnFrame, text="7", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("7"))
        btn.grid(row=1, column=0)
        btn = Button(self.__btnFrame, text="8", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("8"))
        btn.grid(row=1, column=1)
        btn = Button(self.__btnFrame, text="9", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("9"))
        btn.grid(row=1, column=2)
        btn = Button(self.__btnFrame, text="/", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("/"))
        btn.grid(row=1, column=3)
        btn = Button(self.__btnFrame, text="4", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("4"))
        btn.grid(row=2, column=0)
        btn = Button(self.__btnFrame, text="5", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("5"))
        btn.grid(row=2, column=1)
        btn = Button(self.__btnFrame, text="6", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("6"))
        btn.grid(row=2, column=2)
        btn = Button(self.__btnFrame, text="*", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("*"))
        btn.grid(row=2, column=3)
        btn = Button(self.__btnFrame, text="1", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("1"))
        btn.grid(row=3, column=0)
        btn = Button(self.__btnFrame, text="2", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("2"))
        btn.grid(row=3, column=1)
        btn = Button(self.__btnFrame, text="3", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("3"))
        btn.grid(row=3, column=1)
        btn = Button(self.__btnFrame, text="0", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("0"))
        btn.grid(row=3, column=2)
        btn = Button(self.__btnFrame, text="-", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("-"))
        btn.grid(row=3, column=3)
        btn = Button(self.__btnFrame, text=".", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("."))
        btn.grid(row=4, column=0)
        btn = Button(self.__btnFrame, text="+", width=20, height=4, padx=1, pady=1, command=lambda: self.press_btn("+"))
        btn.grid(row=4, column=3)
        btnResult = Button(self.__btnFrame, text="=", width=20, height=4, padx=1, pady=1, command=self.get_result)
        btnResult.grid(row=4, column=1, columnspan=4)
        btnResulk = Button(self.__btnFrame, text="C", width=20, height=4, padx=1, pady=1, command=self.k)
        btnResulk.grid(row=4, column=0, columnspan=3)
mycalc = Calc()
mycalc.master.title("?????????????????????")
mycalc.master.geometry("1000x600")
mycalc.mainloop()
