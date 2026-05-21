from tkinter import Tk, Label

# label permite que adicione texto em janela gráfica

root = Tk()
hello = Label(master = root, text='Hello world')
# master indica a jannela onde o texto será inserido, text declara o texto

hello.pack()
# pack fará o empacotamento dos componentes na janela que será criada

root.mainloop()