from tkinter import filedialog


from modules.MyLog import MyLog


from modules.FileRootDirWriter import FileRootDirWriter
from modules.CreateFolderVideoWatch import CreateFolderVideoWatch
from modules.FileMp4Writer import FileMp4Writer
from modules.CheckFileCurrent import CheckFileCurrent
from modules.OpenVideo import OpenVideo


def ChonThuMuc():
    root_dir = filedialog.askdirectory(title="Chọn thư mục")

    if not root_dir:
        MyLog.error("ChonThuMuc: Chưa chọn thư mục")
        return

    MyLog.info(f"ChonThuMuc: Đã chọn: {root_dir}")
    MyLog.info(f"ChonThuMuc: root_dir\nChonThuMuc: {root_dir}")

    FileRootDirWriter(root_dir)

    CreateFolderVideoWatch()

    FileMp4Writer()

    CheckFileCurrent()

    OpenVideo()
