import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def hex2rgb(colorcode: str):
    code = colorcode.lstrip('#')
    return tuple(int(code[i:i+2], 16)/256 for i in range(0, 6, 2))

class Superhero(tk.Frame):
    ''' Bootstrap Superhero Theme '''
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        style = ttk.Style()
        # style.theme_use('classic')
        style.theme_use('clam')
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
        h1_font = 'Arial', 32
        h2_font = 'Arial', 24
        h3_font = 'Arial', 16
        body_font = 'Arial', 8
        style.configure('c.TFrame', background=bg)
        style.configure('c.TLabel', background=bg, foreground=fg)
        style.configure('c.TCheckbutton', background=bg, foreground=fg)
        style.configure('p.TButton', borderwidth=0, background=primary, foreground=fg)
        style.configure('s.TButton', borderwidth=0, background=secondary, foreground=fg)
        style.configure('g.TButton', borderwidth=0, background=success, foreground=fg)
        style.configure('b.TButton', borderwidth=0, background=info, foreground=fg)
        style.configure('y.TButton', borderwidth=0, background=warning, foreground=fg)
        style.configure('d.TButton', borderwidth=0, background=danger, foreground=fg)
        style.configure('c.TSeparator', background=bg)
        style.configure('Treeview.Heading', background=secondary, foreground=fg)
        style.configure('Treeview', background=dark, foreground=fg)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.protocol('WM_DELETE_WINDOW', self._destroyWindow)
        self.master.title('super hello theme')
        self.master.geometry('+30+30')
        self.master.resizable(width=False, height=False)
        self.master.attributes('-alpha', 0.98)
        self.frame = ttk.Frame(master, width=200, height=200, style='c.TFrame')
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.heading()
        separator = ttk.Separator(self.frame, orient='horizontal', style='c.TSeparator')
        separator.pack(fill=tk.BOTH, padx=16)
        self.buttons()
        self.tree()
        self.plot()

    def heading(self):
        frame1 = ttk.Frame(self.frame, style='c.TFrame')
        frame1.pack(expand=True, fill=tk.X, anchor=tk.N, padx=16, pady=16)
        h1_font = 'Arial', 32
        h2_font = 'Arial', 24
        h3_font = 'Arial', 16
        label = ttk.Label(frame1, text='Superhero', style='c.TLabel', font=h1_font)
        label.pack(anchor=tk.W)
        label = ttk.Label(frame1, text='The breve and the blue', style='c.TLabel', font=h3_font)
        label.pack(anchor=tk.W)

    def buttons(self):
        frame2 = ttk.Frame(self.frame, style='c.TFrame')
        frame2.pack(expand=True, fill=tk.BOTH, padx=16)
        ttk.Frame(frame2, height=16, style='c.TFrame').pack()
        btn = ttk.Button(frame2, text='Primary', style='p.TButton')
        btn.pack(side=tk.LEFT, anchor=tk.N, padx=2, pady=8)
        btn = ttk.Button(frame2, text='Secondary', style='s.TButton')
        btn.pack(side=tk.LEFT, anchor=tk.N, padx=2, pady=8)
        btn = ttk.Button(frame2, text='Success', style='g.TButton')
        btn.pack(side=tk.LEFT, anchor=tk.N, padx=2, pady=8)
        btn = ttk.Button(frame2, text='Info', style='b.TButton')
        btn.pack(side=tk.LEFT, anchor=tk.N, padx=2, pady=8)
        btn = ttk.Button(frame2, text='Warning', style='y.TButton')
        btn.pack(side=tk.LEFT, anchor=tk.N, padx=2, pady=8)
        btn = ttk.Button(frame2, text='danger', style='d.TButton')
        btn.pack(side=tk.LEFT, anchor=tk.N, padx=2, pady=8)

    def tree(self):
        frame3 = ttk.Frame(self.frame, style='c.TFrame')
        frame3.pack(expand=True, fill=tk.BOTH, padx=16, pady=16)
        label = ttk.Label(frame3, text='Table', style='c.TLabel', font=('Arial', 16))
        label.pack(anchor=tk.W, pady=8)

        df_ = pd.read_csv('iris.csv')
        # df = df_.drop(columns=['class']).iloc[:3, :]
        df = df_.iloc[:3, :]
        tree = ttk.Treeview(frame3, height=len(df))
        tree["column"] = list(range(len(df.columns)))
        tree["show"] = "headings"
        cols = []
        for col in df.columns:
            cols.append((col, 98))

        for i, (name, width) in enumerate(cols):
            tree.heading(i, text=name)
            anchor = tk.E if i < 4 else tk.CENTER
            tree.column(i, width=width, anchor=anchor)

        for i in df.index:
            values = [df[col][i] for col in df.columns]
            tree.insert("", "end", values=values)

        tree.pack(anchor=tk.W)

    def plot(self):
        frame4 = ttk.Frame(self.frame, style='c.TFrame')
        frame4.pack(expand=True, fill=tk.BOTH)
        label = ttk.Label(frame4, text='Plot', style='c.TLabel', font=('Arial', 16))
        label.pack(anchor=tk.W, padx=16)

        bg = hex2rgb('#0f2537')
        fg = hex2rgb('#ebebeb')
        primary = hex2rgb('#df6919')
        secondary = hex2rgb('#4e5d6c')
        success = hex2rgb('#5cb85c')
        info = hex2rgb('#5bc0de')
        warning = hex2rgb('#ffc107')
        danger = hex2rgb('#d9534f')
        light = hex2rgb('#abb6c2')
        dark = hex2rgb('#20374c')

        iris = pd.read_csv('iris.csv')
        sepal_length = iris['sepal-length']
        sepal_width = iris['sepal-width']
        target = iris['class']

        fig, ax = plt.subplots(figsize=(5, 4))
        fig.set_facecolor(dark)
        ax.set_facecolor(secondary)
        ax.scatter(sepal_length[target=='Iris-setosa'], sepal_width[target=='Iris-setosa'], label='Setosa', color=primary, marker='o')
        ax.scatter(sepal_length[target=='Iris-versicolor'], sepal_width[target=='Iris-versicolor'], label='Versicolor', color=success, marker='x')
        ax.scatter(sepal_length[target=='Iris-virginica'], sepal_width[target=='Iris-virginica'], label='Virginica', color=danger, marker='^')

        ax.set_title('Sepal Length vs Sepal Width', color=fg)
        ax.set_xlabel('Sepal Length', color=fg)
        ax.set_ylabel('Sepal Width', color=fg)
        plt.gca().tick_params(axis='x', colors=fg)
        plt.gca().tick_params(axis='y', colors=fg)
        plt.legend(facecolor=secondary)
        
        canvas = FigureCanvasTkAgg(fig, master=frame4)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH, padx=16, pady=8)

        ttk.Frame(frame4, height=8, style='c.TFrame').pack()

    def _destroyWindow(self):
        self.master.quit()
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    Superhero(root)
    app = App(master=root)
    app.mainloop()