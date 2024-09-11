import os


from modules.CONST import CONST
from modules.MyLog import MyLog


from modules.FileRootDirReader import FileRootDirReader
from modules.FileCurrentWriter import FileCurrentWriter


def CheckFileCurrent():
    root_dir = FileRootDirReader()

    check = os.path.exists(os.path.join(root_dir, CONST.CURRENT_FILE))
    MyLog.info(f"CheckFileCurrent: check\nCheckFileCurrent: {check}")
    if not check:
        current_index = 0
        MyLog.info(f"CheckFileCurrent: current_index\nCheckFileCurrent: {current_index}")
        FileCurrentWriter(current_index)
