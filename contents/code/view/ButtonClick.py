from tkinter import messagebox


from view.UseCase import UseCase
from modules.MyLog import MyLog


from modules.XoaManHinh import XoaManHinh


from modules.ChonThuMuc import ChonThuMuc
from modules.MoThuMuc import MoThuMuc
from modules.GhiThongTin import GhiThongTin

from modules.OpenVideo import OpenVideo
from modules.OpenNote import OpenNote
from modules.OpenVideoBack import OpenVideoBack
from modules.OpenVideoNext import OpenVideoNext
from modules.HopNhatFileNote import HopNhatFileNote
from modules.HopNhatFileSub import HopNhatFileSub


from modules.ThoatChuongTrinh import ThoatChuongTrinh


def ButtonClick(chuc_nang):
    MyLog.title(f"Bắt đầu chức năng: {chuc_nang}")
    Router(chuc_nang)
    MyLog.title(f"Kết thúc chức năng: {chuc_nang}")


def Router(chuc_nang):
    if chuc_nang == "":
        MyLog.error(chuc_nang)
        MyLog.error(UseCase.error)
        messagebox.showerror("Thông báo", UseCase.error)
    elif chuc_nang == UseCase.XoaManHinh:
        XoaManHinh()

    # NOTE: Chỉnh chức năng trong vùng này
    elif chuc_nang == UseCase.ChonThuMuc:
        ChonThuMuc()
        ThoatChuongTrinh()
    elif chuc_nang == UseCase.MoThuMuc:
        MoThuMuc()
        ThoatChuongTrinh()

    elif chuc_nang == UseCase.GhiThongTin:
        GhiThongTin()

    elif chuc_nang == UseCase.MoVideo:
        OpenVideo()
        ThoatChuongTrinh()

    elif chuc_nang == UseCase.MoGhiChu:
        OpenNote()
        ThoatChuongTrinh()

    elif chuc_nang == UseCase.XemVideoTruoc:
        OpenVideoBack()
        ThoatChuongTrinh()

    elif chuc_nang == UseCase.XemVideoSau:
        OpenVideoNext()
        ThoatChuongTrinh()

    elif chuc_nang == UseCase.HopNhatFileNote:
        HopNhatFileNote()
        ThoatChuongTrinh()

    elif chuc_nang == UseCase.HopNhatFileSub:
        HopNhatFileSub()
        ThoatChuongTrinh()

    # ! Chỉ chỉnh các chức năng trong vùng này

    elif chuc_nang == UseCase.ThoatChuongTrinh:
        ThoatChuongTrinh()
    else:
        MyLog.error(chuc_nang)
        MyLog.error(UseCase.error)
        messagebox.showerror("Thông báo", UseCase.error)
