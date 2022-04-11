import random
import time

k = random.randint(0,200)               #引入随机变量

print("当前的变量为：",k)

sn0 = int("0015")                       #将基础的sn,不包含设备号和尾号
sn_new = sn0 + 11 * k
sn_new_4 = str(sn_new).zfill(4)         #将获得的sn变为4位数
sn = "1840ODN" + str(sn_new_4) + "00"   #输出16进制的sn

print("当前生成的SN为：",sn)


mac0 = int("6242", 16)                  #将基础的mac转换为10进制，不包含设备号和尾号
mac_new = mac0 + 4 * k
mac1 = "0011328F" + str.upper(format(mac_new,"x"))     #输出16进制的第一个mac
mac2 = "0011328F" + str.upper(format(mac_new+1,"x"))
mac3 = "0011328F" + str.upper(format(mac_new+2,"x"))
mac4 = "0011328F" + str.upper(format(mac_new+3,"x"))

print("当前生成的MAC1为：",mac1)
print("当前生成的MAC2为：",mac2)
print("当前生成的MAC3为：",mac3)
print("当前生成的MAC4为：",mac4)

time.sleep(1800)
