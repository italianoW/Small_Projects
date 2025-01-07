##italianow

import tkinter as tk
from tkinter import ttk 

field_text = ""

def update_field_image():
    global field_text
    field.delete(1.0,"end")
    field.insert(1.0,str(field_text))

def add_text(textAdded):
    global field_text
    if field_text=="Error":
        field_text = ""
    field_text= field_text + str(textAdded)
    update_field_image()

def calculate():
    global field_text
    try:
        field_text = str(eval(field_text)) ## DANGEROUS, EVAL CAN EXECUTE **CODES**
    except Exception:
        field_text = "Error"

    update_field_image()

def clear_text():
    global field_text
    field_text = ""
    update_field_image()

def percentage_calculate():
    global field_text
    calculate()
    if field_text!="Error":
        field_text = str(float(field_text)/100)
    update_field_image()


window = tk.Tk()
window.title("Calculadora")
window.geometry("300x300")


field = tk.Text(window,width=16,height=2,font=("Arial",24))
field.grid(row=1,columnspan=5)

btn_1 = tk.Button(window, text="1", command= lambda:add_text("1"),width=5, font =("Arial",14))
btn_1.grid(row=2,column=1)

btn_2 = tk.Button(window, text="2", command= lambda:add_text("2"),width=5, font =("Arial",14))
btn_2.grid(row=2,column=2)

btn_3 = tk.Button(window, text="3", command= lambda:add_text("3"),width=5, font =("Arial",14))
btn_3.grid(row=2,column=3)

btn_4 = tk.Button(window, text="4", command= lambda:add_text("4"),width=5, font =("Arial",14))
btn_4.grid(row=3,column=1)

btn_5 = tk.Button(window, text="5", command= lambda:add_text("5"),width=5, font =("Arial",14))
btn_5.grid(row=3,column=2)

btn_6 = tk.Button(window, text="6", command= lambda:add_text("6"),width=5, font =("Arial",14))
btn_6.grid(row=3,column=3)

btn_7 = tk.Button(window, text="7", command= lambda:add_text("7"),width=5, font =("Arial",14))
btn_7.grid(row=4,column=1)

btn_8 = tk.Button(window, text="8", command= lambda:add_text("8"),width=5, font =("Arial",14))
btn_8.grid(row=4,column=2)

btn_9 = tk.Button(window, text="9", command= lambda:add_text("9"),width=5, font =("Arial",14))
btn_9.grid(row=4,column=3)

btn_0 = tk.Button(window, text="0", command= lambda:add_text("0"),width=5, font =("Arial",14))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(window, text="+", command= lambda:add_text("+"),width=5, font =("Arial",14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(window, text="-", command= lambda:add_text("-"),width=5, font =("Arial",14))
btn_minus.grid(row=3, column=4)

btn_lp = tk.Button(window, text="(", command= lambda:add_text("("),width=5, font =("Arial",14))
btn_lp.grid(row=5, column=1)

btn_rp = tk.Button(window, text=")", command= lambda:add_text(")"),width=5, font =("Arial",14))
btn_rp.grid(row=5, column=3)

btn_multiply = tk.Button(window, text="x", command= lambda:add_text("*"),width=5, font =("Arial",14))
btn_multiply.grid(row=4, column=4)

btn_divide = tk.Button(window, text="/", command= lambda:add_text("/"),width=5, font =("Arial",14))
btn_divide.grid(row=5, column=4)

btn_calculate = tk.Button(window, text="=", command= lambda:calculate(),width=5, font =("Arial",14))
btn_calculate.grid(row=6, column=4)

btn_clear = tk.Button(window, text="C", command= lambda:clear_text(),width=5, font =("Arial",14))
btn_clear.grid(row=6, column=1)

btn_point = tk.Button(window, text=".", command= lambda:add_text("."),width=5, font =("Arial",14))
btn_point.grid(row=6, column=2)

btn_percentage = tk.Button(window, text="%", command= lambda:percentage_calculate(),width=5, font =("Arial",14))
btn_percentage.grid(row=6, column=3)

window.mainloop()

##italianow
