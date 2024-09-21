from modules.MyExecute import MyExecute
from modules.FileRootDirReader import FileRootDirReader


def MoThuMuc():
    root_dir = FileRootDirReader()
    # MyExecute(f" code {root_dir}")
    MyExecute(f" start {root_dir}")
