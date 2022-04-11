import tkinter as tk
def insert():
    txt.insert(tk.INSERT, entry.get())
def append():
    txt.insert(tk.END, entry.get())
window = tk.Tk()
window.title("打字")
window.geometry("800x600")
entry = tk.Entry()
entry.pack()
btn1 = tk.Button(text="insert", command=insert)
btn1.pack()
btn2 = tk.Button(text="append", command=append)
btn2.pack()
txt = tk.Text()
txt.pack()
window.mainloop()
