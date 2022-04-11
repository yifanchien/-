# -*-coding:utf-8-*-
import tkinter as tk
from tkinter import *
import time
from PIL import ImageTk, Image
class Window:
    def __init__(self):
        self.name = None
        with open("saves.txt",encoding='UTF-8') as f:
            self.save_s = eval(f.read())
    

    def moverectangle1(self):
        self.canas.move(self.me_r, 0, -5)
    def moverectangle2(self):
        self.canas.move(self.me_r, 0, 5)
    def moverectangle3(self):
        self.canas.move(self.me_r, -5, 0)
    def moverectangle4(self):
        self.canas.move(self.me_r, 5, 0)
    
    
    
    def world(self):
        self.world_s = tk.Tk()
        self.canas = Canvas(self.world_s, width = 1000, height = 1000)
        self.canas.pack()
        self.me_r = self.canas.create_rectangle(180,180,190,190,fill="red")
        self.canas.bind_all("<Up>",command=self.moverectangle1)
        self.canas.bind_all("<Down>",command=self.moverectangle2)
        self.canas.bind_all("<Left>",command=self.moverectangle3)
        self.canas.bind_all("<Right>",command=self.moverectangle4)
        self.world_s.mainloop()
    
    
    
    
    def get_user_infor(self):
        return self.save_s[self.name]["energy"]*self.save_s[self.name]["things"][0],self.save_s[self.name]["speed"]*self.save_s[self.name]["things"][1],self.save_s[self.name]["attack"]*self.save_s[self.name]["things"][2]
    def quituiuiui(self):
        with open("saves.txt","r",encoding='UTF-8') as f:
            a = eval(f.read())
        a[self.name]["energy"] = int(self.spin1.get())
        a[self.name]["speed"] = int(self.spin2.get())
        a[self.name]["attack"] = int(self.spin3.get())
        with open("saves.txt","w",encoding='UTF-8') as f:
            f.write(str(a))
        self.set_cur.destroy()
        self.curtain = tk.Tk()
        self.curtain.title('curtain')
        self.b_number_dict = " ".join(list(map(str,self.get_user_infor())))
        self.a = tk.Label(self.curtain,text=self.name)
        self.b = tk.Label(self.curtain,text=self.b_number_dict)
        self.c = tk.Button(self.curtain,text="set property",command=self.set_)
        self.d = tk.Button(self.curtain,text="The entrance to the world",command=self.world)
        self.e = tk.Button(self.curtain,text="quit",command=self.l_5444741)
        self.a.grid(row=0,column=0)
        self.b.grid(row=1,column=0)
        self.c.grid(row=1,column=1)
        self.d.grid(row=2,column=0)
        self.e.grid(row=2,column=1)
        self.curtain.mainloop()
    def quitu(self):
        self.asdfh = self.save_s[self.name]["all_energy"]-int(self.spin1.get())-int(self.spin2.get())-int(self.spin3.get())
        self.all_po['text'] = f"SKILL POINTS UNASSIGNED: {self.asdfh}"
        self.spin1['to'] = self.asdfh+int(self.spin1.get())
        self.spin2['to'] = self.asdfh+int(self.spin2.get())
        self.spin3['to'] = self.asdfh+int(self.spin3.get())
    def set_(self):
            self.curtain.destroy()
            self.set_cur = tk.Tk()
            self.asdfh = self.save_s[self.name]["all_energy"]
            self.all_po = tk.Label(self.set_cur,text=f"SKILL POINTS UNASSIGNED: {self.asdfh}")
            self.spin1 = tk.Spinbox(self.set_cur, from_=0, to=self.asdfh)
            self.spin2 = tk.Spinbox(self.set_cur, from_=0, to=self.asdfh)
            self.spin3 = tk.Spinbox(self.set_cur, from_=0, to=self.asdfh)
            self.sp1n = tk.Label(self.set_cur,text="energy")
            self.sp2n = tk.Label(self.set_cur,text="speed")
            self.sp3n = tk.Label(self.set_cur,text="attack")
            self.boooooo = tk.Button(self.set_cur,text="set",command=self.quituiuiui)
            self.tnhuhbgin = tk.Button(self.set_cur,text="update(Click once for each set)",command=self.quitu)
            self.all_po.grid(row=0,column=0)
            self.sp1n.grid(row=1,column=0)
            self.spin1.grid(row=1,column=1)
            self.sp2n.grid(row=2,column=0)
            self.spin2.grid(row=2,column=1)
            self.sp3n.grid(row=3,column=0)
            self.spin3.grid(row=3,column=1)
            self.boooooo.grid(row=5,column=0)
            self.tnhuhbgin.grid(row=4,column=0)
            self.set_cur.mainloop()
    def l_5444741(self):
        self.curtain.destroy()
        self.main()
    def goi(self):
        self.window.destroy()
        self.curtain = tk.Tk()
        self.curtain.title('curtain')
        self.b_number_dict = " ".join(list(map(str,self.get_user_infor())))
        self.a = tk.Label(self.curtain,text=self.name)
        self.b = tk.Label(self.curtain,text=self.b_number_dict)
        self.c = tk.Button(self.curtain,text="set property",command=self.set_)
        self.d = tk.Button(self.curtain,text="The entrance to the world",command=self.world)
        self.e = tk.Button(self.curtain,text="quit",command=self.l_5444741)
        self.a.grid(row=0,column=0)
        self.b.grid(row=1,column=0)
        self.c.grid(row=1,column=1)
        self.d.grid(row=2,column=0)
        self.e.grid(row=2,column=1)
        self.curtain.mainloop()

    def quit_register(self):
        self.aw.destroy()
        self.register.destroy()
        self.main()
    def quit_register_2(self):
        self.aw2.destroy()
        self.registration.destroy()
        self.main()
    
    
    def reg(self):
            with open("user_name.txt","r",encoding='UTF-8') as f:
                self.fr = eval(f.read())
            if self.ue.get() in self.fr:
                if self.pe.get() == self.fr[self.ue.get()]:
                    self.name = self.ue.get()
                    self.aw = tk.Tk()
                    self.label = tk.Label(self.aw,text='login successfully')
                    self.label.pack()
                    self.b2 = tk.Button(self.aw,text="quit",command=self.quit_register)
                    self.b2.pack()
                    self.aw.mainloop()
                else:
                    self.aw = tk.Tk()
                    self.label = tk.Label(self.aw,text='wrong password')
                    self.label.pack()
                    self.b2 = tk.Button(self.aw,text="quit",command=self.quit_register)
                    self.b2.pack()
                    self.aw.mainloop()
            else:
                self.aw = tk.Tk()
                self.label = tk.Label(self.aw,text='There is no such user name')
                self.label.pack()
                self.b2 = tk.Button(self.aw,text="quit",command=self.quit_register)
                self.b2.pack()
                self.aw.mainloop()
    def reg_str(self):
        if (self.ue2.get() == self.ue3.get()) and (self.pe2.get() == self.pe3.get()):
            with open("user_name.txt","r",encoding='UTF-8') as f:
                self.fdg = eval(f.read())
            if self.ue2.get() not in self.fdg:
                with open("users.txt","r",encoding='UTF-8') as f:
                    self.fd = eval(f.read())
                with open("saves.txt","r",encoding='UTF-8') as f:
                    self.hggh = eval(f.read())
                self.fdg[self.ue2.get()] = self.pe2.get()
                self.fd[self.ue2.get()] = [0,"","",[]]
                self.hggh[self.ue2.get()] = {"all_energy":1,"energy":1,"speed":0,"attack":0,"things":[1,1,1]}
                with open("user_name.txt","w",encoding='UTF-8') as f:
                    f.write(str(self.fdg))
                with open("users.txt","w",encoding='UTF-8') as f:
                    f.write(str(self.fd))
                with open("saves.txt","w",encoding='UTF-8') as f:
                    f.write(str(self.hggh))
                self.name = self.ue2.get()
                self.aw2 = tk.Tk()
                self.label2 = tk.Label(self.aw2,text="Registration Successful")
                self.label2.pack()
                self.bb = tk.Button(self.aw2,text="quit",command=self.quit_register_2)
                self.bb.pack()
                self.aw2.mainloop()
            else:
                self.aw2 = tk.Tk()
                self.label2 = tk.Label(self.aw2,text="Registration Failure")
                self.label2.pack()
                self.bb = tk.Button(self.aw2,text="quit",command=self.quit_register_2)
                self.bb.pack()
                self.aw2.mainloop()
        else:
            self.aw2 = tk.Tk()
            self.label2 = tk.Label(self.aw2,text="This username is already registered")
            self.label2.pack()
            self.bb = tk.Button(self.aw2,text="quit",command=self.quit_register_2)
            self.bb.pack()
            self.aw2.mainloop()
    
    
    def regist(self):# 登录主函数
        self.window.destroy()
        self.register = tk.Tk()
        self.register.title('Register')
        self.ul = tk.Label(self.register,text='User name:')
        self.ue = tk.Entry(self.register)
        self.pl = tk.Label(self.register,text='Password:')
        self.pe = tk.Entry(self.register)
        self.b1 = tk.Button(self.register,text="Register",command=self.reg)
        self.ul.grid(row=0,column=0)
        self.ue.grid(row=0,column=1)
        self.pl.grid(row=1,column=0)
        self.pe.grid(row=1,column=1)
        self.b1.grid(row=2,column=1)
        self.register.mainloop()
    def registr(self):# 注册主函数
        self.window.destroy()
        self.registration = tk.Tk()
        self.registration.title('Registration')
        self.ul2 = tk.Label(self.registration,text='User name:')
        self.ue2 = tk.Entry(self.registration)
        self.pl2 = tk.Label(self.registration,text='Password:')
        self.pe2 = tk.Entry(self.registration)
        self.ul3 = tk.Label(self.registration,text='Confirm user name:')
        self.ue3 = tk.Entry(self.registration)
        self.pl3 = tk.Label(self.registration,text='Confirm password:')
        self.pe3 = tk.Entry(self.registration)
        self.b12 = tk.Button(self.registration,text="Registration",command=self.reg_str)
        self.ul2.grid(row=0,column=0)
        self.ue2.grid(row=0,column=1)
        self.pl2.grid(row=1,column=0)
        self.pe2.grid(row=1,column=1)
        self.ul3.grid(row=2,column=0)
        self.ue3.grid(row=2,column=1)
        self.pl3.grid(row=3,column=0)
        self.pe3.grid(row=3,column=1)
        self.b12.grid(row=4,column=1)
        self.registration.mainloop()


    def change_things(self):
        with open("users.txt","r",encoding='UTF-8') as f:
            self.infor = eval(f.read())
        self.u_information[1] = self.sex.get()
        self.u_information[2] = self.names.get()
        self.u_information[3] = self.other.get().split()
        self.infor[self.name] = self.u_information
        with open("users.txt","w",encoding='UTF-8') as f:
            f.write(str(self.infor))
        self.main()
    def complete_information(self):
        self.window.destroy()
        with open("users.txt","r",encoding='UTF-8') as f:
            self.u_information = eval(f.read())
        self.u_information = self.u_information[self.name]
        self.information_c = tk.Tk()
        self.information_c.title('information')
        self.um = tk.Label(self.information_c,text=f"user name: {self.name}")
        self.level = tk.Label(self.information_c,text=f"level: lv.{self.u_information[0]//10}")
        self.points = tk.Label(self.information_c,text=f"points: {self.u_information[0]}")
        self.se = tk.Label(self.information_c,text="sex:")
        self.sex = tk.Entry(self.information_c)
        self.sex.insert(0,f"{self.u_information[1]}")
        self.nam = tk.Label(self.information_c,text="real name: ")
        self.names = tk.Entry(self.information_c)
        self.names.insert(0,f"{self.u_information[2]}")
        self.other = tk.Entry(self.information_c)
        self.other.insert(0," ".join(self.u_information[3]))
        self.boo = tk.Button(self.information_c,text="change information",command=self.change_things)
        
        self.um.grid(row=0,column=0)
        self.level.grid(row=1,column=0)
        self.points.grid(row=2,column=0)
        self.se.grid(row=3,column=0)
        self.sex.grid(row=3,column=1)
        self.nam.grid(row=4,column=0)
        self.names.grid(row=4,column=1)
        self.other.grid(row=5,column=1)
        self.boo.grid(row=6,column=1)
        self.information_c.mainloop()


    def main(self):
            self.window = tk.Tk()
            self.window.title('window')
            if self.name != None:
                with open("users.txt","r",encoding='UTF-8') as f:
                    ab = eval(f.read())
                self.user_information = tk.Label(self.window,text=f"{self.name}({ab[self.name][2]})\nlevel: lv.{ab[self.name][0]//10}\npoints: {ab[self.name][0]}\nsex: {ab[self.name][1]}\n{' '.join(ab[self.name][3])}")
                self.user_information.grid(row=0,column=0)
                self.boot1 = tk.Button(self.window,text="change your information",command=self.complete_information)
                self.boot2 = tk.Button(self.window,text="Registration",command=self.registr)
                self.boot3 = tk.Button(self.window,text="Register",command=self.regist)
                self.boot1.grid(row=0,column=1)
                self.boot2.grid(row=1,column=1)
                self.boot3.grid(row=2,column=1)
                self.go_in = tk.Button(self.window,text="start",command=self.goi)
                self.go_in.grid(row=1,column=0)
            else:
                self.user_information = tk.Label(self.window,text="Not logged in")
                self.user_information.grid(row=0,column=0)
                self.boot2 = tk.Button(self.window,text="Registration",command=self.registr)
                self.boot3 = tk.Button(self.window,text="Register",command=self.regist)
                self.boot2.grid(row=0,column=1)
                self.boot3.grid(row=1,column=1)
            self.window.mainloop()
block = Window()
block.main()