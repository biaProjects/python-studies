from tkinter import Tk, Label, PhotoImage
# photoimage é uma classe que só aceita gif

root = Tk()

photo = PhotoImage(file='4 - Part-4/d - gui-univesp/computer.gif').subsample(5)
# subsample -> para diminuir o tamanho da imagem, para encaixar na janela

hello = Label(master=root, image=photo, width=300, height=180)
hello.pack()
root.mainloop()