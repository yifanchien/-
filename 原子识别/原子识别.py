import tkinter


def cc():
    if int(eca.get()) <= 94 and int(eca.get()) != 61:
        if not ((eca.get() == 0 and ecb.get() == 0) or (eca.get() == 0 and ecc.get() == 0) or (
                ecb.get() == 0 and ecc.get() == 0)):
            if eca.get() == ecc.get():
                n = v[int(eca.get())]
                gg.config(text="%s-%s" % (n, int(eca.get()) + int(ecb.get())))
            elif int(eca.get()) > int(ecc.get()):
                n = v[int(eca.get())]
                gg.config(text="%s离子(+)" % n)
            elif int(eca.get()) < int(ecc.get()):
                n = v[int(eca.get())]
                gg.config(text="%s离子(-)" % n)
        else:
            if eca.get() == 0 and ecb.get() == 0:
                gg.config(text="单个电子")
            elif eca.get() == 0 and ecc.get() == 0:
                gg.config(text="单个中子")
            else:
                gg.config(text="单个质子")
    else:
        gg.config(text="无效输入!")

v = {1: "氢", 2: "氦", 3: "锂", 4: "铍", 5: "硼", 6: "碳", 7: "氮", 8: "氧", 9: "氟", 10: "氖", 11: "钠", 12: "镁", 13: "铝", 14: "硅", 15: "磷", 16: "硫", 17: "氯", 18: "氩", 19: "钾", 20: "钙", 21: "钪", 22: "钛", 23: "钒", 24: "铬", 25: "锰", 26: "铁", 27: "钴", 28: "镍", 29: "铜", 30: "锌", 31: "镓", 32: "锗", 33: "砷", 34: "硒", 35: "溴", 36: "氪", 37: "铷", 38: "锶", 39: "钇", 40: "锆", 41: "铌", 42: "钼", 43: "锝", 44: "钌", 45: "铑", 46: "钯", 47: "银", 48: "镉", 49: "铟", 50: "锡", 51: "锑", 52: "碲", 53: "碘", 54: "氙", 55: "铯", 56: "钡", 57: "镧", 58: "铈", 59: "镨", 60: "钕", 62: "钐", 63: "铕", 64: "钆", 65: "铽", 66: "镝", 67: "钬", 68: "铒", 69: "铥", 70: "镱", 71: "镥", 72: "铪", 73: "钽", 74: "钨", 75: "铼", 76: "锇", 77: "铱", 78: "铂", 79: "金", 80: "汞", 81: "铊", 82: "铅", 83: "铋", 84: "钋", 85: "砹", 86: "氡", 87: "钫", 88: "镭", 89: "锕", 90: "钍", 91: "镤", 92: "铀", 93: "镎", 94: "钚"}
tk2 = tkinter.Tk()
tk2.title("自然界原子、离子识别")
eca = tkinter.Entry(tk2)
eca.grid(row=0, column=1)
lca = tkinter.Label(tk2, text="核内质子数:")
lca.grid(row=0, column=0)
ecb = tkinter.Entry(tk2)
ecb.grid(row=0, column=3)
lcb = tkinter.Label(tk2, text="核内中子数:")
lcb.grid(row=0, column=2)
ecc = tkinter.Entry(tk2)
ecc.grid(row=0, column=5)
lcc = tkinter.Label(tk2, text="核外电子数:")
lcc.grid(row=0, column=4)
bb = tkinter.Button(tk2, text="输出", command=cc)
bb.grid(row=1, column=2)
gg = tkinter.Label(tk2, text="")
gg.grid(row=1, column=4)
tk2.mainloop()
