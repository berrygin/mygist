import tkinter as tk
import tkinter.ttk as ttk


class myStyle(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        style = ttk.Style()
        style.theme_use('classic')
        bg = '#333'
        fg = '#eff'
        style.configure('c.TFrame', background=bg)
        style.configure('c.TLabel', background=bg, foreground=fg)  # noqa
        style.configure('c.TCheckbutton', background=bg, foreground=fg)
        style.configure('c.TButton', borderwidth=0, background=bg, foreground=fg)  # noqa
        style.configure('c.TSeparator', background=bg)
        style.configure('Treeview.Heading', background=bg, foreground=fg)
        style.configure('Treeview', background=bg, foreground=fg)


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.master.title('hello')
        self.master.geometry('300x300+30+30')
        self.master.resizable(width=False, height=False)
        self.master.attributes('-alpha', 0.98)
        fm = ttk.Frame(master, width=200, height=200)
        fm.pack()
        lbl = ttk.Label(fm, text='spam', style='c.TLabel')
        lbl.pack()

if __name__ == '__main__':
    root = tk.Tk()
    _ = myStyle(root)
    app = App(master=root)
    app.mainloop()