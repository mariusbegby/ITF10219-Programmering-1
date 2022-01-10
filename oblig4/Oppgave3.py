import tkinter as tk

# Oppgave A
window1 = tk.Tk()
window1.title("Hello tkinter!")

window1.mainloop()

# Oppgave B
window2 = tk.Tk()
window2.title("GUI Elements")
label1 = tk.Label(text="Label 1").pack()
label2 = tk.Label(text="Label 2", background="red", foreground="white").pack()
label3 = tk.Label(text="Label 3", background="yellow", width=10, height=5).pack()
button1 = tk.Button(text="Button!", width=7, height=2).pack()
input1 = tk.Entry(width=15).pack()
textbox1 = tk.Text().pack()

window2.mainloop()