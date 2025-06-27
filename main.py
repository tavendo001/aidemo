import tkinter as tk
import threading
import random
import duiqi as d
from tkinter import PhotoImage
import tkinter.messagebox as tkm
import GetInfo

def get_dict(name):
    file_name = name
    list_stu = []
    file = open(file_name, 'r', encoding='utf-8')  # 打开文件
    list_stu = file.readlines()  # 读取所有行
    list_stu = [line.strip() for line in list_stu]  # 去掉换行符
    di_li_stu = []
    for i in list_stu:
        di_li_stu.append(i.split("  "))
    dic_stu = {}
    for i in range(len(di_li_stu)):
        dic_stu[di_li_stu[i][0]] = [di_li_stu[i][1], int(di_li_stu[i][2])]
    return dic_stu


def get_list(dic):
    k = []
    for i in dic.keys():
        k.append(i)
    return k


class ChairList():
    def __init__(self, cl, W, H, sl, make, first_x, first_y, listButton, result, sd,aoi1):  # 初始化
        self.cl = cl
        self.W = W
        self.H = H
        self.sl = sl
        self.make = make
        self.first_x = first_x
        self.first_y = first_y
        self.listButton = listButton
        self.result = result
        self.sd = sd
        self.aoi1 = aoi1
        self.man = 0
        self.woman = 0
        self.nobody = 0
        self.choice = 0
        self.cbl = False
        self.cbr = False
        self.cbu = False
        self.cbd = False

    def makelist(self, li, L, H):
        k = li.copy()
        l = []
        ll = []
        for i in range(len(k)):
            for j in range(len(k[i])):
                l.append(k[i][j])
        for i in range(L*H-len(l)):
            l.append("")
        for i in range(H):
            lll = []
            for j in range(L):
                lll.append(l.pop(0))
            ll.append(lll)
        self.result = ll

    def update(self):
        if self.aoi1.get() == True:
            self.line()
        for i in range(len(self.result)):
            for j in range(len(self.result[i])):
                self.listButton[i][j]["text"] = self.result[i][j]
                if self.result[i][j] != "":
                    k = self.sd[self.result[i][j]][1]
                    sex = self.sd[self.result[i][j]][0]
                    if k == 1:
                        self.listButton[i][j]["bg"] = "pink"
                    elif k == 2:
                        self.listButton[i][j]["bg"] = "yellow"
                    elif k == 3:
                        self.listButton[i][j]["bg"] = "#C3DEEF"
                    elif k == 4:
                        self.listButton[i][j]["bg"] = "grey"
                    if sex == "男":
                        self.listButton[i][j]["image"] = self.man
                        self.listButton[i][j]["compound"] = "center"
                    elif sex == "女":
                        self.listButton[i][j]["image"] = self.woman
                        self.listButton[i][j]["compound"] = "center"
                    
                else:
                    self.listButton[i][j]["bg"] = "green"
                    self.listButton[i][j]["image"] = self.nobody

    def line(self):
        for i in range(len(self.result[0])):
            l = []
            for j in range(len(self.result)):
                if self.result[j][i]!="":
                    l.append(self.result[j][i])
                    self.result[j][i] = ""
            for j in range(len(l)):
                self.result[j][i] = l[j]
    
    def updatemess(self):
        tkm.showinfo("智能排座位 更新记录", "智能排座位V1.0,功能：向前后左右，交换两个座位的位置，随机排列，按选科生成\n智能排座位V2.0,更新：人名表(√)，新增功能：按男女生成(√)，自动补位(√)\n智能排座位V3.0,更名为智能排座位V3.0,更新：优化输入界面(√)，新增操作指南(√)、更新日志(√)\n智能排座位V4：更新功能：尝试向按钮插入图片(√)，选择保存进入excel(√)")

    def tkprepare(self):
        win = tk.Tk()
        win.geometry(str(100*self.W)+"x"+str(110*self.H+100))
        win.title("智能排座位V4.0  主界面")
        #仅在创建窗口后可定义的变量
        self.man = tk.PhotoImage(file="man.png")
        self.woman = tk.PhotoImage(file="woman.png")
        self.nobody = tk.PhotoImage(file="nobody.png")
        self.cbl = tk.BooleanVar()
        self.cbr = tk.BooleanVar()
        self.cbu = tk.BooleanVar()
        self.cbd = tk.BooleanVar()
        # 设置窗口的位置及讲台
        win.geometry('+100+100')
        jiangtai = tk.Label(win, text='讲台', bg='red',font=('Arial', 25), width=10, height=1)
        jiangtai.place(x=self.W*35, y=75)
        #按不同方式大调
        tk.Label(win,text = "大调区",fg = "red",font = 14).place(x=5,y=2)
        re_btn = tk.Button(win, text='重新随机生成', bg='red', font=('Arial', 10), width=10, height=1, command=lambda: self.randommap())
        re_btn.place(x=5, y=40)
        re_btn = tk.Button(win, text='按选科生成', bg='red', font=('Arial', 10), width=10, height=1, command=lambda: self.Submap())
        re_btn.place(x=5, y=75)
        re_btn = tk.Button(win, text='按性别生成', bg='red', font=('Arial', 10), width=10, height=1, command=lambda: self.Sexmap())
        re_btn.place(x=5, y=110)
        #杂项
        tk.Label(win,text="注：单击两个座位可以使其互换位置",fg = "blue",font = 2).place(x=self.W*35-25,y = 125)
        save_btn = tk.Button(win, text='保存到', bg='red', font=('Arial', 10), width=10, height=1, command=lambda: self.save())
        save_btn.place(x=self.W*35, y=0)
        self.choice = tk.IntVar(value = 0)
        ChoseTxt = tk.Radiobutton(win,text = "txt",variable = self.choice,value = 0)
        ChoseTxt.place(x = self.W*48,y = 3)
        ChoseExcel = tk.Radiobutton(win,text = "Excel",variable = self.choice,value = 1)
        ChoseExcel.place(x = self.W*55,y = 3)
        #re_btn = tk.Button(win, text='使用指南', bg='red', font=('Arial', 10), width=8, height=1, command=lambda: self.helpmess())
        re_btn.place(x=self.W*47, y=33)
        re_btn = tk.Button(win, text='更新记录', bg='red', font=('Arial', 10), width=8, height=1, command=lambda: self.updatemess())
        re_btn.place(x=self.W*58, y=33)
        #整体移动
        tk.Label(win,text = "整体移动区",font = 14,fg = "red").place(x=100*self.W-130, y=5)
        CBL = tk.Checkbutton(win,text = "向左",variable = self.cbl,onvalue = True,offvalue = False)
        CBL.place(x=100*self.W-120, y=30)
        CBR = tk.Checkbutton(win,text = "向右",variable = self.cbr,onvalue = True,offvalue = False)
        CBR.place(x=100*self.W-120, y=50)
        CBU = tk.Checkbutton(win,text = "向前",variable = self.cbu,onvalue = True,offvalue = False)
        CBU.place(x=100*self.W-60, y=30)
        CBD = tk.Checkbutton(win,text = "向后",variable = self.cbd,onvalue = True,offvalue = False)
        CBD.place(x=100*self.W-60, y=50)
        tk.Button(win, text="移动", width=14, height=1,command=lambda: self.allmove()).place(x=100*self.W-120, y=70)
        #自动补位
        self.aoi1 = tk.BooleanVar()
        CbAoi = tk.Checkbutton(win, text="自动补位", variable=self.aoi1,onvalue=True, offvalue=False)  # aline on itsef
        CbAoi.place(x = self.W*35,y = 33)

        #print(self.sl)
        ssl = self.sl.copy()
        num = len(ssl)
        for i in range(0, self.H):  # 生成鼠标按钮
            for j in range(0, self.W):
                if num >= 1:
                    num = len(ssl)
                    k = random.randint(0, num-1)
                    bt = tk.Button(win, text=ssl[k], bg="green", font=('Arial', 16), width=73, height=57, command=lambda xx=i, yy=j, text=ssl[k]: self.click(xx, yy, text))
                    bt.place(x=100*j, y=100*i+150)
                    self.listButton[i][j] = bt
                    self.result[i][j] = ssl[k]
                    num = num-1
                    ssl.pop(k)
                else:
                    bt = tk.Button(win, text="", bg="green", font=('Arial', 16), width=73, height=57, command=lambda xx=i, yy=j, text="": self.click(xx, yy, text))
                    bt.place(x=100*j, y=100*i+150)
                    self.listButton[i][j] = bt
                    self.result[i][j] = ""
        win.attributes("-topmost", True)  # 全屏顶层
        self.update()
        win.mainloop()

    def randommap(self):  # 随机生成
        ssl = self.sl.copy()  # 一定要用.copy(),因为python中类是默认浅拷贝，一块更改
        num = len(ssl)
        self.cl = []
        if num > self.W*self.H:
            return
        else:
            for i in range(self.H):
                l = []
                for j in range(self.W):
                    l.append("")
                self.cl.append(l)
            i = 0
            X = 0
            Y = 0
            while i < num:
                #print(X,Y,self.W,self.H,len(list_stu),num)
                self.cl[Y][X] = ssl.pop(random.randint(0, len(ssl)-1))
                X += 1
                if X > self.W-1:
                    Y += 1
                    X = 0
                i += 1
            self.result = self.cl
            self.update()
            #print(self.cl)

    def Submap(self):
        li = [[], [], [], []]  # 一定不能用li = []*4,不然一个改变其他的都改变！！！！！！
        for i in range(len(self.result)):
            for j in range(len(self.result[i])):
                if self.result[i][j] != "":
                    if self.sd[self.result[i][j]][1] == 1:
                        li[0].append(self.result[i][j])
                    elif self.sd[self.result[i][j]][1] == 2:
                        li[1].append(self.result[i][j])
                    elif self.sd[self.result[i][j]][1] == 3:
                        li[2].append(self.result[i][j])
                    elif self.sd[self.result[i][j]][1] == 4:
                        li[3].append(self.result[i][j])
        random.shuffle(li)
        for i in range(len(li)):
            random.shuffle(li[i])
        self.makelist(li, self.W, self.H)
        self.update()

    def Sexmap(self):                            
        li = [[], []]
        for i in range(len(self.result)):
            for j in range(len(self.result[i])):
                if self.result[i][j] != "":
                    if self.sd[self.result[i][j]][0] == "男":
                        li[0].append(self.result[i][j])
                    elif self.sd[self.result[i][j]][0] == "女":
                        li[1].append(self.result[i][j])
        random.shuffle(li)
        l = []
        ll = []
        for i in range(self.H):
            k = []
            for j in range(self.W):
                k.append("")
            ll.append(k)
        i = 0
        while li[0] != [] or li[1] != []:
            if li[0] == []:
                for i in range(len(li[1])):
                    l.append(li[1].pop(0))
            elif li[1] == []:
                for i in range(len(li[0])):
                    l.append(li[0].pop(0))
            else:
                if i == 0:
                    l.append(li[0].pop(0))
                    i = 1
                elif i == 1:
                    l.append(li[1].pop(0))
                    i = 0
        for i in range(len(ll)):
            for j in range(len(ll[i])):
                if l != []:
                    ll[i][j] = l.pop(0)
        for i in range(len(ll)):
            k = random.randint(0,1)
            if k % 2==0:
                if len(ll[i])%2 == 0:
                    ll[i].reverse()
                k+=1
            else:
                k+=1
        self.result = ll
        self.update()

    def click(self, bx, by, btext):  # 交换俩个座位
        if self.first_x == -1:
            #hid[bx][by] = not hid[bx][by]
            self.listButton[bx][by]["bg"] = "red"
            self.first_x = bx
            self.first_y = by
        else:
            self.listButton[bx][by]['text'] = self.result[self.first_x][self.first_y]
            self.listButton[self.first_x][self.first_y]['text'] = self.result[bx][by]
            self.listButton[self.first_x][self.first_y]["bg"] = "green"
            tmp_name = self.result[bx][by]
            self.result[bx][by] = self.result[self.first_x][self.first_y]
            self.result[self.first_x][self.first_y] = tmp_name
            self.update()
            self.first_x = -1
            self.first_y = -1
    
    def allmove(self):
        if self.cbl.get() == True:
            self.left()
        if self.cbr.get() == True:
            self.right()
        if self.cbu.get() == True:
            self.up()
        if self.cbd.get() == True:
            self.down()

    def left(self):
        for i in range(len(self.result)):
            self.result[i].append(self.result[i].pop(0))
        self.update()

    def right(self):
        for i in range(len(self.result)):
            self.result[i].insert(0, self.result[i].pop(-1))
        self.update()

    def up(self):
        self.result.append(self.result.pop(0))
        self.update()

    def down(self):
        self.result.insert(0, self.result.pop(-1))
        self.update()
        
    def txtmessage(self):
        tkm.showinfo("智能排座位  保存","成功保存到Txt!")

    def excelmessage(self):
        tkm.showinfo("智能排座位  保存","成功保存到Excel!")
        
    def save(self):  # 保存
        list_column = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        
        #保存到TXT
        if self.choice.get() == 0:
            output = open('新座位表.txt', 'w+')

            output.write("新座次表：")
            output.write("\n")
            output.write(d.duiqi("", 2, "left"))
            for j in range(self.W):
                output.write(d.duiqi(list_column[j], 4, "left"))
            output.write("\n")
            for i in range(len(self.result)):
                output.write(d.duiqi(str(i+1), 2, "left"))
                for j in range(len(self.result[i])):
                    output.write(d.duiqi(self.result[i][j], 4, "left"))
                    output.write(' ')
                output.write('\n')
            output.close()
            self.txtmessage()
            
        elif self.choice.get() == 1:
            output = open('新座位表.xls','w+')
    
            output.write("新座次表：")    
            output.write("\n")   
            output.write('\t')
            for j in range(self.W):
                output.write(list_column[j])
                output.write('\t')
            output.write("\n")
            for i in range(len(self.result)):
                output.write(str(i+1))
                output.write('\t')
                for j in range(len(self.result[i])):
                    output.write(self.result[i][j])
                    output.write('\t')
                output.write('\n')
            output.close()
            self.excelmessage()

if __name__ == "__main__":
    cl = []
    sd = get_dict("stu_name.txt")
    sl = get_list(sd)
    GIM = GetInfo.GetInfoMation(len(sl))
    GIM.getinfo()
    W = GIM.stunumli[0]
    H = GIM.stunumli[1]
    CL = ChairList(cl, W, H, sl, False, -1, -1, [[tk.Button for i in range(W)] for j in range(H)], [["" for i in range(W)] for j in range(H)], sd,False)
    thread1 = threading.Thread(target=CL.tkprepare())
    thread1.start()
