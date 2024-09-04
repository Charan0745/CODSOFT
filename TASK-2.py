# Calculator :
import tkinter as tk
import math

new_calculation = True

def button_click(event):
    global new_calculation
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            new_calculation = True  
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)
        new_calculation = True  

    elif text == "√":
        expression = entry.get()
        try:
            result = math.sqrt(float(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            new_calculation = True  
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    else:
        if new_calculation:
            entry.delete(0, tk.END)
            new_calculation = False 
        entry.insert(tk.END, text)


window = tk.Tk()
window.title("Simple Calculator")
entry = tk.Entry(window, font=("Arial Bold", 24), justify="center")
entry.grid(row=0, column=0, columnspan=4)

button_labels = [
    'C', '√', '(', ')',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
buttons = []
for label in button_labels:
    button = tk.Button(window, text=label, padx=20, pady=20, font=("Helvetica", 18))
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)
    buttons.append(button)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
