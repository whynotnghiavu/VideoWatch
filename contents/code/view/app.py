import tkinter as tk


from view.Button import Button
from view.ButtonClick import ButtonClick


def app():
    # Tạo một cửa sổ Tkinter
    gui = tk.Tk()

    # Đặt vị trí ở bên phải màn hình
    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()
    # NOTE: Kích thước cửa sổ (150)
    x_pos = screen_width - 150
    y_pos = 0
    gui.geometry(f"{150}x{screen_height}+{x_pos}+{y_pos}")
    # gui.geometry(f"{150}x{277}+{x_pos}+{y_pos}")

    # Tạo màu nền cửa sổ
    gui.configure(background="#282a36")

    # Đặt tiêu đề cho cửa sổ
    gui.title("Video")

    # Làm cửa sổ trong suốt bằng cách sử dụng alpha (giá trị từ 0.0 đến 1.0)
    gui.attributes('-alpha', 0.8)  # 0.8 là mức trong suốt

    # Thêm các nút chức năng
    for chuc_nang, theme in Button.button_themes.items():
        button = tk.Button(
            text=chuc_nang,
            background=theme["background"],
            foreground=theme["foreground"],
            # NOTE: Kích thước nút bấm (15)
            width=15,
            command=lambda i=chuc_nang: ButtonClick(i)
        )
        button.pack()

    gui.mainloop()
