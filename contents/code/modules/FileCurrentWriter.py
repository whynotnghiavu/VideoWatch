import os


from modules.CONST import CONST
from modules.MyLog import MyLog


from modules.FileRootDirReader import FileRootDirReader


def FileCurrentWriter(current_index):
    root_dir = FileRootDirReader()

    MyLog.info(f"FileCurrentWriter: current_index\nFileCurrentWriter: {current_index}")

    with open(os.path.join(root_dir, CONST.CURRENT_FILE), "w", encoding="utf-8") as current_file:
        current_file.write(f"{current_index}")
