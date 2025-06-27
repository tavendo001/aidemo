'''
调用方法
#左边对齐
string1 = "字符串123"
result = duiqi(string1,10,"left")#对齐字符串，长度，对齐方式
print(result)
#右边对齐
string1 = "字符串123"
result = duiqi(string1,10,"right")#对齐字符串，长度，对齐方式
print(result)
#居中对齐这个有点麻烦，例如 “123” ，对齐长度 6 ，要补三个空格，前面一个后面两个还是前面两个后面一个，这个是可以设置的
对齐的方式有 center0 center1 center2
center1：前面的空格更少，后面的更多
center2：后面的空格更少，前面的更多
center0：两边空格一样多（需要字符合理——例： 字符串“123”， 长度为 “5”，不然要报错）
'''


def duiqi(string, length, way):
    if(way == "left"):
        difference = length - len(string)
        if difference == 0:  # 若差值为0则不需要补
            return string
        elif difference < 0:
            print('错误：限定的对齐长度小于字符串长度!')
            return None
        new_string = ''
        space = '　'
        for i in string:
            codes = ord(i)  # 将字符转为ASCII或UNICODE编码
            if codes <= 126:  # 若是半角字符
                new_string = new_string + chr(codes+65248)  # 则转为全角
            else:
                new_string = new_string + i  # 若是全角，则不转换
        return new_string + space*(difference)  # 返回补齐空格后的字符串
    elif(way == "right"):
        difference = length - len(string)
        if difference == 0:  # 若差值为0则不需要补
            return string
        elif difference < 0:
            print('错误：限定的对齐长度小于字符串长度!')
            return None
        new_string = ''
        space = '　'
        for i in string:
            codes = ord(i)  # 将字符转为ASCII或UNICODE编码
            if codes <= 126:  # 若是半角字符
                new_string = new_string + chr(codes+65248)  # 则转为全角
            else:
                new_string = new_string + i  # 若是全角，则不转换
        return space*(difference) + new_string   # 返回补齐空格后的字符串
    elif(way == "center0"):
        difference = length - len(string)
        if difference == 0:  # 若差值为0则不需要补
            return string
        elif difference < 0:
            print('错误：限定的对齐长度小于字符串长度!')
            return None
        new_string = ''
        space = '　'
        for i in string:
            codes = ord(i)  # 将字符转为ASCII或UNICODE编码
            if codes <= 126:  # 若是半角字符
                new_string = new_string + chr(codes+65248)  # 则转为全角
            else:
                new_string = new_string + i  # 若是全角，则不转换
        # 返回补齐空格后的字符串
        return space*(int(difference/2)) + new_string + space*(int(difference/2))
    elif(way == "center2"):
        difference = length - len(string)
        if difference == 0:  # 若差值为0则不需要补
            return string
        elif difference < 0:
            print('错误：限定的对齐长度小于字符串长度!')
            return None
        new_string = ''
        space = '　'
        for i in string:
            codes = ord(i)  # 将字符转为ASCII或UNICODE编码
            if codes <= 126:  # 若是半角字符
                new_string = new_string + chr(codes+65248)  # 则转为全角
            else:
                new_string = new_string + i  # 若是全角，则不转换
        return space*(int(difference/2+1)) + new_string + space*(int(difference/2))
    elif(way == "center1"):
        difference = length - len(string)
        if difference == 0:  # 若差值为0则不需要补
            return string
        elif difference < 0:
            print('错误：限定的对齐长度小于字符串长度!')
            return None
        new_string = ''
        space = '　'
        for i in string:
            codes = ord(i)  # 将字符转为ASCII或UNICODE编码
            if codes <= 126:  # 若是半角字符
                new_string = new_string + chr(codes+65248)  # 则转为全角
            else:
                new_string = new_string + i  # 若是全角，则不转换
        # 返回补齐空格后的字符串
        return space*(int(difference/2)) + new_string + space*(int(difference/2 + 1))
    elif(way == "center2"):
        difference = length - len(string)
        if difference == 0:  # 若差值为0则不需要补
            return string
        elif difference < 0:
            print('错误：限定的对齐长度小于字符串长度!')
            return None
        new_string = ''
        space = '　'
        for i in string:
            codes = ord(i)  # 将字符转为ASCII或UNICODE编码
            if codes <= 126:  # 若是半角字符
                new_string = new_string + chr(codes+65248)  # 则转为全角
            else:
                new_string = new_string + i  # 若是全角，则不转换
        # 返回补齐空格后的字符串
        return space*(int(difference/2+1)) + new_string + space*(int(difference/2))

'''
def tkprepare():
    win = tk.Tk()    
    win.geometry(str(100*CL.L)+"x"+str(100*CL.H+100))
    win.title("座位表")    
    # 设置窗口的位置
    win.geometry('+100+100')
    jiangtai = tk.Label(win, text='讲台', bg='red', font=('Arial', 25), width=10, height=1)
    jiangtai.place(x=CL.L*35, y=20)
    save_btn = tk.Button(win, text='保存座次表', bg='red', font=('Arial', 10), width=10, height=1,command=lambda : CL.save())
    save_btn.place(x=0, y=0)
    re_btn = tk.Button(win, text='重新随机生成', bg='red', font=('Arial', 10), width=10, height=1,command=lambda : CL.randommap())
    re_btn.place(x=0, y=40)

    num = len(CL.sl)
    print(CL.sl)
    for i in range(0, CL.H):  # 生成鼠标按钮
        for j in range(0, CL.L):
            if num != 1: 
                print(num-1)
                k = random.randint(0, num-1)
                bt = tk.Button(win, text=CL.cl[k], bg="green", font=(
                    'Arial', 16), width=6, height=2, command=lambda xx=i, yy=j, text=CL.cl[k]: click(xx, yy, text))
                bt.place(x=100*j, y=100*i+100)
                self.listButton[i][j] = bt
                self.result[i][j] = CL.cl[k]
                num = num-1
                CL.cl.pop(k)
            else:
                bt = tk.Button(win, text="", bg="green", font=(
                    'Arial', 16), width=6, height=2, command=lambda xx=i, yy=j, text="": click(xx, yy, text))
                bt.place(x=100*j, y=100*i+100)
                self.listButton[i][j] = bt
                self.result[i][j] = ""
    win.attributes("-topmost", True)  # 全屏顶层

    win.mainloop()
'''