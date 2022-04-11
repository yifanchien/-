with open("users.txt","r") as f:
    users = eval(f.read())
def PASSWORD(str2):
    str3 = input(">>>password\n:")
    if users[str2] == str3:
        print(">>>Let's start")
        print("===================================================================================================")
        print("\n")
        return 1
    else:
        str4 = input(">>>sign in?(y/n)\n")
        if str4 == "y":
            return 2
        return 0
def ALL_GETIN():
    import time
    print("=========================================SPACE SIMULATION==========================================")
    print("\n")
    str1 = input(">>>r/s\n:")
    if str1 == "r":
        str2 = input(">>>please enter you user name\n:")
        if str2 in users:
            showe = 0
            while showe == 0:
                showe = PASSWORD(str2)
            if showe == 2:
                str5 = input(">>>please enter you user name\n:")
                str6 = input(">>>please enter you password\n:")
                users[str5] = str6
                print(">>>Let's start")
                print("===================================================================================================")
                print("\n")
        else:
            print(">>>switchover to sign in.")
            str5 = input(">>>please enter you user name\n:")
            str6 = input(">>>please enter you password\n:")
            users[str5] = str6
            print(">>>Let's start")
            print("===================================================================================================")
            print("\n")
    else:
            str5 = input(">>>please enter you user name\n:")
            str6 = input(">>>please enter you password\n:")
            users[str5] = str6
            print(">>>Let's start")
            print("===================================================================================================")
            print("\n")
    with open("users.txt","w") as f:
        f.write(str(users))
ALL_GETIN()
import random
import numpy as np
import matplotlib.pyplot as plt
BIGBOOK_FIGHT = {}
DIEBOOK = []
J_LIST = []
R_LIST = []
S_LIST = []
ALL_LIST = []
LEN = []
MY_DHE = "0123456789abcdefghijklmnopqrstuvwxyz"
MY = {}
for i in range(len(MY_DHE)):
    MY[MY_DHE[i]] = i
def MY_to_int(MYZ,K = 36):
    MYZ = str(MYZ)
    INT = 0
    while len(MYZ):
        INT += MY[MYZ[0]]*(K**(len(MYZ)-1))
        MYZ = MYZ[1:]
    return INT
def int_to_MY(INT,K = 36):
    INT = int(INT)
    MYZ = ""
    while INT:
        MYZ = MY_DHE[INT%K]+MYZ
        INT = INT//K
    return MYZ
FIGHT_MESSAGE = {}
def find_max_min(list_for_find):
    new_list = []
    for i in list_for_find:
        new_list.append(MY_to_int(i))
    if new_list == []:
        return [[None,None],[None,None]],[[None,None],[None,None]],None
    return [[max(new_list),int_to_MY(max(new_list))],[min(new_list),int_to_MY(min(new_list))]],len(new_list)
def create_ex(EX_NUMBER,SPACE_SIZE_XY,J_feature,R_feature,S_feature):
    SPACE = {}
    for i in range(EX_NUMBER):
        X,Y,C,CLASS = int_to_MY(random.randint(0,SPACE_SIZE_XY[0][0])),int_to_MY(random.randint(0,SPACE_SIZE_XY[0][1])),int_to_MY(random.randint(SPACE_SIZE_XY[1][0],SPACE_SIZE_XY[1][1])),random.choices(["J","R","S"])[0]
        if CLASS == "J":
            AVAILABLE_RESOURCES_SLOPE = random.randint(J_feature[0][0],J_feature[0][1])
            AVAILABLE_RESOURCES = MY_to_int(C)*AVAILABLE_RESOURCES_SLOPE*random.randint(J_feature[1][0],J_feature[1][1])
            PREDATORY_RATE_SLOPE = 11-AVAILABLE_RESOURCES_SLOPE
            PREDATORY_RATE = MY_to_int(C)*PREDATORY_RATE_SLOPE*random.randint(J_feature[2][0],J_feature[2][1])
        elif CLASS == "R":
            AVAILABLE_RESOURCES_SLOPE = random.randint(R_feature[0][0],R_feature[0][1])
            AVAILABLE_RESOURCES = MY_to_int(C)*AVAILABLE_RESOURCES_SLOPE*random.randint(R_feature[1][0],R_feature[1][1])
            PREDATORY_RATE_SLOPE = 11-AVAILABLE_RESOURCES_SLOPE
            PREDATORY_RATE = MY_to_int(C)*PREDATORY_RATE_SLOPE*random.randint(R_feature[2][0],R_feature[2][1])
        else:
            AVAILABLE_RESOURCES_SLOPE = random.randint(S_feature[0][0],S_feature[0][1])
            AVAILABLE_RESOURCES = MY_to_int(C)*AVAILABLE_RESOURCES_SLOPE*random.randint(R_feature[1][0],R_feature[1][1])
            PREDATORY_RATE_SLOPE = 11-AVAILABLE_RESOURCES_SLOPE
            PREDATORY_RATE = MY_to_int(C)*PREDATORY_RATE_SLOPE*random.randint(R_feature[2][0],R_feature[2][1])
        if len(X) == 3:
            if len(Y) == 3:
                SPACE[f"{CLASS+X+Y}"] = [C,AVAILABLE_RESOURCES,PREDATORY_RATE]
            elif len(Y) == 2:
                SPACE[f"{CLASS+X+'0'+Y}"] = [C,AVAILABLE_RESOURCES,PREDATORY_RATE]
            else:
                SPACE[f"{CLASS+X+'00'+Y}"] = [C,AVAILABLE_RESOURCES,PREDATORY_RATE]
        elif len(X) == 2:
            SPACE[f"{CLASS+'0'+X+Y}"] = [C,AVAILABLE_RESOURCES,PREDATORY_RATE]
        else:
            SPACE[f"{CLASS+'00'+X+Y}"] = [C,AVAILABLE_RESOURCES,PREDATORY_RATE]
        print(f"\r{i/EX_NUMBER}",end="")
    return SPACE
def name_to_information(name):
    return name[0],MY_to_int(name[1:4]),MY_to_int(name[4:])
def distance(name1,name2):
    return ((name_to_information(name1)[1]-name_to_information(name2)[1])**2+(name_to_information(name1)[2]-name_to_information(name2)[2])**2)**0.5
def draw_points(SPACE,colors,sizes,markers,alphas,i1,show_tf):
    global LEN
    S_X_list,S_Y_list = [],[]
    R_X_list,R_Y_list = [],[]
    J_X_list,J_Y_list = [],[]
    JI,RI,SI = 0,0,0
    ii0 = 0
    for i in SPACE.keys():
        if name_to_information(i)[0] == "S":
            S_X_list.append(name_to_information(i)[1])
            S_Y_list.append(name_to_information(i)[2])
            SI += 1
        elif name_to_information(i)[0] == "R":
            R_X_list.append(name_to_information(i)[1])
            R_Y_list.append(name_to_information(i)[2])
            RI += 1
        else:
            J_X_list.append(name_to_information(i)[1])
            J_Y_list.append(name_to_information(i)[2])
            JI += 1
        ii0 += 1
        print(f"\r{ii0/len(SPACE)}",end="")
    print(f"""
-------------------------------------------------------
J:{JI}                 R:{RI}                   S:{SI}
-------------------------------------------------------""")
    DFE = {}
    for i in SPACE.keys():
        DFE[SPACE[i][0]] = 0
    print(DFE.keys())
    LEN.append(len(DFE))
    if show_tf:
        plt.scatter(S_X_list,S_Y_list,c=colors[2],s=sizes[2],marker=markers[2],alpha=alphas[2])
        plt.scatter(R_X_list,R_Y_list,c=colors[1],s=sizes[1],marker=markers[1],alpha=alphas[1])
        plt.scatter(J_X_list,J_Y_list,c=colors[0],s=sizes[0],marker=markers[0],alpha=alphas[0])
        plt.show()
    print("\r----1",end="")
    plt.scatter(S_X_list,S_Y_list,c=colors[2],s=sizes[2],marker=markers[2],alpha=alphas[2])
    print("\r----2",end="")
    plt.scatter(R_X_list,R_Y_list,c=colors[1],s=sizes[1],marker=markers[1],alpha=alphas[1])
    print("\r----3",end="")
    plt.scatter(J_X_list,J_Y_list,c=colors[0],s=sizes[0],marker=markers[0],alpha=alphas[0])
    print("\r----4",end="")
    plt.savefig(f"{i1}a.jpg")
    print("\r----5",end="")
    J_LIST.append(JI)
    R_LIST.append(RI)
    S_LIST.append(SI)
    ALL_LIST.append(JI+RI+SI)
    print("\r----6",end="")
def LIST_TF(listinput):
    for i in listinput:
        if i:
            return 1
    return 0
def change(SPACE,J_CHANGE_FEATURE,R_CHANGE_FEATURE,S_CHANGE_FEATURE):
    i0 = 0
    for i in SPACE.keys():
        i0 += 1
        print(f"\r{i0/len(SPACE)}",end="")
        if i[0] == "J":
            SPACE[i] = [int_to_MY(MY_to_int(SPACE[i][0])+random.randint(J_CHANGE_FEATURE[0][0],J_CHANGE_FEATURE[0][1])),SPACE[i][1],SPACE[i][2]]
            C = SPACE[i][0]
            AVAILABLE_RESOURCES_SLOPE = random.randint(J_CHANGE_FEATURE[1][0],J_CHANGE_FEATURE[1][1])
            AVAILABLE_RESOURCES = MY_to_int(C)*AVAILABLE_RESOURCES_SLOPE*random.randint(J_CHANGE_FEATURE[2][0],J_CHANGE_FEATURE[2][1])/10
            PREDATORY_RATE_SLOPE = 11-AVAILABLE_RESOURCES_SLOPE
            PREDATORY_RATE = MY_to_int(C)*PREDATORY_RATE_SLOPE*random.randint(J_CHANGE_FEATURE[3][0],J_CHANGE_FEATURE[3][1])/10
            SPACE[i] = [SPACE[i][0],SPACE[i][1]+AVAILABLE_RESOURCES,SPACE[i][2]+PREDATORY_RATE]
        elif i[0] == "R":
            SPACE[i] = [int_to_MY(MY_to_int(SPACE[i][0])+random.randint(R_CHANGE_FEATURE[0][0],R_CHANGE_FEATURE[0][1])),SPACE[i][1],SPACE[i][2]]
            C = SPACE[i][0]
            AVAILABLE_RESOURCES_SLOPE = random.randint(R_CHANGE_FEATURE[1][0],R_CHANGE_FEATURE[1][1])
            AVAILABLE_RESOURCES = MY_to_int(C)*AVAILABLE_RESOURCES_SLOPE*random.randint(R_CHANGE_FEATURE[2][0],R_CHANGE_FEATURE[2][1])/10
            PREDATORY_RATE_SLOPE = 11-AVAILABLE_RESOURCES_SLOPE
            PREDATORY_RATE = MY_to_int(C)*PREDATORY_RATE_SLOPE*random.randint(R_CHANGE_FEATURE[3][0],R_CHANGE_FEATURE[3][1])/10
            SPACE[i] = [SPACE[i][0],SPACE[i][1]+AVAILABLE_RESOURCES,SPACE[i][2]+PREDATORY_RATE]
        else:
            SPACE[i] = [int_to_MY(MY_to_int(SPACE[i][0])+random.randint(S_CHANGE_FEATURE[0][0],S_CHANGE_FEATURE[0][1])),SPACE[i][1],SPACE[i][2]]
            C = SPACE[i][0]
            AVAILABLE_RESOURCES_SLOPE = random.randint(S_CHANGE_FEATURE[1][0],S_CHANGE_FEATURE[1][1])
            AVAILABLE_RESOURCES = MY_to_int(C)*AVAILABLE_RESOURCES_SLOPE*random.randint(S_CHANGE_FEATURE[2][0],S_CHANGE_FEATURE[2][1])/10
            PREDATORY_RATE_SLOPE = 11-AVAILABLE_RESOURCES_SLOPE
            PREDATORY_RATE = MY_to_int(C)*PREDATORY_RATE_SLOPE*random.randint(S_CHANGE_FEATURE[3][0],S_CHANGE_FEATURE[3][1])/10
            SPACE[i] = [SPACE[i][0],SPACE[i][1]+AVAILABLE_RESOURCES,SPACE[i][2]+PREDATORY_RATE]
    return SPACE
def change_cut(SPACE,CUT_RATE,GET_PRO):
    EX_NAME1 = random.choice(list(SPACE.keys()))
    EX_NAME2 = random.choice(list(SPACE.keys()))
    if distance(EX_NAME1,EX_NAME2) <= (MY_to_int(SPACE[EX_NAME1][0])+MY_to_int(SPACE[EX_NAME2][0]))*10*CUT_RATE:
        if EX_NAME1 != EX_NAME2:
            EX_DF1,EX_DF2 = MY_to_int(SPACE[EX_NAME1][0]),MY_to_int(SPACE[EX_NAME2][0])
            nm,nq = SPACE[EX_NAME1],SPACE[EX_NAME2]
            a,b = SPACE[EX_NAME2][2]*(EX_DF2/(EX_DF1+EX_DF2))*2,SPACE[EX_NAME1][2]*(EX_DF1/(EX_DF1+EX_DF2))*2
            SPACE[EX_NAME1] = [SPACE[EX_NAME1][0],SPACE[EX_NAME1][1]-a+b*random.randint(GET_PRO[0],GET_PRO[1])/10,SPACE[EX_NAME1][2]]
            SPACE[EX_NAME2] = [SPACE[EX_NAME2][0],SPACE[EX_NAME2][1]-b+a*random.randint(GET_PRO[0],GET_PRO[1])/10,SPACE[EX_NAME2][2]]
            print(f"""
-------------------------------------------
        {EX_NAME1}:{nm}
        {EX_NAME2}:{nq}
        {EX_NAME1} <====> {EX_NAME2}
        实际距离:{distance(EX_NAME1,EX_NAME2)}
        可发生距离:{(MY_to_int(SPACE[EX_NAME1][0])+MY_to_int(SPACE[EX_NAME2][0]))*10*CUT_RATE}
        {EX_NAME1}:{SPACE[EX_NAME1]}
        {EX_NAME2}:{SPACE[EX_NAME2]}
-------------------------------------------""")
            FIGHT_MESSAGE[f"{EX_NAME1}><{EX_NAME2}"] = f"""
-------------------------------------------
        {EX_NAME1}:{nm}
        {EX_NAME2}:{nq}
        {EX_NAME1} <====> {EX_NAME2}
        实际距离:{distance(EX_NAME1,EX_NAME2)}
        可发生距离:{(MY_to_int(SPACE[EX_NAME1][0])+MY_to_int(SPACE[EX_NAME2][0]))*10*CUT_RATE}
        {EX_NAME1}:{SPACE[EX_NAME1]}
        {EX_NAME2}:{SPACE[EX_NAME2]}
-------------------------------------------"""
            if (EX_NAME1 in BIGBOOK_FIGHT) and (EX_NAME2 in BIGBOOK_FIGHT):
                BIGBOOK_FIGHT[EX_NAME1] = BIGBOOK_FIGHT[EX_NAME1]+[EX_NAME2]
                BIGBOOK_FIGHT[EX_NAME2] = BIGBOOK_FIGHT[EX_NAME2]+[EX_NAME1]
            elif EX_NAME1 in BIGBOOK_FIGHT:
                BIGBOOK_FIGHT[EX_NAME1] = BIGBOOK_FIGHT[EX_NAME1]+[EX_NAME2]
                BIGBOOK_FIGHT[EX_NAME2] = [EX_NAME1]
            elif EX_NAME2 in BIGBOOK_FIGHT:
                BIGBOOK_FIGHT[EX_NAME1] = [EX_NAME2]
                BIGBOOK_FIGHT[EX_NAME2] = BIGBOOK_FIGHT[EX_NAME2]+[EX_NAME1]
            else:
                BIGBOOK_FIGHT[EX_NAME1] = [EX_NAME2]
                BIGBOOK_FIGHT[EX_NAME2] = [EX_NAME1]
        else:
            return SPACE,0
    else:
        return SPACE,0
    return SPACE,1
def cut(SPACE):
    print("-------------------------------------------")
    ii0 = 0
    SPACE_NEW = {}
    for i in SPACE.keys():
        if SPACE[i][1] > 0:
            SPACE_NEW[i] = SPACE[i]
        else:
            print(i,"灭亡",SPACE[i])
            DIEBOOK.append(i)
        ii0 += 1
        print(f"\r{ii0/len(SPACE)}",end="")
    SPACE = SPACE_NEW
    print(f"剩余 {len(SPACE)}")
    print("-------------------------------------------")
    return len(SPACE),SPACE
def del_png(count):
    import os
    for i in range(count):
        print(str(i)+"a.jpg")
        os.remove(str(i)+"a.jpg")
def save(EX_N_LIST,SPACE_D):
    with open("BIGBOOK_FIGHT.txt","w") as f1:
        f1.write(str(BIGBOOK_FIGHT))
    with open("DIEBOOK.txt","w") as f2:
        f2.write(str(DIEBOOK))
    with open("ALL_LIST.txt","w") as f3:
        f3.write(str([J_LIST,R_LIST,S_LIST,ALL_LIST]))
    with open("EX_N_LIST.txt","w") as f4:
        f4.write(str(EX_N_LIST))
    with open("SPACE_D.txt","w") as f5:
        f5.write(str(SPACE_D))
    with open("LEN.txt","w") as f6:
        f6.write(str(LEN))
    with open("FIGHT_MESSAGE.txt","w") as f7:
        f7.write(str(FIGHT_MESSAGE))
    import os
    from PIL import Image
    images = []
    all_list_u = []
    for i in os.listdir():
        if i[-5:] == "a.jpg":
            all_list_u.append(i)
    for i in range(len(all_list_u)):
        im = Image.open(str(i)+"a.jpg")
        images.append(im)
    images[0].save("end.gif",save_all=True,loop=True,append_images=images[1:],duration=100)
    del_png(len(all_list_u))
def main():
    with open("space_system.txt","r") as f:
        system_file = eval(f.read())
    print(f"show_data:{system_file}\n\n")
    EX_NUMBER,EX_N_MAX = system_file[0],system_file[1]
    show=system_file[2]
    wait=system_file[3]
    save_=system_file[4]
    colors=list(system_file[5])
    sizes=list(system_file[6])
    markers=list(system_file[7])
    alphas=list(system_file[8])
    SPACE = create_ex(int(EX_NUMBER),system_file[9],system_file[10],system_file[11],system_file[12])
    with open("space_ex.txt","w") as f:
        f.write(str(SPACE))
    print("\n")
    with open("space_ex.txt","r") as f:
        SPACE = eval(f.read())
    SPACE_D = SPACE
    import time
    EX_N = EX_N_MAX
    EX_N_LIST = []
    i0 = 0
    i1 = 0
    while EX_N>system_file[20]:
        NPS_LS = []
        for i in range(system_file[18]):
            SPACE,NP = change_cut(SPACE,system_file[16],system_file[17])
            NPS_LS.append(NP)
            print(f"\r{i/system_file[18]}",end="")
        if LIST_TF(NPS_LS):
            print("=======================================================================================")
            print(f"第{i0}次诱发")
            EX_N,SPACE = cut(SPACE)
            draw_points(SPACE,colors,sizes,markers,alphas,i1,show)
            i1 += 1
            print("=======================================================================================")
            if wait:time.sleep(wait)
        SPACE = change(SPACE,system_file[13],system_file[14],system_file[15])
        SPACE.update(create_ex(int(system_file[19]),system_file[9],system_file[10],system_file[11],system_file[12]))
        DFE = {}
        for i in SPACE.keys():
            DFE[SPACE[i][0]] = 0
        EX_N_LIST.append(len(DFE.keys()))
        print(find_max_min(list(DFE.keys())))
        i0 += 1
    if save_:save(EX_N_LIST,SPACE_D)
main()