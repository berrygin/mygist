import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("Matplotlib Scatter Plot in Tkinter")

# Frameを作成して配置
frame = tk.Frame(root)
frame.pack()

# Matplotlibのフィギュアを作成
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
ax.scatter(x, y, color='red')  # 散布図を追加

# MatplotlibのフィギュアをTkinterのCanvasに埋め込む
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Tkinterウィンドウを表示
root.mainloop()

