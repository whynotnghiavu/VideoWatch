

from modules.CONST import CONST
from modules.MyLog import MyLog


def FileRootDirWriter(root_dir):
    MyLog.info(f"FileRootDirWriter: root_dir\nFileRootDirWriter: {root_dir}")
    MyLog.info(f"FileRootDirWriter: File lưu root_dir\nFileRootDirWriter: {CONST.ROOT_DIR_FILE}")
    with open(CONST.ROOT_DIR_FILE, "w", encoding="utf-8") as root_dir_file:
        root_dir_file.write(f"{root_dir}")
