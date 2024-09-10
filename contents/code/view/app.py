import tkinter as tk


from view.Button import Button
from view.ButtonClick import ButtonClick


def app():
    gui = tk.Tk()
    # Đặt vị trí ở bên phải màn hình
    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()
    # NOTE: Kích thước cửa sổ (400)
    x_pos = screen_width - 400
    y_pos = 0
    gui.geometry(f"{400}x{screen_height}+{x_pos}+{y_pos}")

    gui.configure(background="#282a36")
 

    # Thêm các nút chức năng
    for chuc_nang, theme in Button.button_themes.items():
        button = tk.Button(
            text=chuc_nang,
            background=theme[0],
            foreground=theme[1],
            # NOTE: Kích thước nút bấm (40)
            width=40,
            command=lambda i=chuc_nang: ButtonClick(i)
        )
        button.pack()

    gui.mainloop()
