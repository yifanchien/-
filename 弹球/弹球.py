import tkinter
import time
pad_x, pad_y, pad1_x, pad1_y, pad2_x, pad2_y, pad3_x, pad3_y = 4, 3, 3, 4, 3, 3, 4, 4
tk = tkinter.Tk()
tk.title("弹球")
canvas = tkinter.Canvas(tk, width=1000, height=500)
canvas.pack()
ball, ball1, ball2, ball3 = canvas.create_oval(280, 400, 250, 370, fill="red"), canvas.create_oval(220, 400, 190, 370, fill="red"), canvas.create_oval(180, 400, 150, 370, fill="red"), canvas.create_oval(100, 400, 70, 370, fill="red")
while True:
    pos, pos1, pos2, pos3 = canvas.coords(ball), canvas.coords(ball1), canvas.coords(ball2), canvas.coords(ball3)
    if pos[2] > 1000 or pos[0] < 0:
        pad_x = -pad_x
    if pos[1] < 0 or pos[3] > 500:
        pad_y = -pad_y
    if pos1[2] > 1000 or pos1[0] < 0:
        pad1_x = -pad1_x
    if pos1[1] < 0 or pos1[3] > 500:
        pad1_y = -pad1_y
    if pos2[2] > 1000 or pos2[0] < 0:
        pad2_x = -pad2_x
    if pos2[1] < 0 or pos2[3] > 500:
        pad2_y = -pad2_y
    if pos3[2] > 1000 or pos3[0] < 0:
        pad3_x = -pad3_x
    if pos3[1] < 0 or pos3[3] > 500:
        pad3_y = -pad3_y
    canvas.move(ball, pad_x, pad_y), canvas.move(ball1, pad1_x, pad1_y), canvas.move(ball2, pad2_x, pad2_y), canvas.move(ball3, pad3_x, pad3_y), tk.update(), time.sleep(0.01)
