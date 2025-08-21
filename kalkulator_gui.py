import tkinter as tk

def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Setup jendela
root = tk.Tk()
root.title("Kalkulator Warna")
root.configure(bg="#2c2f33")  # warna background (dark gray)

# Entry untuk input
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5, relief="ridge", bg="#23272a", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Tombol kalkulator dengan warna
buttons = [
    ("7", "#99aab5"), ("8", "#99aab5"), ("9", "#99aab5"), ("/", "#7289da"),
    ("4", "#99aab5"), ("5", "#99aab5"), ("6", "#99aab5"), ("*", "#7289da"),
    ("1", "#99aab5"), ("2", "#99aab5"), ("3", "#99aab5"), ("-", "#7289da"),
    ("0", "#99aab5"), ("C", "#f04747"), ("=", "#43b581"), ("+", "#7289da"),
]

row, col = 1, 0
for (text, color) in buttons:
    b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16, "bold"),
                  bg=color, fg="white", activebackground="#99aab5",
                  command=lambda t=text: click(t))
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
