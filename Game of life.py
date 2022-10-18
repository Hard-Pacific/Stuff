# -*- coding: utf-8 -*-
import tkinter as tk
import numpy as np
import Rule

stop_ = False
#Начинает симуляцию
def start():
    #Считывает инфу со всех клетках на поле (Старую)
    old_map = np.array([])
    for i in range(900):
        x = 1 if cell[i]["bg"] == "#333333" else 0
        old_map = np.append(old_map, x)
    def start_2(old):
        game = Rule.game
        new_map = np.array(old)
        #Останавливает программу если нажата кнопка Stop
        global stop_ 
        if stop_:
            stop_ = False
            return None
        #Считывает инфу со всех клетках на поле
        for i in range(899, -1, -1):
            quan = 0
            #Считает живые клетки вокруг
            for x in range(3):
                quan += old[i - 60 - x]
                quan += old[i - 30 - x]
                quan += old[i - x]
            if old[i - 31] == 1:
                quan -= 1
            #Правила игры
            if quan in Rule.rules[game]["B"]:
                new_map[i - 31] = 1
                cell[i - 31]["bg"] = "#333333"
            elif quan not in Rule.rules[game]["S"]:
                new_map[i - 31] = 0
                cell[i - 31]["bg"] = "#FFFFFF"     
        win.after(100, start_2, new_map)
    start_2(old_map)

#Меняет цвет клетки при нажатии
def life_death(event):
    x = str(event.widget)
    x = x.replace(".!button","")
    x = 0 if x == "" else int(x)-1
    if cell[x]["bg"] == "#333333":
        cell[x]["bg"] = "#FFFFFF"
        return None
    cell[x]["bg"] = "#333333"

#Останавливает процесс и меняет правила
def Choose_the_rule():
    global stop_
    stop_ = True
    Rule.Next()
    Rule_Label["text"] = Rule.game
    
#Останавливает процесс
def stop():
    global stop_
    stop_ = True
    
#Останавливает процесс и очищает карту
def clear():
    global stop_
    stop_ = True
    for i in range(900):
        cell[i]["bg"] = "#FFFFFF"
            
win = tk.Tk()
win.title("Conwey's game of life")
win.geometry("+0+0")

cell = []
#Создает поле
for i in range(30):
    for j in range(30):
        cell.append(0)
        cell[i*30+j] = tk.Button(win, width =2, bg = "#FFFFFF", borderwidth = 1, relief = "ridge")
        cell[i*30+j].bind("<Button-1>", life_death)
        cell[i*30+j].grid(column = j, row = i)
        
start_Button = tk.Button(win, text = "Start", width = 11, font ="Arial 11", command = start)
start_Button.grid( row = 31, columnspan = 5, column = 0)

stop_Button = tk.Button(win, text = "Stop", width = 11, font ="Arial 11", command = stop)
stop_Button.grid(row = 31, columnspan = 5, column = 5)

clear_Button = tk.Button(win, text = "Clear", width = 11, font ="Arial 11", command = clear)
clear_Button.grid(row = 31, columnspan = 5, column = 10)

Rule_Button = tk.Button(win, text = "Rules", width = 11, font ="Arial 11", command = Choose_the_rule)
Rule_Button.grid(row = 31, columnspan = 5, column = 15)

Rule_Label = tk.Label(win, text = "Life", width = 11, font ="Arial 11")
Rule_Label.grid(row = 31, columnspan = 5, column = 20)

win.mainloop()
