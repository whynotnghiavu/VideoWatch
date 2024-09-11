import os


from modules.CONST import CONST
from modules.MyLog import MyLog


from modules.FileRootDirReader import FileRootDirReader


def FileCurrentReader():
    root_dir = FileRootDirReader()

    with open(os.path.join(root_dir, CONST.CURRENT_FILE), "r", encoding="utf-8") as current_file:
        current_index = current_file.read()

    MyLog.info(f"FileCurrentRead: current_index\nFileCurrentRead: {current_index}")
    return int(current_index)
