import tkinter
import time
clock = tkinter.Tk()
clock.title("时钟")
clock.geometry("250x30")
while True:
    c = time.ctime().split()
    if c[1] == "Jan":
        c[1] = "1月"
    elif c[1] == "Feb":
        c[1] = "2月"
    elif c[1] == "Mar":
        c[1] = "3月"
    elif c[1] == "Apr":
        c[1] = "4月"
    elif c[1] == "May":
        c[1] = "5月"
    elif c[1] == "Jun":
        c[1] = "6月"
    elif c[1] == "Jul":
        c[1] = "7月"
    elif c[1] == "Aug":
        c[1] = "8月"
    elif c[1] == "Sep":
        c[1] = "9月"
    elif c[1] == "Oct":
        c[1] = "10月"
    elif c[1] == "Nov":
        c[1] = "11月"
    elif c[1] == "Dec":
        c[1] = "12月"
    if c[0] == "Mon":
        c[0] = "星期一"
    elif c[0] == "Tue":
        c[0] = "星期二"
    elif c[0] == "Wed":
        c[0] = "星期三"
    elif c[0] == "Thu":
        c[0] = "星期四"
    elif c[0] == "Fri":
        c[0] = "星期五"
    elif c[0] == "Sat":
        c[0] = "星期六"
    elif c[0] == "Sun":
        c[0] = "星期日"
    a0 = tkinter.Label(clock, text=c[4] + "年" + c[1] + c[2] + "日")
    a0.grid(row=0, column=0)
    a1 = tkinter.Label(clock, text=c[0])
    a1.grid(row=0, column=1)
    a2 = tkinter.Label(clock, text=c[3])
    a2.grid(row=0, column=2)
    clock.update()
