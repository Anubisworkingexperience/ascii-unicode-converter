from tkinter import *
from tkinter.filedialog import asksaveasfile
from datetime import datetime
from unidecode import unidecode
 
root = Tk()
root.title("ascii-unicode-converter")    
root.geometry("750x750")
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
 
label = Label(text="Конвертер ascii в unicode", font=('Arial', 32)) 
label.pack()

titleLabel1 = Label(text='ascii', font=('Arial', 16))
titleLabel1.pack()

arrowLabel = Label(text='⇄', font=('Arial', 24), cursor='exchange')
arrowLabel.pack()

def exchangeLabelTexts(self):
    if titleLabel1['text'] == 'ascii':
        titleLabel1.config(text='unicode')
        titleLabel2.config(text='ascii')
    else:
        titleLabel1.config(text='ascii')
        titleLabel2.config(text='unicode')

arrowLabel.bind('<Button-1>', exchangeLabelTexts)

titleLabel2 = Label(text='unicode', font=('Arial', 16))
titleLabel2.pack()

textField = Text(wrap='char', height=10)
textField.pack()

output = Text(wrap='char', height=10, background='#e1e6e2', state='disabled')
output.pack()

convertButton = Label(text='Конвертировать', font=('Arial', 16), background='#5d4fe0', foreground='#ffffff',padx=10, pady=10)
convertButton.pack()

def saveToFile():
    print('saving file...')
    now = datetime.now()
    print(now)
    outputText = output.get('1.0', 'end').strip()
    print(outputText)
    outputEncoding = convertEncodings(self=saveToFile)
    print(outputEncoding)
    if outputEncoding == 'ascii':
        file = open(f'./files/{now}', 'w', encoding='utf-8')
    else:
        file = open(f'./files/{now}', 'w', encoding='ascii')
    file.write(outputText)

def textFromFile():
    print('текст из файла')

mainMenu = Menu()
mainMenu.add_command(label='Сохранить в файл', command= saveToFile)
mainMenu.add_command(label='Текст из файла', command=textFromFile)

def convertEncodings(self):
    if titleLabel1['text'] == 'ascii':
        outputEncoding = 'unicode'
        asciiString = textField.get('1.0', 'end').strip()
        print(asciiString)
        unicodeString = asciiString.encode('utf-8')
        print(unicodeString)
        output.config(state=NORMAL)
        output.delete('1.0', END)
        output.insert('1.0', unicodeString)
        output.config(state=DISABLED)
    else:
        unicodeString = textField.get('1.0', 'end').strip()
        outputEncoding = 'ascii'
        print(unicodeString)
        asciiString = unidecode(unicodeString)
        print(asciiString)
        output.config(state=NORMAL)
        output.delete('1.0', END)
        output.insert('1.0', asciiString)
        output.config(state=DISABLED)
    return outputEncoding

convertButton.bind('<Button-1>', convertEncodings)

root.config(menu=mainMenu)
root.mainloop()