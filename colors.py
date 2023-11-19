import numpy as np
from PIL import Image, ImageGrab, ImageTk
import tkinter as tk
import tkinter.ttk as ttk

# token: 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
def tkimg_to_arr(photoimage):

    height = photoimage.height()
    width = photoimage.width()
    bitmap = []
    for y in range(height):
        pixels = []
        for x in range(width):
            pixel = list(photoimage.get(x, y))
            pixels.append(pixel)
        bitmap.append(pixels)

    # 作成したリストをNumPy配列に変換
    cv2_rgb_image = numpy.array(bitmap, dtype='uint8')

    # RGB -> BGRによりCV2画像オブジェクトに変換
    cv2_image = cv2.cvtColor(cv2_rgb_image, cv2.COLOR_RGB2BGR)

    return cv2_image


class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.photo = None
        self.photo_crop = None
        self.rect = 0., 0., 0., 0.

        self.master.geometry('680x680+100+100')

        frame = tk.Frame(self)
        frame.pack(expand=True, fill=tk.BOTH)
        frame1 = tk.Frame(frame)
        frame1.pack(expand=True, fill=tk.BOTH, padx=8, pady=8)
        btn_paste = tk.Button(frame1, text='paste', width=4, command=self.paste())
        btn_paste.pack(side=tk.LEFT)
        btn_crop = tk.Button(frame1, text='crop', width=4, command=self.crop_())
        btn_crop.pack(side=tk.LEFT)
        btn_calc = tk.Button(frame1, text='calc', width=4, command=lambda: print('calc'))
        btn_calc.pack(side=tk.LEFT)

        separator = ttk.Separator(frame, orient='horizontal')
        separator.pack(fill='x', padx=8)

        frame2 = tk.Frame(frame)
        frame2.pack(expand=True, fill=tk.BOTH)
        self.canvas = tk.Canvas(frame2, width=664, height=664)
        self.canvas.pack()

    def mouse_event(self):

        def on_press(event):
            global start_x, start_y
            start_x = event.x
            start_y = event.y

        def on_drag(event):
            global start_x, start_y
            self.rect = start_x, start_y, event.x, event.y
            print(self.rect)
            self.canvas.coords(rect, start_x, start_y, event.x, event.y)

        start_x = None
        start_y = None
        self.canvas.bind("<ButtonPress-1>", on_press)
        self.canvas.bind("<B1-Motion>", on_drag)
        rect = self.canvas.create_rectangle(0, 0, 0, 0, outline='hotpink', dash=(2, 4))

    def paste(self):
        def func():
            screenshot = ImageGrab.grab()
            crop_image = screenshot.crop((0, 0, 664, 664))
            self.photo = ImageTk.PhotoImage(crop_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.mouse_event()
        return func

    def crop_(self):
        def func():
            self.photo_crop = self.photo.crop(self.rect)
            print(self.photo_crop)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_crop)
        return func


if __name__ == '__main__':
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()

