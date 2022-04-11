import tkinter
tk = tkinter.Tk()

def insert():
    deno(entry.get(),entry2.get())
def deno(y, mb):
    import urllib.request
    h = urllib.request.urlopen(y)
    hk = h.read()
    f = open(mb, "wb")
    f.write(hk)
    f.close()


tk.geometry("400x100")
label = tkinter.Label(text="原文件网址")
label.grid(row=4, column=1)
label2 = tkinter.Label(text="目标文件名")
label2.grid(row=5, column=1)
entry = tkinter.Entry()
entry.grid(row=4, column=2)
entry2 = tkinter.Entry()
entry2.grid(row=5, column=2)
btn1 = tkinter.Button(text="下载", command=insert)
btn1.grid(row=6, column=2)
tk.mainloop()




# http://123.57.67.154/media/paper/21ke/21ke_615/ke615catchingshrimp.mp3
# http://123.57.67.154/media/paper/21ke/21ke_615/ke615swimminginabus.mp3
# http://123.57.67.154/media/paper/21ke/21ke_615/ke615funworld.mp3
# http://123.57.67.154/media/paper/21ke/21ke_615/ke615theholeinyourplastic.mp3
# http://123.57.67.154/media/paper/21ke/21ke_615/ke615havefunwash.mp3
# http://123.57.67.154/media/paper/21ke/21ke_615/ke615whichflower.mp3
# http://123.57.67.154/media/paper/21ke/21ke_615/ke615youlook.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616russiasspace.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616librarywheels.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616funworld.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616howdophone.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616isthisgrowup.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616flyingcartakes.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616whyshould.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616thankyou.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616notjustfruit.mp3
# http://123.57.67.154/media/paper/21ke/21ke_616/ke616muchameetschina.mp3














# import urllib.request
# import urllib.parse
# import re
# from bs4 import BeautifulSoup
#
#
# def main():
#     keyword = input("请输入关键词\n")
#     keyword = urllib.parse.urlencode({"word": keyword})
#     response = urllib.request.urlopen(f"http://123.57.67.154/media/paper/21ke{keyword}")
#     html = response.read()
#     soup = BeautifulSoup(html, "html.parser")
#     for each in soup.find_all(href = re.compile(""))
