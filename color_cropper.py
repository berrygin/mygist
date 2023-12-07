import numpy as np
from PIL import Image, ImageGrab, ImageTk
import tkinter as tk
import tkinter.ttk as ttk

# token: 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

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True, fill=tk.BOTH)
        self.master.title('color cropper')
        self.master.geometry('680x680+680+96')

        self.screenshot = None
        self.image_id = 0
        self.rect_id = 0
        self.rect = 0., 0., 0., 0.
        self.var = tk.StringVar(value='')

        frame = tk.Frame(self)
        frame.pack(expand=True, fill=tk.BOTH)

        frame1 = tk.Frame(frame)
        frame1.pack(expand=True, fill=tk.X, padx=8, pady=8)
        button_paste = tk.Button(frame1, text='paste', width=4, command=self.paste())
        button_paste.pack(side=tk.LEFT, padx=4)
        button_crop = tk.Button(frame1, text='crop', width=4, command=self.crop())
        button_crop.pack(side=tk.LEFT, padx=4)

        label = tk.Label(frame1, textvariable=self.var, fg='#000')
        label.pack(side=tk.LEFT, padx=8)

        separator = ttk.Separator(frame, orient='horizontal')
        separator.pack(fill='x', padx=8)

        frame2 = tk.Frame(frame)
        frame2.pack(expand=True, fill=tk.BOTH)
        self.canvas = tk.Canvas(frame2, height=680-80)
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=8, pady=8)

    def mouse_event(self):

        def on_press(event):
            global start_x, start_y
            start_x = event.x
            start_y = event.y

        def on_drag(event):
            global start_x, start_y
            self.canvas.coords(self.rect_id, start_x, start_y, event.x, event.y)

        def release(event):
            global start_x, start_y
            self.rect = start_x, start_y, event.x, event.y

        start_x = None
        start_y = None
        self.canvas.bind('<ButtonPress-1>', on_press)
        self.canvas.bind('<B1-Motion>', on_drag)
        self.canvas.bind('<ButtonRelease-1>', release)
        self.rect_id = self.canvas.create_rectangle(0, 0, 0, 0, outline='hotpink', dash=(2, 4))

    def paste(self):
        def func():
            global photoimage
            self.screenshot = ImageGrab.grab()
            crop_ = self.screenshot.crop((0, 0, 664, 664))
            photoimage = ImageTk.PhotoImage(crop_)
            self.image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=photoimage)
            self.mouse_event()
        return func

    def crop(self):
        def func():
            global photoimage
            global crop_
            crop_ = self.screenshot.crop(self.rect)
            photoimage = ImageTk.PhotoImage(crop_)
            self.canvas.delete(self.image_id)
            self.canvas.delete(self.rect_id)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photoimage)
            arr = np.array(crop_)
            r = int(arr[:,:,0].mean())
            g = int(arr[:,:,1].mean())
            b = int(arr[:,:,2].mean())
            rgb = f'(RGB: {r} {g} {b})'
            hex_ = '#' + format(r, '02x') + format(g, '02x') + format(b, '02x')
            self.var.set(f'{hex_} has been added to the clipboard. ' + rgb)
            self.master.clipboard_clear()
            self.master.clipboard_append(hex_)
            print('HEX ->', hex_)
        return func


if __name__ == '__main__':
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()

