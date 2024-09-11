

from modules.CONST import CONST
from modules.MyLog import MyLog


def FileRootDirWriter(root_dir):
    MyLog.info(f"GhiFileRootDir: root_dir\nGhiFileRootDir: {root_dir}")
    MyLog.info(f"GhiFileRootDir: File lưu root_dir\nGhiFileRootDir: {CONST.ROOT_DIR_FILE}")
    with open(CONST.ROOT_DIR_FILE, "w", encoding="utf-8") as root_dir_file:
        root_dir_file.write(f"{root_dir}")
