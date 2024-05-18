from tkinter import *

class TextEditor(Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Editor")
        self.geometry('560x480')
        self.textarea = Text(self)
        self.btn = Button(self, text="Enregistrer", command=self.save)

        self.textarea.pack(expand=True, fill='both')
        self.btn.pack()

    def save(self):
        print(self.textarea.get("1.0", "end-1c"))


if __name__ == '__main__':
    t = TextEditor()
    t.mainloop()