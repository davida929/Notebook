from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class TextEditor(Tk):

    def __init__(self):
        super().__init__()
        self.title("Text Editor")
        self.geometry('560x480')

        # adding some widget
        self.textarea = Text(self, borderwidth=0)
        self.menubar = Menu(self)

        # addign menu items
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(label="Fichier", menu=self.file)

        self.file.add_command(label="Ouvrir",command= self.open_file)
        self.file.add_command(label="Enregistrer",command= self.save)

        self.menubar.add_command(label="About",command= self.about)
        self.menubar.add_command(label="Quiter",command= self.quit)

        # packing
        self.textarea.pack(expand=True, fill='both', padx=5, pady=5)
        self.config(menu=self.menubar)

    def save(self):
        content = self.textarea.get('1.0', "end-1c")
        savedirectory = filedialog.asksaveasfilename(
            filetypes=(
                ("Text File", '*.txt'),
                ("Python File", '*.py'),
                ("All Files", '*.*')
            )
        )
        if not savedirectory:
            return None
        with open(savedirectory, 'w', encoding='utf-8') as fl:
            fl.write(content)
        print(savedirectory)

    def open_file(self):
        content = filedialog.askopenfilename(
            filetypes=(
                ("Text File", '*txt'),
                ("Python File", "*.py"),
                ("All File", '*.*'),
            )
        )
        if not content:
            return None
        with open(content, 'r', encoding='utf-8') as ct:
            self.textarea.delete('1.0', END)
            self.textarea.insert('1.0', ct.read())

    def about(self):
        messagebox.showinfo("About", "Text-Editor App \nVersion 2.0.0")




if __name__ == '__main__':
    t = TextEditor()
    t.mainloop()