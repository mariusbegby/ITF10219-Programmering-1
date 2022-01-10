# Importerer tkinter og todo_module som inneholder funksjonene mine
from tkinter import *
import todo_module as td

# Oppretter vinduet, setter størrelse, tittel og bakgrunn.
window = Tk()
window.geometry('430x530')
window.title("To-Do List")
window.config(bg="#add3f7")
window.resizable(height=False, width=False)

# Lager listbox som vil inneholde to do items
listbox = Listbox(width=50, height=20)
listbox.grid(row=0, column=0, pady=10, columnspan=4)

# Oppretter entry field som brukes til å legge til nye items i listen
todo = Entry(width=50)
todo.grid(row=1, column=0, columnspan=4, pady=20)

# Oppretter entry field som brukes til å skrive inn filnavn for lagring/åpning
filename_field = Entry(width=30)
filename_field.grid(row=3, column=0, columnspan=2)

# Oppretter en label som inneholder status etter utførte operasjoner og evt. feil som dukker opp
statusLabel = Label(text="STATUS")
statusLabel.grid(row=4, columnspan=4, sticky="ew", pady=20)

# Oppretter knapper, og knytter de til funksjonalitet med command=
add_button = Button(text="Add item", command=lambda: td.addItem(listbox, todo, statusLabel))
delete_button = Button(text="Delete item", command=lambda: td.deleteItem(listbox, statusLabel))
check_button = Button(text="Check item", command=lambda: td.checkItem(listbox, statusLabel))
uncheck_button = Button(text="Uncheck item", command= lambda: td.unCheckItem(listbox, statusLabel))
open_button = Button(text="Open from file", command= lambda: td.openFromFile(filename_field, listbox, statusLabel))
save_button = Button(text="Save to file", command= lambda: td.saveToFile(filename_field, listbox, statusLabel))

# Setter opp knappene i grid layout
add_button.grid(row=2, column=0, padx=20)
delete_button.grid(row=2, column=1, padx=15, pady=10)
check_button.grid(row=2, column=2, padx=15, pady=10)
uncheck_button.grid(row=2, column=3, padx=20)
open_button.grid(row=3, column=2, padx=15)
save_button.grid(row=3, column=3, padx=15)

# Kjører vinduet
window.mainloop()
