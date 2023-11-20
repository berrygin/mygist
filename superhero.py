import tkinter as tk
import tkinter.ttk as ttk


class Superhero(tk.Frame):
    ''' Bootstrap Superhero Theme '''
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        style = ttk.Style()
        style.theme_use('classic')
        bg = '#0f2537'
        fg = '#ebebeb'
        primary = '#df6919'
        secondary = '#4e5d6c'
        success = '#5cb85c'
        info = '#5bc0de'
        warning = '#ffc107'
        danger = '#d9534f'
        light = '#abb6c2'
        dark = '#20374c'
        bodyfont = ('Arial', 8, 'bold')
        style.configure('c.TFrame', background=bg)
        style.configure('c.TLabel', background=bg, foreground=fg)  # noqa
        style.configure('c.TCheckbutton', background=bg, foreground=fg)
        style.configure('c.TButton', borderwidth=0, background=secondary, foreground=fg, font=bodyfont)  # noqa
        style.configure('p.TButton', borderwidth=0, background=primary, foreground=fg, font=bodyfont)
        style.configure('c.TSeparator', background=bg)
        style.configure('Treeview.Heading', background=bg, foreground=fg)
        style.configure('Treeview', background=bg, foreground=fg)


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.master.title('super hello theme')
        self.master.geometry('300x300+30+30')
        self.master.resizable(width=False, height=False)
        self.master.attributes('-alpha', 0.98)
        frame = ttk.Frame(master, width=200, height=200, style='c.TFrame')
        frame.pack(expand=True, fill=tk.BOTH)

        title_font = ('Arial', 26)
        lbl = ttk.Label(frame, text='Superhero', style='c.TLabel', font=title_font)
        lbl.pack(anchor=tk.W, padx=16, pady=8)
        btn = ttk.Button(frame, text='Primary', style='p.TButton')
        btn.pack(side=tk.LEFT, anchor=tk.N, padx=4, pady=8)
        btn = ttk.Button(frame, text='Secondary', style='c.TButton')
        btn.pack(side=tk.LEFT, anchor=tk.N, padx=4, pady=8)

if __name__ == '__main__':
    root = tk.Tk()
    Superhero(root)
    app = App(master=root)
    app.mainloop()