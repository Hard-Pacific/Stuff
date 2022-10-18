import subprocess,re,os,datetime
from openpyxl import Workbook
from tkinter import messagebox
from tkinter import *
#Проверка наличия данных
y=0.15
date = datetime.date.today()
#Даты
Calendar = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
try:
    with open("Данные.txt") as P:
        st=P.read()
except:
    with open("Данные.txt","w+") as P:
        st=P.read()
try:
    with open("{x}{y}.txt".format(x=Calendar[date.month-1],y=str(date.year))) as D:
        data=D.read()
except:
    with open("{x}{y}.txt".format(x=Calendar[date.month-1],y=date.year),"w+") as D:
        data=D.read()
try:
    with open("Универсал.txt") as D:
        Uni=D.read()
    if Uni=="":
        Ticket2=0
    else:
        Ticket2=1
except:
    with open("Универсал.txt","w+") as D:
        None
    Ticket2=0
C2 = 0
Ticket = False
DeskCheck = False
subprocess.check_call(["attrib","+H","Данные.txt"])
subprocess.check_call(["attrib","+H","Универсал.txt"])
try:
    cycle=cycle
    Name=Name
    Stat=Stat
    n1=n1
    n2=n2
    Digit=Digit
    cycle2=cycle2
except:
    Digit=[]
    Name=[]
    Stat=[]
    n1 = []
    n2 = []
    cycle=0
    cycle2=[]
#Стандарт\Универсал
def desk():
    global Ticket2
    if Ticket2==1:
        global Desk2
        Choose["text"]="Универсал"
        with open("Универсал.txt") as D:
            doc=D.read()
        lnames=re.findall(r"[a-zA-ZА-Яа-я]+",doc)
        global cycle2
        cycle2=len(lnames)
        print(cycle2)
        Desk2 = Frame(win,bg="#BBB")
        Desk2.place(relx=.1955,rely=0.2,relwidth=.55,relheight=.657)
        LAB2=[]
        for _ in range(cycle2):
            global Digit
            print("PPPP",str(n1))
            if _>4:
                LAB2.append(0)
                LAB2[_]= Label(Desk2,text=lnames[_],background="#BBB", height=1,font="Arial 10 bold")
                LAB2[_].place(relx=.55,rely=.035+(_-5)*0.21,relwidth=.3)
                Digit.append(0)
                Digit[_]= Text(Desk2,background="#CCC",width=5, height=1,font="Arial 10")
                Digit[_].insert(1.0,"0")
                Digit[_].place(relx=.83,rely=.043+(_-5)*0.21)
            else:
                Digit.append(0)
                Digit[_]= Text(Desk2,background="#CCC",width=5, height=1,font="Arial 10")
                Digit[_].insert(1.0,"0")
                Digit[_].place(relx=.35,rely=.043+_*0.21)
                LAB2.append(0)
                LAB2[_]= Label(Desk2,text=lnames[_],background="#BBB", height=1,font="Arial 10 bold")
                LAB2[_].place(relx=.05,rely=.035+_*0.21,relwidth=.3)
            
        Ticket2=2
        return None
    if Ticket2==2:
        Desk2.destroy()
        Choose["text"]="Стандарт"
        Ticket2=1
        return None
        
    def CreateDesk():
        global Ticket2
        Ticket2=2
        global Ticket
        global cycle
        global Desk
        if Ticket==True:
            Desk.destroy()
            Choose["text"]="Стандарт"
            Ticket=False
            return None
        Choose["text"]="Универсал"
        Desk.destroy()
        Desk = Frame(win,bg="#BBB")
        Desk.place(relx=.1955,rely=0.2,relwidth=.55,relheight=.657)
        
        global Name
        global Stat
        global n1
        LAB=[]
        
        for _ in range(cycle):
            global Digit
            print("PPPP",str(n1))
            if _>4:
                LAB.append(0)
                Digit.append(0)
                LAB[_]= Label(Desk,text=n1[_],background="#BBB", height=1,font="Arial 10 bold")
                LAB[_].place(relx=.55,rely=.035+(_-5)*0.21,relwidth=.3)
                Digit[_]= Text(Desk,background="#CCC",width=5, height=1,font="Arial 10")
                Digit[_].insert(1.0,"0")
                Digit[_].place(relx=.83,rely=.043+(_-5)*0.21)
            else:
                Digit.append(0)
                Digit[_]= Text(Desk,background="#CCC",width=5, height=1,font="Arial 10")
                Digit[_].insert(1.0,"0")
                Digit[_].place(relx=.35,rely=.043+_*0.21)
                LAB.append(0)
                LAB[_]= Label(Desk,text=n1[_],background="#BBB", height=1,font="Arial 10 bold")
                LAB[_].place(relx=.05,rely=.035+_*0.21,relwidth=.3)
        Choose["command"]=CreateDesk
        Ticket=True
        global n2
        for i in range(cycle):
            n2[i]=int(n2[i])
            n2[i]*=int(PM[i])
        DOC=str(n1)+str(n2)
        print("n",n2)
        with open("Универсал.txt","a") as P:
            P.write(DOC)
    Choose["text"]="Универсал"
    global Desk
    global DeskCheck
    if DeskCheck==True:
        DeskCheck=False
        global cycle
        cycle=0
        Desk.destroy()
        Choose["text"]="Стандарт"
        return None
    PM=[]
    def conf():
        global n1
        global n2
        n1.append(0)
        n2.append(0)
        t1=(Cat.get(1.0,END))
        
        t2=Num.get(1.0,END)
        t1=t1[:-1]
        t2=t2[:-1]
        print("dfd",len(re.findall(r"[\D\n\s]+",t2[:-1])) )
        if len(re.findall(r"[\D\n\s]+",t2[:-1]))>0:
            return messagebox.showinfo("Неверные символы","Введите число от 0 до 100")
        if int(t2)<-100 or int(t2)>100:
            return messagebox.showinfo("Неверные символы","Введите число от 0 до 100")
        if t1=="" or t2=="":
            return messagebox.showinfo("Неверные символы","Введите категорию")
        global Name
        global Stat
        global cycle

        n1[cycle]=t1
        n2[cycle]=t2
        if cycle==0:
            Confirm = Button(Desk,text="Принять",font="Arial 12",command=CreateDesk,bd=0,bg="#999")
            Confirm.place(anchor="c",relx=.91,rely=.2,relheight=.1)
        Name.append(0)
        Stat.append(0)
        #Задает отрицательный или положительный коэффициент
        def PlusMinus(e):
            a=int(str(e.widget)[-1:])
            if e.widget["bg"]!="#E72B2B":
                e.widget["bg"]="#E72B2B"
                print(e.widget)
                PM[a-3]="-1"
            else:
                e.widget["bg"]="#7FBC4C"
                PM[a-3]="1"
            print(PM)
        if cycle>4:
            if cycle==10:
                return messagebox.showinfo("Ограничение","Список не должен превышать 10 пунктов")
            Name[cycle]=Label(Desk,text=t1,font="Arial 11",bg="#999")
            Name[cycle].place(anchor="c",relx=.7,rely=.38+(cycle-5)/7,relwidth=.3)
            Stat[cycle]=Button(Desk,text=t2,font="Arial 11",bg="#7FBC4C",bd=0)
            Stat[cycle].bind("<1>",PlusMinus)
            Stat[cycle].place(anchor="c",relx=.9,rely=.38+(cycle-5)/7,relwidth=.1,relheight=.08)
            PM.append(1)
        else:
            Name[cycle]=Label(Desk,text=t1,font="Arial 11",bg="#999")
            Name[cycle].place(anchor="c",relx=.2,rely=.38+cycle/7,relwidth=.3)
            Stat[cycle]=Button(Desk,text=t2,font="Arial 11",bg="#7FBC4C",bd=0)
            Stat[cycle].bind("<1>",PlusMinus)
            Stat[cycle].place(anchor="c",relx=.4,rely=.38+cycle/7,relwidth=.1,relheight=.08)
            PM.append(1)
        cycle+=1
        
    if Ticket==True:
        end=Univ.find("]")
        names = re.findall(r"[\w[\s\w]*]+",Univ[:end])
        numbers = re.findall(r"[\d]+",Univ[end:])
        Choose["text"]="Универсал"
        Choose["command"]=CreateDesk
        cycle = len(names)
        print(names)
        Desk = Frame(win,bg="#BBB")
        Desk.place(relx=.1955,rely=0.2,relwidth=.55,relheight=.657)
        LAB=[]
        
        for _ in range(cycle):
            print("PPPP",str(n1))
            if _>4:
                LAB.append(0)
                Digit.append(0)
                LAB[_]= Label(Desk,text=names[_],background="#BBB", height=1,font="Arial 10 bold")
                LAB[_].place(relx=.55,rely=.035+(_-5)*0.21,relwidth=.3)
                Digit[_]= Text(Desk,background="#CCC",width=5, height=1,font="Arial 10")
                Digit[_].insert(1.0,"0")
                Digit[_].place(relx=.83,rely=.043+(_-5)*0.21)
            Digit.append(0)
            Digit[_]= Text(Desk,background="#CCC",width=5, height=1,font="Arial 10")
            Digit[_].insert(1.0,"0")
            Digit[_].place(relx=.35,rely=.043+_*0.21)
            LAB.append(0)
            LAB[_]= Label(Desk,text=names[_],background="#BBB", height=1,font="Arial 10 bold")
            LAB[_].place(relx=.05,rely=.035+_*0.21,relwidth=.3)
    Desk = Frame(win,bg="#BBB")
    Desk.place(relx=.1955,rely=0.2,relwidth=.55,relheight=.657)
    Cat = Text(Desk,bg="#888")
    Cat.place(anchor="c",relx=.2,rely=.2,relwidth=.3,relheight=.1)
    Num = Text(Desk,bg="#888")
    Num.place(anchor="c",relx=.55,rely=.2,relwidth=.3,relheight=.1)
    CatL = Label(Desk,text="Категория",bg="#BBB",font="Arial 12")
    CatL.place(anchor="c",relx=.2,rely=.1)
    NumL = Label(Desk,text="Соотношение",bg="#BBB",font="Arial 12")
    NumL.place(anchor="c",relx=.55,rely=.1)
    OK = Button(Desk,text="Ok",font="Arial 12",command=conf,bd=0,bg="#999")
    OK.place(anchor="c",relx=.765,rely=.2,relheight=.1,relwidth=.1)
    DeskCheck=True
    #Очистить
def CL():
    if Ticket2==2:
        global Digit
        global cycle
        for i in range(cycle):
            Digit[i].delete(1.0,END)
            Digit[i].insert(1.0,"0")
    Text1.delete(1.0,END)
    Text2.delete(1.0,END)
    Text3.delete(1.0,END)
    Text4.delete(1.0,END)
    Text5.delete(1.0,END)
    Text6.delete(1.0,END)
    Text7.delete(1.0,END)
    Text8.delete(1.0,END)
    Text1.insert(1.0,"0")
    Text2.insert(1.0,"0")
    Text3.insert(1.0,"0")
    Text4.insert(1.0,"0")
    Text5.insert(1.0,"0")
    Text6.insert(1.0,"0")
    Text7.insert(1.0,"0")
    Text8.insert(1.0,"0")
#Анимирование кнопок
def foo():
    BUTTON2['bg']="#000"
#Страницы
def LP():
    LyceumPage.place(relx=.1955,rely=0.2)
    Lyceum["bg"]="#BBB"

#Контекстное меню
def menu3(event):
    global x,y
    x=event.x
    y=event.y
    clickm.post(event.x_root,event.y_root)
#Загрузка
def reading():
    st2=st
    data2=data
    n3=0
    match1 = re.search(r"\[",st2)
    l = len(re.findall(r"\[",st2))
    name=""
    global namelist
    namelist = []
    for _ in range(l):
        st2=st2[n3:]
        n1=st2.find("[")+1
        n2=st2.find("]")
        n3=st2.find(";")+1
        name = st2[n1:n2]
        namelist.append(name)
        lbox.insert(0,name)
#Сохранение
def download():
    global Digit
    global Ticket2
    global Ticket
    print(Ticket2,"TTTT")
    print(Ticket,"ttttt")
    if Ticket2==2:
        print("DONE")
        
        try:
            with open("{x}{y}un.txt".format(x=Calendar[date.month-1],y=str(date.year))) as D:
                NAME= D.read()
            subprocess.check_call(["attrib","+H","{x}{y}un.txt".format(x=Calendar[date.month-1],y=str(date.year))])
        except:
            with open("{x}{y}un.txt".format(x=Calendar[date.month-1],y=str(date.year)),"w+") as D:
                NAME= D.read()
            subprocess.check_call(["attrib","+H","{x}{y}.txt".format(x=Calendar[date.month-1],y=str(date.year))])
        print("NAME",NAME)
        Check = re.findall(r"\[[\w\s]+\]",NAME)
        print("CH",Check)
        select = lbox.curselection()
        name1="["+str(lbox.get(select[0]))+"]"
        print(Check," ", name1)
        for i in range(len(Check)):
            if Check[i]==name1:
                return messagebox.showinfo("Заполнено","Данные уже записаны")
        
        name1=name1+":"
        global cycle
        global cycle2
        if Ticket==False:
            cyc=cycle2
        if Ticket==True:
            cyc=cycle
        print(type(cyc))
        if type(cyc)==type(list):
            cyc=int(cyc[0])
        print(cyc)
        for _ in range(cyc):
            if _==cyc-1:
                name1+=str(float(Digit[_].get(1.0,END)))+";"
                break
            a =str(float(Digit[_].get(1.0,END)))
            name1+=a[:]+","
        NAME+=name1
        lbox.delete(select[0])
        print("name1",name1)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{x}{y}un.txt'.format(x=Calendar[date.month-1],y=str(date.year)))
        os.remove(path)
        with open( '{x}{y}un.txt'.format(x=Calendar[date.month-1],y=str(date.year)),"w+") as P:
            P.write(NAME)
        return None
    with open("{x}{y}.txt".format(x=Calendar[date.month-1],y=str(date.year))) as D:
        name= D.read()
    subprocess.check_call(["attrib","+H","{x}{y}.txt".format(x=Calendar[date.month-1],y=str(date.year))])
    Check = re.findall(r"\[[\w\s]+\]",name)
    select = lbox.curselection()
    name1="["+str(lbox.get(select[0]))+"]"
    print(Check," ", name1)
    for i in range(len(Check)):
        if Check[i]==name1:
            return messagebox.showinfo("Заполнено","Данные уже записаны")
    name1=name1+":"
    s=[]
    for i in range(10):
        s.append(0)
    lbox.delete(select[0])
    file1=lbox.get(0,END)
    lbox.insert(select[0])
    l = len(file1)
    s[0] = str(float(Text1.get(1.0, END)))
    s[1] = str(float(Text2.get(1.0, END)))
    s[2] = str(float(Text3.get(1.0, END)))
    s[3] = str(float(Text4.get(1.0, END)))
    s[4] = str(float(Text5.get(1.0, END)))
    s[5] = str(float(Text6.get(1.0, END)))
    s[6] = str(float(Text7.get(1.0, END)))
    s[7] = str(float(Text8.get(1.0, END)))
    name+=name1
    for _ in range(8):
        name+=s[_]
        if _<7:
            name+=","
    name+=";"
    print(name)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{x}{y}.txt'.format(x=Calendar[date.month-1],y=str(date.year)))
    os.remove(path)
    with open( '{x}{y}.txt'.format(x=Calendar[date.month-1],y=str(date.year)),"w+") as P:
        P.write(name)
#Удалить (Готово и проверено)
def delete():
    name=""
    try:
        select = lbox.curselection()
        lbox.delete(select[0])
    except:
        return None
    file1=lbox.get(0,END)
    l = len(file1)
    for _ in range(l):
        file=str(file1[_])
        file=(file.replace("'",""))
        file=(file.replace(",",""))
        file=(file.replace(" ",""))
        file="["+file+"]:;"
        name+=file
    print(name)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"Данные.txt")
    os.remove(path)
    with open("Данные.txt","w") as P:
            P.write(name)
#Добавить (Готово и Проверено)
def append():
    def ins():
        def lam():
            try:
                ln["text"]="Введите Ф.И.О."
                ln["font"]="Arial 12 bold"
                ln["foreground"]="#000"
                return None
            except:
                return None
        with open("Данные.txt") as P:
            R = P.read()
        print("R",R)
        namelist2 = re.findall(r"\[[\w\s]+\]",R)
        name=tn.get(1.0, END)
        name=name[:-1]
        for _ in range(len(namelist2)):
            print( namelist2[_]+" "+"["+name+"]")
            if namelist2[_]=="["+name+"]":
                ln["text"]="Имя уже занято"
                ln["font"]="Arial 12 bold"
                ln["foreground"]="red"
                win.after(1500,lam)
                return None
        a=re.findall(r"\s",name)
        print(len(a),"ggg",len(name))
        if len(re.findall(r"[\d\n]",name))>0 or len(name)==len(re.findall(r"\s",name)):
            ln["text"]="Сторонние символы"
            ln["font"]="Arial 12 bold"
            ln["foreground"]="red"
            win.after(1500,lam)
            return None
        lbox.insert(0,name)
        with open("Данные.txt","a") as P:
            P.write("["+name+"]"+":;")
        data.destroy()
    def canc():
        data.destroy()
        win.unbind("<Return>")
    data=Frame(win,width=250, height=150, background="#DDD", borderwidth=2,relief="solid")
    data.place(relx=.25,rely=.25)
    ln=Label(data,text="Введите Ф.И.О.",background="#DDD",font="Arial 12 bold")
    ln.place(relx=.15,rely=.2,relwidth=.7)
    tn= Text(data, background="#CCC",relief="solid",height=1)
    tn.place(relx=.15,rely=.45,relwidth=.7)
    OK = Button(data,text="Принять",background="#CCC",bd=0,command=ins,font="Arial 9")
    OK.place(relx=.035,rely=.7,relwidth=.45,relheight=0.25)
    CANCEL = Button(data,text="Отмена",background="#CCC",bd=0,command=canc,font="Arial 9")
    CANCEL.place(relx=.515,rely=.7,relwidth=.45,relheight=0.25)
    win.bind("<Return>",ins)
#Инструкция
def helper():
    root=Toplevel(win)
    root.title("Инструкция")
    root.geometry("400x420")
    root.resizable(False,False)
    h1 = Label(root,font="Arial 12",text="Что это?\nЭто версия 3.1. оценки производительности педагога.\nЦель: Помощь в продуктивности\nСтатус: Альфа тест",background="#ccc",wraplength=400)
    h1.place(relx=.02,rely=.01)
    txt1 = """Рабочее пространство.
•Стандарт – смена 2 режимов работы (стандартный и индивидуальный).
•Очистить – очистка всех полей ввода.
Правая панель.
•Сохранение – данные переводятся в формате json в память компьютера.
•История – просмотр истории за весь год.
•Рейтинг - просмотр рейтинга за весь год.
•Высчитать – просмотр статистики, советов по оптимизации и т.д.
•Выйти – выход из программы.
Журнал.
•Добавить – добавить сотрудника в систему.
•Удалить – удаление сотрудника из системы.
"""
    h2 = Label(root,font="Arial 12",text=txt1,background="#ccc",justify=LEFT,wraplength=389)
    h2.place(relx=.02,rely=.25)
    
    root.mainloop()
#Выйти
def func():
    import sys
    win.destroy()
    sys.exit()
#Вычислить
def getText():
    global Ticket2
    global Uni
    if Ticket2==2:
        numbers=re.findall(r"\d+",Uni)
        a = lbox.get(lbox.curselection())
        TF=False
        s=[]
        d=[]
        leng=len(re.findall(r"[a-zA-ZА-Яа-я]+",Uni))
        for i in range(leng):
            s.append(0)
            d.append(0)
            d[i]=numbers[i]
            s[i] = float(Digit2[i].get(1.0, END))
        try:
            
            for ii in range(leng):
                if s[ii]>-1 and s[ii]<101:
                    TF = True
                if s[ii]<-1 or s[ii]>101:
                    messagebox.showwarning("Ой! ошибка","Неверное число")
                    TF = False
                    break
        except:
            messagebox.showwarning("Ой! Ошибка","Неверные символы")
            TF = False
        if TF:
            result=0
            for i in range(leng):
                d.append(0)
                result += int(s[i]/100*d[i])
            print("res",result)
            if result < 40:
                adv="У {x} низкий результат, стоит срочно повысить показатели.".format(x=lbox.get(lbox.curselection()))
            if result > 40 and result < 60:
                adv="Стабильный результат."
            if result > 60 and result < 80:
                adv="Довольно хороший показатель."
            if result > 80:
                adv = "У вас отличные показатели"
            if s[0]<45 and s[0]>20 or s[1]<45 and s[1]>20 or s[2]<45 and s[2]>20:
                adv2="Советуем уделить внимание методу обучения, возможно стоит подобрать более лучший подход к ученикам"
            if s[3]<45 and s[3]>20 or s[4]<45 and s[4]>20:
                adv3="Предлагаем обновить свои знания и опыт. Вы можете найти информацию о современных новшествах в вашей сфере, посетить тренинги и подойти к обучению более творчески"

            graf = Toplevel(win,background="gray")
            #graf.geometry("550x300")
            graf.title("График")
            graf.resizable(False,False)
            CANV = Canvas(graf,width=550,height=300)
            CANV.pack()
            CANV.create_line(10,220,10,1,width=2,arrow=LAST)
            CANV.create_line(10,220,220,220,width=2,arrow=LAST)
            dist=10
            for i in range(9):
                #X
                CANV.create_text(dist+(i*20),230,text=str(i),font="Arial 6")
                #Y
                CANV.create_text(5,220-(i*20),text=str(i),font="Arial 6")
                dist = dist+3
                #Шкалы
            dist=25
            dist2=35
            for j in range(8):
                if j<5:
                    CANV.create_rectangle(dist+(j*20),220,dist2+(j*20),220-s[j]*2,width=2,fill="#cdf")
                if j>4 and j<7:
                    CANV.create_rectangle(dist+(j*20),220,dist2+(j*20),220-s[j]*2,width=2,fill="#ec1a28")
                if j==7:
                    CANV.create_rectangle(dist+(j*20),220,dist2+(j*20),220-s[j]*2,width=2,fill="yellowgreen")
                dist=dist+3.5
                dist2=dist2+3.5
            CANV.create_text(90,270,text="Результат:"+str(result),font="Arial 16")
            try:
                #ФИО и совет в окне графики
                CANV.create_text(400,20,text=lbox.get(lbox.curselection()),font="Arial 16")
                CANV.create_text(400,70,text=adv,font="Arial 12",width=300)
                CANV.create_text(400,120,text=adv2,font="Arial 12",width=300)
                CANV.create_text(405,200,text=adv3,font="Arial 12",width=300)
            except:
                None
    if Ticket2==0 or Ticket2==1:
        try:
            a = lbox.get(lbox.curselection())
            TF=False
            s=[]
            d=[]
            for i in range(10):
                s.append(0)
            try:
                s[0] = float(Text1.get(1.0, END))
                s[1] = float(Text2.get(1.0, END))
                s[2] = float(Text3.get(1.0, END))
                s[3] = float(Text4.get(1.0, END))
                s[4] = float(Text5.get(1.0, END))
                s[5] = float(Text6.get(1.0, END))
                s[6] = float(Text7.get(1.0, END))
                s[7] = float(Text8.get(1.0, END))
                for i in range(8):
                    if s[i]>-1 and s[i]<101:
                        TF = True
                    if s[i]<-1 or s[i]>101:
                        messagebox.showwarning("Ой! ошибка","Неверное число")
                        TF = False
                        break
            except:
                messagebox.showwarning("Ой! Ошибка","Неверные символы")
                TF = False
            if TF:
                adv2 = ""
                adv3 = ""
                for i in range(10):
                    d.append(0)
                result = int(s[0]/5+s[1]/5+s[2]/100*15+s[3]/100*15+s[4]/10-s[5]/10-s[6]/10+s[7])
                if result < 72:
                    adv="У {x} низкий результат, стоит срочно повысить показатели.".format(x=lbox.get(lbox.curselection()))
                if result > 72 and result < 108:
                    adv="Стабильный результат."
                if result > 108 and result < 144:
                    adv="Довольно хороший показатель."
                if result > 144:
                    adv = "У вас отличные показатели"
                if s[0]<45 and s[0]>20 or s[1]<45 and s[1]>20 or s[2]<45 and s[2]>20:
                    adv3="Советуем уделить внимание методу обучения, возможно стоит подобрать более лучший подход к ученикам"
                if s[3]<45 and s[3]>20 or s[4]<45 and s[4]>20:
                    adv2="Предлагаем обновить свои знания и опыт. Вы можете найти информацию о современных новшествах в вашей сфере, посетить тренинги и подойти к обучению более творчески"
                if s[0] < 60:
                    adv2 = "Стоит уделить внимание изучению английского языка среди учеников, советуем провести интерактивное мероприятие для привлечения изучения английского языка"
                if s[1] < 60:
                    adv2 = "Срочно начните подготовку учеников к поступлению, рекомендуем создать проф. курсы по подготовке ко вступительным испытаниям"
                if s[6] > 10:
                    adv2 = "Задумайтесь о новом режиме, за этот месяц вы часто опаздываете"
                graf = Toplevel(win,background="gray")
                #graf.geometry("550x300")
                graf.title("График")
                graf.resizable(False,False)
                CANV = Canvas(graf,width=550,height=300)
                CANV.pack()
                CANV.create_line(10,220,10,1,width=2,arrow=LAST)
                CANV.create_line(10,220,220,220,width=2,arrow=LAST)
                dist=10
                for i in range(9):
                    #X
                    CANV.create_text(dist+(i*20),230,text=str(i),font="Arial 6")
                    #Y
                    CANV.create_text(5,220-(i*20),text=str(i),font="Arial 6")
                    dist = dist+3
                    #Шкалы
                dist=25
                dist2=35
                for j in range(8):
                    if j<5:
                        CANV.create_rectangle(dist+(j*20),220,dist2+(j*20),220-s[j]*2,width=2,fill="#cdf")
                    if j>4 and j<7:
                        CANV.create_rectangle(dist+(j*20),220,dist2+(j*20),220-s[j]*2,width=2,fill="#ec1a28")
                    if j==7:
                        CANV.create_rectangle(dist+(j*20),220,dist2+(j*20),220-s[j]*2,width=2,fill="yellowgreen")
                    dist=dist+3.5
                    dist2=dist2+3.5
                CANV.create_text(90,270,text="Результат:"+str(result),font="Arial 16")
                try:
                    #ФИО и совет в окне графики
                    CANV.create_text(400,20,text=lbox.get(lbox.curselection()),font="Arial 16")
                    CANV.create_text(250,70,text=adv,font="Arial 12",width=300, anchor = W)
                    CANV.create_text(250,130,text=adv2,font="Arial 12",width=300, anchor = W)
                    CANV.create_text(250,200,text=adv3,font="Arial 12",width=300, anchor = W)
                except:
                    None
        except:
            return messagebox.showinfo("Кто это?","Выберите сотрудника")
#История
def history():
    global Ticket
    global Ticket2
    if Ticket2==2:
        z="un"
    if Ticket2==0 or Ticket2==1:
        z=""
    def Date():
        #Поиск по датам
        def search():
            def lim():
                head["text"]="Выберите дату"
                head["fg"]="black"
            a1=Ent2.get()
            a2=Ent3.get()
            if a1=="" and a2=="":
                head["text"]="Неверный ввод"
                head["fg"]="red"
                C.after(1000,lim)
                return None
            else:
                date=Calendar[int(a1)-1]+str(a2)
                date2=Calendar[int(a1)-1]+" "+str(a2)
                
            F2=Frame(F,bg="#666")
            F2.place(anchor="c",relx=.5,rely=.5,relwidth=1,relheight=1)    
                
            print(date)
            B["text"]=date2
            try:
                with open("{x}{z}.txt".format(x=date,z=z)) as P:
                    Names1=P.read()
            except:
                Names1=""
            N = re.sub(r"\d","",Names1)
            N=re.findall(r"\w+[\s\w]*",N)
            leng = len(N)
            print("pro",N)
            #Имена и данные
            for i in range(leng):
                Names=Names1
                num = re.findall(r"\d+\.\d+",Names)
                print("num",num)
                Names = re.sub(r"\d","",Names)
                Names = re.findall(r"\w+[\s\w]*",Names)
                print("Names",Names)
                l = re.findall(r"[\d+\.\d+,]+;",Names1)
                l = l[0]
                l = re.findall(r",",l)
                NUMS=len(l)+1
                print(NUMS)
                SUM=0
                for _ in range(NUMS):
                    SUM+=float(num[_+i*NUMS])
                    if _==NUMS-1:
                        result=Label(F2,text=round(SUM/NUMS,2),font="Arial 14",bg="#C9C9C9")
                        result.place(anchor="n",relx=.24025+(_+1)/14,rely=.002+i/31.25,relwidth=.08,relheight=.03)
                    D.append(0)
                    D[i] = Label(F2,text=num[_+i*NUMS],font="Arial 14")
                    D[i].place(anchor="n",relx=.23625+_/14,rely=.002+i/31.25,relwidth=.07,relheight=.03)
                num=num[NUMS:]
                L.append(0)
                L[i] = Label(F2,text=Names[i],font="Arial 12")
                L[i].place(anchor="n",relx=.1,rely=.002+i/31.25,relwidth=.2,relheight=.03)
            C2.destroy()
                
        def exit():
            C2.destroy()
        global C2
        C2=Frame(win,borderwidth=3,relief="solid")
        C2.place(relx=.5,rely=.5,anchor="c",relwidth=.4,relheight=.4)
        head = Label(C2,text="Выберите дату",font="Arial 14")
        head.place(relx=.1,rely=.05,relwidth=.8,relheight=.2)
        Ent2 = Entry(C2,font="Arial 12",justify=CENTER)
        Ent3 = Entry(C2,font="Arial 12",justify=CENTER)
        Ent2.place(relx=.1,rely=.45,relwidth=.3,relheight=.2)
        Ent3.place(relx=.6,rely=.45,relwidth=.3,relheight=.2)
        Lab2 = Label(C2,text="Месяц",font="Arial 14")
        Lab3 = Label(C2,text="Год",font="Arial 14")
        Lab2.place(relx=.1,rely=.25,relwidth=.3,relheight=.2)
        Lab3.place(relx=.6,rely=.25,relwidth=.3,relheight=.2)
        Conf = Button(C2,text="Подтвердить",font="Arial 12",command=search)
        Conf.place(relx=.55,rely=.7,relwidth=.4,relheight=.2)
        Cancel = Button(C2,text="Отмена",font="Arial 12",command=exit)
        Cancel.place(relx=.05,rely=.7,relwidth=.4,relheight=.2)
    def exit():
        global C2
        win.unbind("<MouseWheel>")
        C.destroy()
        F.destroy()
        if C2!=0:
            C2.destroy()
    C = Canvas(win,width=wid,height=hei)
    C.place(anchor="c",relx=.5,rely=.5,relwidth=1,relheight=1)
    #Кнопка поиска по датам

    #Frame(Таблица рейтингов)
    F=Frame(C,bg="#666",height=1000)
    F.place(anchor="n",relx=.5,rely=.15,relwidth=1)
    BACK=Label(C,bg="#CCC")
    BACK.place(relx=.5,rely=.05,anchor="c",relheight=.2,relwidth=1)
    B = Button(C,text=Calendar[date.month-1]+" "+str(date.year),font="Arial 17 bold",command=Date)
    B.place(relx=.5,rely=.075,anchor="c",relheight=.1,relwidth=.4)
    L=[]
    D=[]
    text=[]
    if Ticket2==2:
        z="un"
    elif Ticket2==1 or Ticket==0:
        z=""
    try:
        with open("{x}{y}{z}.txt".format(x=Calendar[date.month-1],y=str(date.year),z=z)) as P:
            Names1=P.read()
    except:
        with open("{x}{y}{z}.txt".format(x=Calendar[date.month-1],y=str(date.year),z=z),"w+") as P:
            Names1=P.read()
    N = re.sub(r"\d","",Names1)
    N=re.findall(r"\w+[\s\w]*",N)
    leng = len(N)
    if leng>10:
        def c(e):
            global N
            global y
            yy=leng
            if y>.14:
                if e.delta==120:
                    y-=0.025
                    F.place(rely=y)
                return None
            if y<(yy-yy*2)*0.01:
                if e.delta==-120:
                    y+=0.025
                    F.place(rely=y)
                return None
            if e.delta==120:
                y-=0.025
                F.place(rely=y)
            if e.delta==-120:
                y+=0.025
                F.place(rely=y)
        win.bind("<MouseWheel>",c)
    #Имена и данные
    for i in range(leng):
        Names=Names1
        num = re.findall(r"\d+\.\d+",Names)
        Names = re.sub(r"\d","",Names)
        Names = re.findall(r"\w+[\s\w]*",Names)
        l = re.findall(r"[\d+\.\d+,]+;",Names1)
        l = l[0]
        l = re.findall(r",",l)
        NUMS=len(l)+1
        SUM=0
        for _ in range(NUMS):
            SUM+=float(num[_+i*NUMS])
            if _==NUMS-1:
                result=Label(F,text=round(SUM/NUMS,2),font="Arial 14",bg="#C9C9C9")
                result.place(anchor="n",relx=.241+(_+1)/14,rely=.002+i/31,relwidth=.078,relheight=.0304)
            D.append(0)
            print(num[_+i*NUMS])
            D[i] = Label(F,text=num[_+i*NUMS],font="Arial 14")
            D[i].place(anchor="n",relx=.236+_/14,rely=.002+i/31,relwidth=.07,relheight=.0304)
        L.append(0)
        L[i] = Label(F,text=Names[i],font="Arial 12")
        L[i].place(anchor="n",relx=.1,rely=.002+i/31,relwidth=.2,relheight=.0304)
    res = Canvas(C,bg="#DDDDDD")
    res.place(relx=0,rely=.92,relwidth=1,relheight=.08)
    butbox=Frame(res,bd=0,bg="#DDD",width=300)
    butbox.place(anchor="e",relx=1,rely=.5,relheight=.9)
    exit= Button(butbox,text="Выйти",bd=0,bg="#CCCCCC",font="Arial 12",command=exit,width=10).place(anchor="e",relx=1,rely=.5,relheight=1)
#Рейтинг
def rating():
    divider=[]
    global Ticket2
    global Ticket
    if Ticket2==2:
        z="un"
        with open("Универсал.txt") as P:
            coefficient=P.read()
        coefficient=re.findall(r"\d+",coefficient)
    elif Ticket2==1 or Ticket==0:
        z=""
        coefficient=[25,25,15,15,10,-10,-10,10]
    with open("Данные.txt") as P:
        Names1=P.read()
    def exit():
        win.unbind("<MouseWheel>")
        C.destroy()
    L=[]
    C=Canvas(win,bg="#666",width=wid,height=hei)
    C.pack()
    x=0.5
    y=0.125
    f = Frame(C,height=1000,bg="#666")
    f.place(anchor="n",relx=x,rely=y,relwidth=1)
    
    i=0
    try:
        dig=[]
        nam=[]
        while True:
            with open("{x}{y}{z}.txt".format(x=Calendar[date.month-1-i],y=str(date.year),z=z)) as D:
                Month=D.read()
            dig+=re.findall(r"[\d\.\d]+",Month)
            n = re.sub(r"\d","",Month)
            nam+=re.findall(r"\w+[\s\w]*",n)
            i+=1
    except:
        None
    d=[]
    E=[]
    num=[]
    if len(nam)==0:
        dig=0
    else:
        dig=len(dig)/len(nam)
    for __ in range(int(dig)):
        d.append(0.0)
    N = re.sub(r"\d","",Names1)
    N=re.findall(r"\w+[\s\w]*",N)
    leng = len(N)
    #Имена и данные
    if leng>10:
        def c(e):
            global N
            global y
            yy=leng
            if y>.12:
                if e.delta==120:
                    y-=0.025
                    f.place(rely=y)
                return None
            if y<(yy-yy*2)*0.01:
                if e.delta==-120:
                    y+=0.025
                    f.place(rely=y)
                return None
            if e.delta==120:
                y-=0.025
                f.place(rely=y)
            if e.delta==-120:
                y+=0.025
                f.place(rely=y)
        win.bind("<MouseWheel>",c)
    a=0
    for u in range(len(coefficient)):
        coefficient[u]=float(coefficient[u])
    sum_coefficient=sum(filter(lambda x:x>0,coefficient))
    for j in range(len(coefficient)):
        coefficient[j]=coefficient[j]/(sum_coefficient/100)
    NUMS=[]
    m=[]
    for ii in range(leng):#Выбор имени
        d=[]
        dele=[]
        middle=i
        for __ in range(int(dig)):
            d.append(0.0)
            NUMS.append(0.0)
        for _ in range(i):#Выбор месяца
            num=[]
            time=Calendar[date.month-1-_]+str(date.year)
            with open("{x}{z}.txt".format(x=time,z=z)) as D:
                Month=D.read()
            num.append(0.0)
            beg=Month.find("["+N[ii]+"]")
            num=re.findall(r"[\d\.\d]+",Month[beg:])
            num=num[:int(dig)]
            for iii in range(int(dig)):#Переприсвоение чисел
                if num==[]:
                    a+=1
                    middle-=1
                    break
                dele.append(0)
                d[iii]+=float(num[iii])
                NUMS[iii]+=float(num[iii])
        D=[]
        def ratinghistory(e):
            global Ticket2
            if Ticket2==2:
                z="un"
                global cycle
                global cycle2
                if Ticket==False:
                    cyc=cycle2
                if Ticket==True:
                    cyc=cycle
            if Ticket2==0 or Ticket2==1:
                cyc=8
                z=""
            def exit2():
                Fr.destroy()
            a=str(e.widget)
            a=re.findall(r"\d+",a[-2:])
            print(a,"a")
            if a==[]:
                a=[1]
            a=int(a[0])-1
            Fr = Frame(win,bg="#666")
            Fr.place(anchor="c",relx=.5,rely=.5,relwidth=1,relheight=1)
            L=Label(Fr,text=N[a],font="Arial 17 bold")
            
            L.place(relx=.0,rely=.1,anchor="w",relheight=.2,relwidth=.4)
            i=0
            txt=[]
            try:
                while True:
                    txt.append(0)
                    
                    with open("{x}{y}{z}.txt".format(x=Calendar[date.month-i-1],y=str(date.year),z=z)) as P:
                        txt[i]=P.read()
                    i+=1
            except:
                None
            L2=[]
            L3=[]
            numbers=[]
            o=i
            ZP_result=0
            for _ in range(i):#Месяц
                seq = txt[_].find("["+N[a]+"]")
                if seq==-1:
                    o-=1
                    break
                seq = len(re.findall(r"\[",txt[_][:seq]))
                del numbers
                numbers=[]
                beg = txt[_].find(N[a])
                y=.2+(_)/14
                if beg!=-1:
                    txt[i]=txt[_][beg:]
                    end = txt[_].find(";")
                    txt[i]=txt[_][:end]
                    numbers = re.findall(r"[\d\.\d]+",txt[_])
                    global n2
                    L3.append(0)
                    L3[_]=Label(Fr,text="{x}{y}{z}".format(x=Calendar[date.month-_-1],y=str(date.year),z=z),font="Arial 13")
                    L3[_].place(anchor="n",relx=.1,rely=y,relwidth=.2,relheight=.067)
                    
                    SUM=0
                    for __ in range(cyc):#Числа/Данные
                        coefficient[__]=float(coefficient[__])
                        numbers[__+seq*cyc]=float(numbers[__+seq*cyc])
                        SUM+=numbers[__+seq*cyc]/100*coefficient[__]
                        if __==cyc-1:
                            result=Label(Fr,text=round(SUM,2),font="Arial 14",bg="#C9C9C9")
                            result.place(anchor="n",relx=.235+(__+1)/14.2,rely=y,relwidth=.07,relheight=.067)
                            ZP_result+=SUM
                        L2.append(0)
                        L2[__]=Label(Fr,text=round(numbers[__+seq*cyc]/100*coefficient[__],1),font="Arial 14")
                        L2[__].place(anchor="n",relx=.235+__/14,rely=y,relwidth=.07,relheight=.067)
            
            ZP_text=round(ZP_result/o,2)
            if ZP_text<30:
                ZP_text2="План не выполнен"
            if ZP_text>=30 and ZP_text<40:
                ZP_text2="-10%"
            if ZP_text>=40 and ZP_text<60:
                ZP_text2="Стабильно"
            if ZP_text>=60 and ZP_text<70:
                ZP_text2="+5%"
            if ZP_text>=70 and ZP_text<80:
                ZP_text2="+15%"
            if ZP_text>=80 and ZP_text<90:
                ZP_text2="+25%"
            if ZP_text>=90:
                ZP_text2="+30%"
                
            ZP=Label(Fr,text=str(ZP_text)+": "+ZP_text2,font="Arial 17 bold")
            ZP.place(relx=.5,rely=.1,anchor="w",relheight=.2,relwidth=.4)
            res = Canvas(Fr,bg="#DDDDDD",height=30)
            res.place(relx=0,rely=.9,relwidth=1)
            butbox=Frame(res,bd=0,bg="#DDD",width=300)
            butbox.place(anchor="e",relx=1,rely=.5,relheight=.9)
            exit= Button(butbox,text="Выйти",bd=0,bg="#CCCCCC",font="Arial 12",command=exit2,width=10).place(anchor="e",relx=1,rely=.5,relheight=1)
        if dig==0:
            divider.append(0)
        else:
            divider.append(len(dele)/dig)
        if divider[ii]==0:
            L.append(0)
            L[ii]=Button(f,text=N[ii],font="Arial 12")
            L[ii].place(anchor="n",relx=.1,rely=.002+ii/31,relwidth=.2,relheight=.0304)
            SUM=0
            for _i_ in range(len(coefficient)):
                if _i_==len(coefficient)-1:
                    result=Label(f,text="-/-",font="Arial 14",bg="#C9C9C9")
                    result.place(anchor="n",relx=.241+(_i_+1)/14,rely=.002+ii/31,relwidth=.078,relheight=.0304)
                D.append(0)
                D[_i_]=Label(f,text="-/-",font="Arial 14")
                D[_i_].place(anchor="n",relx=.235+_i_/14,rely=0.002+ii/31,relwidth=.07,relheight=.0304)
        
        else:
            L.append(0)
            L[ii]=Button(f,text=N[ii],font="Arial 12")
            L[ii].place(anchor="n",relx=.1,rely=.002+ii/31,relwidth=.2,relheight=.0304)
            L[ii].bind("<1>",ratinghistory)
            SUM=0
            for _i_ in range(len(coefficient)):
                SUM+=round(float(d[_i_])/100*coefficient[_i_],1)
                if _i_==len(coefficient)-1:
                    result=Label(f,text=SUM/len(coefficient),font="Arial 14",bg="#C9C9C9")
                    result.place(anchor="n",relx=.241+(_i_+1)/14,rely=.002+ii/31,relwidth=.078,relheight=.0304)
                D.append(0)
                D[_i_]=Label(f,text=round(float(d[_i_])/100*float(coefficient[_i_]),1),font="Arial 14")
                D[_i_].place(anchor="n",relx=.235+_i_/14,rely=0.002+ii/31,relwidth=.07,relheight=.0304)

    L = Label(C,text="Рейтинг",font="Arial 15",bg="#CCC")
    L.place(anchor="c",relx=.5,rely=.05,relwidth=1,relheight=.15)
    res = Canvas(C,bg="#DDDDDD")
    res.place(relx=0,rely=.92,relwidth=1,relheight=.08)
    butbox=Frame(res,bd=0,bg="#DDD",width=300)
    butbox.place(anchor="e",relx=1,rely=.5,relheight=.9)
    exit= Button(butbox,text="Выйти",bd=0,bg="#CCCCCC",font="Arial 12",command=exit,width=10).place(anchor="e",relx=1,rely=.5,relheight=1)
    
    def com():
        Alfabet=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
        wb = Workbook()
        sheet = wb.active
        sheet.title = "Отчет {x}".format(x=str(date.day)+Calendar[date.month]+str(date.year))
        row=1
        l=len(namelist)
        categories=[]
        if Ticket2==2:
            with open("Универсал.txt") as P:
                a=P.read()
            categories=re.findall(r"[a-zA-ZА-Яа-я]+",a)
        if Ticket2==1:
            categories=["IELTS","Поступаемость","Успехи учащихся","Повышение квалификации","Инициатива","Выговоры","Опаздания","Бонусы"]
        for i in range(len(categories)):
            print(categories)
            sheet[Alfabet[i+1]+"1"]=categories[i]
        for _ in range(l):
            print(divider[_])
            if divider[_]=="0.0":
                print(divider)
                break
            print(namelist[_])
            row+=1
            sheet["A"+str(row)]=namelist[_]
            for i in range(int(dig)):
                print(coefficient[i])
                sheet[Alfabet[i+1]+str(_+2)]=round(float(NUMS[i+_*int(dig)])/100*float(coefficient[i]),1)
        filename = 'Отчет{x}.xlsx'.format(x=str(date.day)+Calendar[date.month-1]+str(date.year))
        try:
            wb.save(filename)
        except:
            os.remove(filename)
            wb.save(filename)
    EXCEL = Button(butbox,text="Отчет в Excel",bg="#CCC",bd=0,fon="Arial 12",command=com)
    EXCEL.place(anchor="e",relx=.67,rely=.5,relheight=1)
#Главное окно
win=Tk()
Desk2=0
#Размер экрана
win.minsize(width=700,height=400)
win.resizable(False,False)
wid=win.winfo_screenwidth()
hei=win.winfo_screenheight()
#Меню 1
mainmenu = Menu(win,background="#999999")
win.config(menu=mainmenu)
filem = Menu(mainmenu,tearoff=0,font="arial 9")
helpm = Menu(mainmenu,tearoff=0,font="arial 9")
editm = Menu(mainmenu,tearoff=0,font="arial 9")
view = Menu(mainmenu,tearoff=0,font="arial 9")

mainmenu.add_cascade(label="Файл", menu=filem)
mainmenu.add_cascade(label="Правка",menu=editm)
mainmenu.add_cascade(label="Вид",menu=view)
mainmenu.add_cascade(label="Помощь", menu=helpm)

filem.add_command(label="Сохранить")
filem.add_command(label="Открыть")
filem.add_command(label="Новый файл")
filem.add_separator()
filem.add_command(label="Выход",command=func)

helpm.add_command(label="Помощь",command=helper)
helpm.add_separator()
helpm.add_command(label="О программе")

editm.add_command(label="Отменить")
editm.add_command(label="Выделить все")
editm.add_command(label="Убрать выделение")
editm.add_command(label="Очистить все")

view.add_command(label="Тема (скоро)",font="arial 9",foreground="#777777")
#Контекстное меню
win.bind("<Button-3>", menu3)

#win.iconbitmap("logo.ico")
win.title("Ассистент")
win.resizable(False,False)
win["bg"]="#CCCCCC"
win.wm_geometry("600x350")

#Меню3
clickm = Menu(win,tearoff=0)
clickm.add_command(label="Клик :)")

#Меню 2
LABELMENU = Label(win,text="Меню",font="Arial 18",bg="#bbbdbb")
LABELMENU.place(relx=.875,rely=.1,anchor="c",relwidth=0.24,relheight=0.2)


BUTTON0 = Button(win,text="Сохранить",bg="#bbbdbb",highlightcolor="#999",borderwidth=0,command=download,font="Monofur 14 ")
BUTTON0.place(relx=.875,rely=.27,anchor="c", relwidth=0.24,relheight=0.153)

BUTTON1 = Button(win,text="История",bg="#bbbdbb",highlightcolor="#999",font="Monofur 14",borderwidth=0,command=history)
BUTTON1.place(relx=.875,rely=.42,anchor="c", relwidth=0.24,relheight=0.153)


BUTTON2 = Button(win,text="Рейтинг",bg="#bbbdbb",highlightcolor="#999",font="Monofur 14",borderwidth=0,command=rating)
BUTTON2.place(relx=.875,rely=.57,anchor="c", relwidth=0.24,relheight=0.153)


BUTTON3 = Button(win,text="Выcчитать",bg="#bbbdbb",command=getText,highlightcolor="#999",font="Monofur 14",borderwidth=0)
BUTTON3.place(relx=.875,rely=.72,anchor="c", relwidth=0.24,relheight=0.153)

BUTTON4 = Button(win,text="Выйти",bg="#bbbdbb",command=func,highlightcolor="#999",font="Monofur 14",borderwidth=0)
BUTTON4.place(relx=.875,rely=.87,anchor="c", relwidth=0.24,relheight=0.153)

BUTTON5 = Button(win,text="Добавить",background="#AAA",bd=0,command=append,font="Monofur 12")
BUTTON5.place(relx=.08,rely=.7,anchor="c", relwidth=.2,relheight=.09)

BUTTON6 = Button(win,text="Удалить",background="#AAA",bd=0,command=delete,font="Monofur 12")
BUTTON6.place(relx=.08,rely=.81,anchor="c", relwidth=.2,relheight=.09)

LABELVERS = Label(win,text="Ли Дмитрий М. v.1.3",bg="#bbbdbb",font="Monofur 8",fg="#606260").place(relx=.875,rely=.97,anchor="c", relwidth=0.24,relheight=0.055)

#Таблица
LABELBOX = Label(win,text="Журнал",bg="#CCCCCC",font="Monofur 14 ")
LABELBOX.place(relx=.0123,rely=.12)
FR= Frame(win,bg="#000")
FR.place(relwidth=.18,relheight=.45,rely=0.2)
lbox = Listbox(FR,font="Arial 8 bold",bg="#CCC",bd=0)
 
lbox.place(relx=0,rely=0,relheight=1,relwidth=1)
scroll = Scrollbar(FR,command=lbox.yview)
scroll.pack(side="right", fill="y")
lbox.config(yscrollcommand=scroll.set)

#Поля ввода
#Лицей
LyceumPage = Frame(win,bg="#BBB")
LyceumPage.place(relx=.1955,rely=0.2,relwidth=.55,relheight=.657)

Text1= Text(LyceumPage,background="#CCC",width=5, height=1,font="Arial 10")
Text1.insert(1.0,"0")
Text1.place(relx=.35,rely=.07)
Text2= Text(LyceumPage,background="#CCC",width=5, height=1,font="Arial 10")
Text2.insert(1.0,"0")
Text2.place(relx=.35,rely=.28)
Text3= Text(LyceumPage,background="#CCC",width=5, height=1,font="Arial 10")
Text3.insert(1.0,"0")
Text3.place(relx=.35,rely=.49)
Text4= Text(LyceumPage,background="#CCC",width=5, height=1,font="Arial 10")
Text4.insert(1.0,"0")
Text4.place(relx=.35,rely=.7)

Text5= Text(LyceumPage,background="#CCC",width=5, height=1,font="Arial 10")
Text5.insert(1.0,"0")
Text5.place(relx=.83,rely=.07)
Text6= Text(LyceumPage,background="#CCC",width=5, height=1,font="Arial 10")
Text6.insert(1.0,"0")
Text6.place(relx=.83,rely=.28)
Text7= Text(LyceumPage,background="#CCC",width=5, height=1,font="Arial 10")
Text7.insert(1.0,"0")
Text7.place(relx=.83,rely=.49)
Text8= Text(LyceumPage,background="#CCC",width=5, height=1,font="Arial 10")
Text8.insert(1.0,"0")
Text8.place(relx=.83,rely=.7)

#Наименование полей ввода
LABEL1= Label(LyceumPage,text="IELTS",background="#BBB",width=12, height=2,font="Arial 9 bold")
LABEL1.place(relx=.07,rely=.035)
LABEL2= Label(LyceumPage,text="Поступаемость",background="#BBB",width=13, height=2,font="Arial 9 bold")
LABEL2.place(relx=.07,rely=.245)
LABEL3= Label(LyceumPage,text="Успехи\nучащихся",background="#BBB",width=12, height=2,font="Arial 9 bold")
LABEL3.place(relx=.07,rely=.455)
LABEL4= Label(LyceumPage,text="Повышение\nквалификации",background="#BBB",width=12, height=2,font="Arial 9 bold")
LABEL4.place(relx=.07,rely=.665)

LABEL5= Label(LyceumPage,text="Инициатива",background="#BBB",width=12, height=2,font="Arial 9 bold")
LABEL5.place(relx=.55,rely=.035)
LABEL6= Label(LyceumPage,text="Выговоры",background="#BBB",width=12, height=2,font="Arial 9 bold")
LABEL6.place(relx=.55,rely=.245)
LABEL7= Label(LyceumPage,text="Опаздания",background="#BBB",width=12, height=2,font="Arial 9 bold")
LABEL7.place(relx=.55,rely=.455)
LABEL8= Label(LyceumPage,text="Бонусы",background="#BBB",width=12, height=2,font="Arial 9 bold")
LABEL8.place(relx=.55,rely=.665)

Choose = Button(win,text="Стандарт",bg="#CCC",font="Arial 14",command=desk)
Choose.place(anchor="c",relx=.456,rely=.1,relwidth=.3,relheight=.1)
#Очистить
Clear = Button(win,text="Очистить",background="#BBB",font = "Monofur 12", width=10, height=1,bd=0,command=CL)
Clear.place(anchor="c",relx=.6455,rely=.925,relwidth=.2,relheight=.1)
reading()
listbox = lbox.get(0,END)
win.mainloop()