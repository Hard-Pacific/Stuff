import tkinter as tk
import math

# Шифр Цезаря
def Ave_():
    alfa = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
    alfa_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text_2 = text.get("1.0", "end")[:-1]
    res = ""  
    for x in range( len( text_2)):
        if text_2[x] in alfa:
            num = alfa.index(text_2[x])
            res += alfa[num-1]
        elif text_2[x] in alfa_eng:
            num = alfa_eng.index(text_2[x])
            res += alfa_eng[num-1]
        else:
            res += str(text_2[x])

    result.configure(state = "normal")
    result.delete(1.0, "end")
    result.insert(1.0, res)
    result.configure(state="disabled")

#Перестановка
def SH_():
    text_2 = text.get("1.0", "end")
    res_1 = ""
    res_2 = ""
    for i in range(len(text_2)):
        if i%2:
            res_1 += text_2[i]
            continue
        res_2 += text_2[i]
    
    res = res_1 + res_2
    
    result.configure(state = "normal")
    result.delete(1.0, "end")
    result.insert(1.0, res)
    result.configure(state="disabled")
    
def Transpose_():
    text_2 = text.get(1.0, "end")
    res = []
    for i in range(len(text_2)//3):
        stack = []
        for j in range(3):
            stack.append(text_2[j + i*3])
        res.append(stack)
    
    res = list(zip(*res))
    t = ""
    leng = math.ceil(len(text_2)/3)
    for i in range(leng):
        t += "".join(res[i])

    result.configure(state = "normal")
    result.delete(1.0, "end")
    result.insert(1.0, t)
    result.configure(state="disabled")     

#Морзе лол
def Morse_():
    alfa = {'а': '.-','б': '-...','в': '.--','г': '--.','д': '-..','е': '.','ж': '...-','з': '--..','и': '..','й': '.---','к': '-.-','л': '.-..','м': '--','н': '-.','о': '---','п': '.--.','р': '.-.','с': '...','т': '-','у': '..-','ф': '..-.','х': '....','ц': '-.-.','ч': '---.','ш': '----','щ': '--.-','ъ': '.--.-.','ы': '-.--','ь': '-..-','э': '..-..','ю': '..--','я': '.-.-', 'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--', ' ' : '/'
}   
    text_2 = text.get("1.0", "end")[:-1]
    text_2 = text_2.lower()
    res = ""
    for x in text_2:
        res += alfa.get(x,x)
    
    result.configure(state = "normal")
    result.delete(1.0, "end")
    result.insert(1.0, res)
    result.configure(state="disabled")
    
def HEX_():
    text_2 = text.get(1.0, "end")
    res = ""
    for i in text_2:
        res += str(hex(ord(i)))[2:] + "."
    
    result.configure(state = "normal")
    result.delete(1.0, "end")
    result.insert(1.0, res)
    result.configure(state="disabled")     
    
def Clear_():
    result.configure(state = "normal")
    result.delete(1.0, "end")
    text.delete(1.0, "end")
    result.configure(state="disabled")

win = tk.Tk()
win.iconbitmap("s.ico")
win.title("C.Machine")
win.minsize(475,185)
win.resizable(False, False)

text = tk.Text(height = 5, width = 50, font = "Arial 11")
text.grid(row = 0, column = 0, rowspan = 3 , columnspan = 2)

result = tk.Text(height=5, width = 44, bg="#DFDFDF", font = "Arial 12")
result.insert(1.0, "Результат")
result.configure(state = "disabled", relief = "flat")
result.grid(row = 3, column = 0, rowspan = 3, columnspan = 2)

Ave = tk.Button(text = "Аве-1", command = Ave_)
Ave.grid(row = 0, column = 3, sticky="NSEW")

SH = tk.Button(text = "Штакетник", command = SH_)
SH.grid(row = 1, column = 3, sticky="NSEW")

Transpose = tk.Button(text = "Матрица", command = Transpose_)
Transpose.grid(row = 2, column = 3, sticky="NSEW")

Binary = tk.Button(text = "16 с/с", command = HEX_)
Binary.grid(row = 3, column = 3, sticky="NSEW")

Morse = tk.Button(text = "Код Морзе", command = Morse_)
Morse.grid(row = 4, column = 3, sticky="NSEW")

Clear = tk.Button(text = "ОЧИСТИТЬ", command = Clear_)
Clear.grid(row = 5, column = 3, sticky="NSEW")

win.mainloop()
