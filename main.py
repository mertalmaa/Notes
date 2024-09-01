import tkinter

window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=800, height=600)

#label
my_label = tkinter.Label(text="this is a text", font=("Arial", 25,"bold"))
my_label.config(bg="black",fg="white")
my_label.pack()

def entry_writer():
    print (my_entry.get()) #my_entry.get sadece yazıyı alır bunu yazdırmam lazım.

#button
button = tkinter.Button(text="this is a button",command=entry_writer,height=5,width=20)
button.pack()

#entry
my_entry = tkinter.Entry(width=20)
my_entry.pack()



window.mainloop()