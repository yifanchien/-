from tkinter import *
import random
ww = Frame(bg="grey", width=200, height=120)
ww.pack()
ww.master.geometry("370x200")
ww.master.resizable(0, 0)
ww.master.title("猜拳游戏")
la2 = Label(ww, text="显示", bg="yellow")
la2.pack()
la1 = Label(ww, text="显示输赢", bg="yellow")
la1.pack()

def pe(ut):
    os = ["石头", "剪子", "布"]
    if ut in os:
        pct = random.choice(os)
        print(f"用户:{ut},电脑:{pct}")
        la2.config(text=f"用户:{ut},电脑:{pct}")
        if ut == pct:
            la1.config(text="平局")
        elif (ut == "石头" and pct == "剪子") or (ut == "剪子" and pct == "布") or (ut == "布" and pct == "石头"):
            print("你赢了")
            la1.config(text="你赢了")
        else:
            print("你输了")
            la1.config(text="你输了")
    else:
        print("输入不合法")
f1 = Frame(ww)
f1.pack()
bk = Button(f1, text="石头", command=lambda: pe("石头"), width=5)
bk.grid(row=0, column=0)
bk = Button(f1, text="剪子", command=lambda: pe("剪子"), width=5)
bk.grid(row=0, column=1)
bk = Button(f1, text="布", command=lambda: pe("布"), width=5)
bk.grid(row=0, column=2)
ww.mainloop()