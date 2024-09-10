from tkinter import messagebox


from view.UseCase import UseCase
from modules.MyLog import MyLog


from modules.XoaManHinh import XoaManHinh


def ButtonClick(chuc_nang):
    MyLog.title(f"Bắt đầu chức năng: {chuc_nang}")
    Router(chuc_nang)
    MyLog.title(f"Kết thúc chức năng: {chuc_nang}")


def Router(chuc_nang):
    if chuc_nang == "":
        MyLog.error(chuc_nang)
        MyLog.error(UseCase.error)
        messagebox.showerror("Thông báo", UseCase.error)

    # NOTE: Chỉnh chức năng trong vùng này

    elif chuc_nang == UseCase.XoaManHinh:
        XoaManHinh()

    # ChonThuMuc     

    # MoVideo     
    # MoGhiChu     

    # XemVideoTruoc     
    # XemVideoSau     

    # MoTatCaGhiChu     

    # ! Chỉ chỉnh các chức năng trong vùng này

    elif chuc_nang == UseCase.ThoatChuongTrinh:
        exit()
    else:
        MyLog.error(chuc_nang)
        MyLog.error(UseCase.error)
        messagebox.showerror("Thông báo", UseCase.error)
