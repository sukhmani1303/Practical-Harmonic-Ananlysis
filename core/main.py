import tkinter as gui
import math

root = gui.Tk()
root.title("PRACTICAL HARMONIC ANALYSIS")
root.resizable(0,0)
icon_pic = gui.PhotoImage(file = r"D:\project UV\uv python\python gui\fourier-solver\res\function.png")
root.iconphoto(False, icon_pic)

input_box = gui.Entry(width = 40, borderwidth= 7 )
input_box.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = (15,0), ipady=10, ipadx = 10)
input_box.insert(0,"0")
input_box.bind("<Key>", lambda e: "break")

second_box = gui.Entry(width = 40, borderwidth= 2 )
second_box.grid(row = 1, column = 0, columnspan=5, padx = 10,pady = (5,0), ipady=3, ipadx = 10)
second_box.bind("<Key>", lambda e: "break")

global ntus,x,y,an_all, bn_all,deciclick,deci
ntus = 0
x = []
y = []
an_all = []
bn_all = []
deciclick = 0
deci = False

def htu():
    htu_window = gui.Toplevel(root)
    htu_window.title("HOW TO USE FOURIER SOLVER Beta")
    htu_window.geometry("500x500")
    htu_window.minsize(300,300)
    gui.Label(htu_window, text = "sample lines").pack()

htu_but = gui.Button(text = "?", bg = "cyan",command = htu).grid(row = 0, column = 4, pady=5, padx = 5 ,ipady = 10, ipadx = 10)

def num_frm_but(num):
    global deci, deciclick
    cur_num = str(input_box.get())
    if deci==False:
        if cur_num[0]==0:
            cur_name = cur_name[0:]
            input_box.delete(0,gui.END)
            input_box.insert(0,str(cur_num)+str(num))
            
        else:
            input_box.delete(0,gui.END)
            input_box.insert(0,str(cur_num)+str(num))
    else:
        if deciclick ==1:
            input_box.delete(0,gui.END)
            input_box.insert(0,str(str(cur_num)+"."+str(num)))
            deciclick+=1
        else:

            input_box.delete(0,gui.END)
            input_box.insert(0,str(str(cur_num)+str(num)))

        # if deciclick == 1:
        #     cur_num = int(input_box.get())
        #     pre_num = len(str(cur_num))
        #     deci_num = float((num)/10**(pre_num))
        #     input_box.insert(0,cur_num+deci_num)
        #     deciclick+=1

        # else:
        #     cur_num = float(input_box.get())
        #     input_box.delete(0,gui.END)
        #     pre_num = len(str(cur_num))
        #     deci_num = float((num)/10**(pre_num-1))
        #     input_box.insert(0,cur_num+deci_num)
        


def clear_input():
    global ntus,x,y,an_all, bn_all
    input_box.delete(0,gui.END)
    second_box.delete(0,gui.END)
    input_box.insert(0,"0")
    second_box.insert(0,"CLEARED !")
    ntus = 0
    x = []
    y = []

def back_input():
    second_box.delete(0,gui.END)
    second_box.insert(0,"prev val : "+ input_box.get())
    inst_num = str(input_box.get())
    new_inst_num = inst_num[:-1]
    input_box.delete(0,gui.END)
    
    if len(new_inst_num)==0:
        input_box.insert(0,"0")
    else:
        input_box.insert(0,new_inst_num)


def x_intake():
    global ntus 
    ntus = 1
    second_box.delete(0,gui.END)
    second_box.insert(0,"ENTER X VALUES")
    input_box.delete(0,gui.END)
    input_box.insert(0,"0")

def y_intake():
    global ntus
    second_box.delete(0,gui.END)
    second_box.insert(0,"ENTER Y VALUES")
    ntus = 2
    input_box.delete(0,gui.END)
    input_box.insert(0,"0")

def har_intake():
    global ntus 
    ntus = 3
    second_box.delete(0,gui.END)
    second_box.insert(0,"ENTER NUMBER OF HARMONICS")
    input_box.delete(0,gui.END)
    input_box.insert(0,"0")

def equalto():
    global ntus,x,y,an_all, bn_all,a0
    input_box.insert(0,"0")
    if ntus== 0:
        input_box.delete(0,gui.END)
        input_box.insert(0,"0")
    elif ntus==1:
        x_val = float(input_box.get())
        input_box.delete(0,gui.END)
        input_box.insert(0,"0")
        x.append(x_val)

    elif ntus==2:
        y_val = float(input_box.get())
        input_box.delete(0,gui.END)
        input_box.insert(0,"0")
        y.append(y_val)

    elif ntus==3:
        har = int(input_box.get())
        input_box.delete(0,gui.END)
        input_box.insert(0,"0")
        if len(y) == len(x) and len(y)!=0:
            n = int(len(y))
            a0 = 2 * (sum(y) / n)
            if har > 0:

                for i in range(har):
                    an = []
                    bn = []

                    for j in range(n):
                        temp_a = x[j] * (i + 1)
                        a_val = (y[j] * math.cos(math.radians(temp_a)))
                        # print("cos : ", math.cos(math.radians(temp_a)))
                        an.append(a_val)

                    for k in range(n):
                        temp_b = x[k] * (i + 1)
                        b_val = (y[k] * math.sin(math.radians(temp_b)))
                        # print("sin : ", math.sin(math.radians(temp_b)))
                        bn.append(b_val)

                    # print("\nsum y*cos : ", sum(an))

                    a = (2 / n) * sum(an)
                    # print("\na", i+1, "is : ", round(a, 3))

                    # print("\nsum y*sin : ", sum(bn))
                    b = (2 / n) * sum(bn)
                    # print("\nb", i+1, "is : ", round(b, 3))
                    an_all.append(a)
                    bn_all.append(b)
            else:
                second_box.delete(0,gui.END)
                second_box.insert(0,"HAR SHOULD BE > 0")
                pass
        else:
            second_box.delete(0,gui.END)
            second_box.insert(0,"NO. OF X MUST = NO. OF Y")
            pass

def a0_val():
    global a0
    second_box.delete(0,gui.END)
    input_box.delete(0,gui.END)
    input_box.insert(0,a0)
    second_box.insert(0,"value of a0")

global aclick_cnt
aclick_cnt = -1

global bclick_cnt
bclick_cnt = -1

def an_val():
    global an_all,aclick_cnt
    if aclick_cnt==len(an_all)-1:
        aclick_cnt=-1
    aclick_cnt+=1
    input_box.delete(0,gui.END)
    second_box.delete(0,gui.END)
    input_box.insert(0,round(an_all[aclick_cnt],3))
    second_box.insert(0,str(aclick_cnt +1)+" an harmonic")

def bn_val():
    global bn_all,bclick_cnt
    if bclick_cnt==len(bn_all)-1:
        bclick_cnt=-1
    bclick_cnt+=1
    input_box.delete(0,gui.END)
    second_box.delete(0,gui.END)
    input_box.insert(0,round(bn_all[bclick_cnt],3))
    second_box.insert(0,str(bclick_cnt +1)+" bn harmonic")

def decimal_in():
    global deciclick,deci
    second_box.delete(0,gui.END)
    second_box.insert(0,"decima on")
    deciclick =1
    deci = True

but0 = gui.Button(text = "0", command =lambda : num_frm_but(0)).grid(row = 2, column = 0, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
but1 = gui.Button(text = "1", command =lambda : num_frm_but(1)).grid(row = 2, column = 1, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
but2 = gui.Button(text = "2", command =lambda : num_frm_but(2)).grid(row = 2, column = 2, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
but3 = gui.Button(text = "3", command =lambda : num_frm_but(3)).grid(row = 2, column = 3, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
but4 = gui.Button(text = "4", command =lambda : num_frm_but(4)).grid(row = 2, column = 4, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
but5 = gui.Button(text = "5", command =lambda : num_frm_but(5)).grid(row = 3, column = 0, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
but6 = gui.Button(text = "6", command =lambda : num_frm_but(6)).grid(row = 3, column = 1, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
but7 = gui.Button(text = "7", command =lambda : num_frm_but(7)).grid(row = 3, column = 2, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
but8 = gui.Button(text = "8", command =lambda : num_frm_but(8)).grid(row = 3, column = 3, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
but9 = gui.Button(text = "9", command =lambda : num_frm_but(9)).grid(row = 3, column = 4, pady=5, padx = 5 ,ipady = 10, ipadx = 10)

ans_but = gui.Button(fg="white",bg="green",text = "ENTER", command =equalto).grid(row = 6, column = 1, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
a0_but = gui.Button(text = "a0", fg="yellow",bg="blue", command =a0_val).grid(row = 5, column = 2, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
an_but = gui.Button(text = "an", fg="yellow",bg="blue",command =an_val).grid(row = 5, column = 3, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
bn_but = gui.Button(text = "bn", fg="yellow",bg="blue",command =bn_val).grid(row = 5, column = 4, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
xval_but = gui.Button(text = "X", fg="white",bg="orange",command =x_intake).grid(row = 5, column = 0, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
yval_but = gui.Button(text = "Y", fg="white",bg="orange",command =y_intake).grid(row = 5, column = 1, pady=5, padx = 5 ,ipady = 10, ipadx = 10)

deci_but = gui.Button(text = ".", command =decimal_in).grid(row = 6, column = 2, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
har_but = gui.Button(text = "HAR", fg="yellow",bg="purple",command =har_intake).grid(row = 6, column = 0, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
clear_but = gui.Button(text = "CLEAR",fg="white",bg="red", command = clear_input).grid(row = 6, column = 3, pady=5, padx = 5 ,ipady = 10, ipadx = 10)
back_but = gui.Button(text = "BACK",fg="black",bg="grey", command = back_input).grid(row = 6, column = 4, pady=5, padx = 5 ,ipady = 10, ipadx = 10)

git_pic = gui.PhotoImage(file = r"D:\project UV\uv python\python gui\fourier-solver\res\footer.png")
gui.Label(root,image = git_pic, bg="black").grid(row=7,column = 0,columnspan = 6, pady=(10,0))

root.mainloop()

# credits - YUVRAJ SINGH SUKHMANI 
