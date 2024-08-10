from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label1 = Label(self.root, text='To-Do-List-App',
                           font='ariel, 25 bold', width=10, bd=5, bg='black', fg='white')
        self.label1.pack(side='top', fill=BOTH)
        
        self.label2 = Label(self.root, text='Add Task',
                           font='ariel, 18 bold', width=10, bd=5, bg='black', fg='white')
        self.label2.place(x=40 ,y=54)
        
        self.label3 = Label(self.root, text='Task',
                           font='ariel, 18 bold', width=10, bd=5, bg='black', fg='white')
        self.label3.place(x=320 ,y=54)
        
        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=200 ,y= 100)
        
        self.text = Text(self.root, bd=5 ,height=2, width=23, font='ariel, 10 bold')
        self.text.place(x=20, y=120)
        
        #=============add task============#
        def add():
            content = self.text.get(1.0, END).strip()  # Strip any trailing newline characters
            if content:  # Check if content is not empty
                self.main_text.insert(END, content)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0, END)     

        def delete():
            selected = self.main_text.curselection()
            if selected:
                task_to_delete = self.main_text.get(selected)
                self.main_text.delete(selected)
                with open('data.txt', 'r') as f:
                    lines = f.readlines()
                with open('data.txt', 'w') as f:
                    for line in lines:
                        if line.strip("\n") != task_to_delete:
                            f.write(line)

        with open('data.txt', 'r') as file:
            for line in file:
                self.main_text.insert(END, line.strip())

        self.button = Button(self.root, text='Add', font='sarif, 20 bold italic',
                             width=8, bd=5, bg='black', fg='white', command=add) 
        self.button.place(x=30, y=175)
        
        self.button2 = Button(self.root, text='Delete', font='sarif, 20 bold italic',
                             width=8, bd=5, bg='black', fg='white', command=delete) 
        self.button2.place(x=30, y=250) 

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
