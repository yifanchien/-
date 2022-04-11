import tkinter as tk
def m():
    M.config(text="""【水星】
英文名：Mercury
水星基本参数：
轨道半长径： 5791万 千米 (0.38 天文单位)
公转周期： 87.70 天
平均轨道速度： 47.89 千米/每秒
轨道偏心率： 0.206
轨道倾角： 7.0 度
行星赤道半径： 2440 千米
质量(地球质量＝1)： 0.0553
密度： 5.43 克/立方厘米
自转周期： 58.65 日
卫星数： 无
公转轨道: 距太阳 57,910,000 千米 
        (0.38 天文单位)""", width=35, height=20)
def v():
    V.config(text="""【金星】
英文名：Venus
金星基本参数
公转周期： 224.701天
平均轨道速度： 35.03 千米/每秒
轨道偏心率： 0.007
轨道倾角： 3.4 度
赤道直径： 12,103.6千米
质量(地球质量＝1)： 0.8150
密度： 5.24 克/立方厘米
自转周期： 243.01 日
卫星数量: 0
公转半径： 108,208,930 km(0.72 天文单位)
表面面积 4.6亿 平方千米
表面引力 8.78 m/s2
自传时间 -243.02天
逃逸速度 10.4 千米/秒
表面温度 最低 平均 最高
737K 750K 773K""", width=35, height=20)
def e():
    E.config(text="""【地球】
英文:earth
轨道半径: 149,600,000 千米 
(离太阳1.00 天文单位)
行星直径: 12,756.3 千米
质量: 5.9736e24 千克
赤道引力(地球=1) 1.00
逃逸速度(公里/秒) 11.2
自转周期(日) 0.9973
黄赤交角(度) 23.44
反照率 0.30
卫星数：1（月球）""", width=35, height=20)
def ma():
    Ma.config(text="""【火星】
英文名: Mars
火星基本参数：
轨道半长径： 22794万 千米 (1.52 天文单位)
公转周期： 686.98 日
平均轨道速度： 24.13 千米/每秒
轨道偏心率： 0.093
轨道倾角： 1.8 度
行星赤道半径： 3398 千米
质量(地球质量＝1)： 0.1074
密度： 3.94 克/立方厘米
自转周期： 1.026 日
卫星数： 2
公转轨道: 离太阳227,940,000 千米 
       (1.52 天文单位)""", width=35, height=20)
def j():
    J.config(text="""【木星】
英文名: Jupiter
公转轨道: 距太阳 778,330,000 千米 
      (5.20 天文单位)
行星直径: 142,984 千米 (赤道)
质量: 1.900e27 千克
卫星: 四颗卫星：木卫一，木卫二，
木卫三和木卫四。
（现常被称作伽利略卫星）""", width=35, height=20)
def s():
    S.config(text="""【土星】
英文名: Saturn
公转轨道: 距太阳 1,429,400,000 千米
       (9.54 天文单位)
卫星直径: 120,536 千米 (赤道)
质量: 5.68e26 千克
卫星: 土星有18颗被命名的卫星，
还有一些小卫星还将被发现。""", width=35, height=20)
def u():
    U.config(text="""【天王星】
英文名: Uranus
公转轨道: 距太阳2,870,990,000 千米 
        (19.218 天文单位)
行星直径: 51,118 千米（赤道）
质量: 8.683e25 千克
卫星: 天王星有15颗已命名的卫星，
以及2颗已发现但暂未命名的卫星。""", width=35, height=20)
def n():
    N.config(text="""【海王星】
英文名: Neptune
公转轨道: 距太阳 4,504,000,000 千米 
       (30.06 天文单位)
行星直径: 49,532 千米（赤道）
质量: 1.0247e26 千克
卫星: 海王星有9颗已知卫星：
8颗小卫星和海卫一。""", width=35, height=20)
def f():
    M.config(text="Mercury")
    V.config(text="Venus")
    E.config(text="Earth")
    Ma.config(text="Mars")
    J.config(text="Jupiter")
    S.config(text="Saturn")
    U.config(text="Uranus")
    N.config(text="Neptune")
    Su.config(text="Sun")
def su():
    Su.config(text="""英文名:Sun
质量:1.9891×10³⁰ kg 
平均密度:1.408×10³ kg/㎥ 
直径:1.392×10⁶ km 
表面温度:5770K 
逃逸速度:617.7 km/s 
视星等:（V）-26.74 
绝对星等:4.83 
自转周期:25.05天 
赤经:286.13° 
赤纬:+63.87° 
距地距离:1.496×10⁸ km 
公转周期:（2.25-2.50）×10⁸ a 
半径:6.955×10⁵ km """)
def mf():
    M.config(text="Mercury")
def vf():
    V.config(text="Venus")
def ef():
    E.config(text="Earth")
def maf():
    Ma.config(text="Mars")
def jf():
    J.config(text="Jupiter")
def sf():
    S.config(text="Saturn")
def uf():
    U.config(text="Uranus")
def nf():
    N.config(text="Neptune")
def suf():
    Su.config(text="Sun")
window = tk.Tk()
window.title("太阳系简介")
window.geometry("1900x1000")
M = tk.Button(text="Mercury", command=m, width=35, height=20)
M.grid(row=0, column=0)
V = tk.Button(text="Venus", command=v, width=35, height=20)
V.grid(row=0, column=1)
E = tk.Button(text="Earth", command=e, width=35, height=20)
E.grid(row=0, column=2)
Ma = tk.Button(text="Mars", command=ma, width=35, height=20)
Ma.grid(row=0, column=3)
J = tk.Button(text="Jupiter", command=j, width=35, height=20)
J.grid(row=2, column=0)
S = tk.Button(text="Saturn", command=s, width=35, height=20)
S.grid(row=2, column=1)
U = tk.Button(text="Uranus", command=u, width=35, height=20)
U.grid(row=2, column=2)
N = tk.Button(text="Neptune", command=n, width=35, height=20)
N.grid(row=2, column=3)
Su = tk.Button(text="Sun", command=su, width=35, height=20)
Su.grid(row=0, column=5)
ldxx = tk.Label(text="类地行星")
ldxx.grid(row=0, column=4)
lmxx = tk.Label(text="类木行星")
lmxx.grid(row=2, column=4)
hx = tk.Label(text="恒星")
hx.grid(row=0, column=6)
F = tk.Button(text="全部返回", command=f)
F.grid(row=3, column=5)
MF = tk.Button(text="Mercury返回", command=mf)
MF.grid(row=1, column=0)
VF = tk.Button(text="Venus返回", command=vf)
VF.grid(row=1, column=1)
EF = tk.Button(text="Earth返回", command=ef)
EF.grid(row=1, column=2)
MaF = tk.Button(text="Mars返回", command=maf)
MaF.grid(row=1, column=3)
JF = tk.Button(text="Jupiter返回", command=jf)
JF.grid(row=3, column=0)
SF = tk.Button(text="Saturn返回", command=sf)
SF.grid(row=3, column=1)
UF = tk.Button(text="Uranus返回", command=uf)
UF.grid(row=3, column=2)
NF = tk.Button(text="Neptune返回", command=nf)
NF.grid(row=3, column=3)
SuF = tk.Button(text="Sun返回", command=suf)
SuF.grid(row=1, column=5)
window.mainloop()
