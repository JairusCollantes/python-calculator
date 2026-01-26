
import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

expression = "" 

def click_handler(event):
    global expression
    button = event.widget
    value = button.cget("text")

    if value == "C":
        expression = ""
        label.config(text="0")
    elif value == "=":
        try:
            safe_expression = expression.replace("x", "*")
            result = str(round(eval(safe_expression), 5))
            label.config(text=result)
            expression = result 
        except Exception:
            label.config(text="Error")
            expression = ""
    else:
        expression += value
        label.config(text=expression)


main = tk.Tk()
main.title("Calculator")
main.config(bg="#FFB6D9")
main.geometry("311x342")
main.resizable(False, False)



style = ttk.Style(main)
style.theme_use("clam")
style.configure("button.TButton", background="#9B4F74", foreground="#000", font=("", 16))
style.map("button.TButton", background=[("active", "#9B4F74")], foreground=[("active", "#000")])
style.configure("label.TLabel", background="#FFB6D9", foreground="#000", font=("TkDefaultFont", 30), anchor="e")

buttons_data = [
    ("7", 27, 111), ("8", 83, 111), ("9", 140, 111), ("+", 196, 111), ("C", 252, 111),
    ("4", 27, 167), ("5", 83, 167), ("6", 140, 167), ("-", 196, 167),
    ("1", 27, 223), ("2", 83, 223), ("3", 140, 223), ("/", 196, 223),
    (".", 27, 279), ("0", 83, 279), ("=", 140, 279), ("x", 196, 279),
]

for text, x, y in buttons_data:
    btn = ttk.Button(master=main, text=text, style="button.TButton")
    btn.bind("<Button-1>", click_handler)
    btn.place(x=x, y=y, width=45, height=39)

label = ttk.Label(master=main, text="0", style="label.TLabel")
label.place(x=27, y=27, width=223, height=54)

main.mainloop()