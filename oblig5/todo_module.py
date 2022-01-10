# Importerer datetime for tidsfunksjonalitet, og tkinter
import datetime as dt
from tkinter import *

# Dette vil kunne brukes til å enkelt endre teksten i et entry field
def setEntry(entry, text):
    entry.delete('0', 'end')
    entry.insert('0', text)
    return entry

# Brukes for å skaffe nåværende tid i ønsket format
def getDateTime():
    return dt.datetime.now().strftime('%Y-%m-%d %H:%M')

# Brukes for å legge til nytt item i todo list, setter så entry field til blank
def addItem(listbox, entry, statusLabel):
    item = getDateTime() + ": " + entry.get()
    listbox.insert("end", item)
    setEntry(entry, "")
    statusLabel.config(text=f"Added new item: {item}")

# Brukes til å slette det selected elementet i listbox
def deleteItem(listbox, statusLabel):
    item = listbox.get(listbox.curselection()[0])
    listbox.delete(listbox.curselection())
    statusLabel.config(text=f"Deleted item: {item}")

# Brukes til å endre bakgrunnsfargen for et element, da blir det markert som "utført"
def checkItem(listbox, statusLabel):
    listbox.itemconfig(listbox.curselection(), bg="#8cd177")
    item = listbox.get(listbox.curselection()[0])
    statusLabel.config(text=f"Completed item: {item}")

# Endrer bakgrunnsfarget tilbake til hvit
def unCheckItem(listbox, statusLabel):
    listbox.itemconfig(listbox.curselection(), bg="#ffffff")
    item = listbox.get(listbox.curselection()[0])
    statusLabel.config(text=f"Unchecked item: {item}")

# Lagrer listbox til en fil med filnavnet i filename_field
def saveToFile(filename_field, listbox, statusLabel):
    file = open(filename_field.get(), "w")
    listbox_text = ""
    for i in range(0, listbox.size()):
        listbox_text += f"{listbox.get(i)}\n"
    file.write(listbox_text)
    file.close()
    statusLabel.config(text=f"Saved To Do list to file {filename_field.get()}")

# Åpner informasjon fra en fil, og tømmer listbox, så setter inn hver linje fra filen til listbox
def openFromFile(filename_field, listbox, statusLabel):
    try:
        file = open(filename_field.get(), "r")
        lines = file.readlines()
        listbox.delete(0, END)
        for line in lines:
            content = line.rstrip()
            listbox.insert("end", content)
        statusLabel.config(text=f"Opened To Do list from file {filename_field.get()}")
    except FileNotFoundError:
        statusLabel.config(text="File not found, try again.")
    except:
        statusLabel.config(text="Unknown issue occured. Try again.")
