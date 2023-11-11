from tkinter import *
 
root = Tk()
root.title("ascii-unicode-converter")    
root.geometry("750x750")
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
 
label = Label(text="Конвертер ascii в unicode", font=('Arial', 32)) 
label.pack()

titleLabel1 = Label(text='ascii', font=('Arial', 16))
titleLabel1.pack()

arrowLabel = Label(text='⇄', font=('Arial', 16), cursor='exchange')
arrowLabel.pack()

titleLabel2 = Label(text='unicode', font=('Arial', 16))
titleLabel2.pack()

textField = Text(wrap='char')
textField.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT)

border_color = Frame(root, background='white')

convertButton = Label(border_color, text='Конвертировать', font=('Arial', 16), background='#5d4fe0', foreground='#ffffff',padx=10, pady=10)
convertButton.pack()
border_color.pack()

mainMenu = Menu()
mainMenu.add_cascade(label='Сохранить')
mainMenu.add_cascade(label='Открыть')

root.config(menu=mainMenu)
root.mainloop()