from tkinter import *

windows = Tk()
windows.title("Widget Examples")
windows.minsize(width=800, height=700)
windows.config(padx=20, pady=20) #ekranımız dış çizgi ile arasına 20 birimlik bir boşluk bırakır

#label
labels = Label(text="Hello World!",padx=20, pady=20)
labels.pack()
#button
def button_click():
    print("bastın")
    print(texts.get("1.4","2.4"))

button = Button(text="Click Me!", command=button_click)
button.pack()

#entry
entries = Entry() #oneline
entries.pack()

#text
texts = Text(height=2) #multiline
texts.focus()
texts.pack()

#scale
def scale_selected(value): #buton gibi basılan birşey olmadığından get ile olmaz
    print(value)
scales = Scale(from_=0, to=100,command=scale_selected)
scales.pack()

#spinbox
def spinbox_selected():
    print(spinboxs.get())
spinboxs = Spinbox(from_=0, to=100,command=spinbox_selected)
spinboxs.pack()

#checkbutton
def checkbutton_selected():
    print(checkstatus.get())
checkstatus =StringVar()
checkbuttons = Checkbutton(text="Hello World!",variable=checkstatus, command=checkbutton_selected)
checkbuttons.pack()

#radiobutton
def radio_selected():
    print(radiobutton_selected.get())

radiobutton_selected = IntVar()
radiobuttons = Radiobutton(text="pasta", value=1, variable=radiobutton_selected, command=radio_selected)
radiobuttons2 = Radiobutton(text="rice", value=2, variable=radiobutton_selected, command=radio_selected)

radiobuttons.pack()
radiobuttons2.pack()

#listbox
def listbox_selected(event):
    print(listboxs.get(listboxs.curselection()))
name_list = ("Mert", "Berke Can", "Burak", "Bekir")
listboxs = Listbox()
for i in range(len(name_list)):
    listboxs.insert(i , name_list[i])
listboxs.bind("<<ListboxSelect>>", listbox_selected)
listboxs.pack()


windows.mainloop()