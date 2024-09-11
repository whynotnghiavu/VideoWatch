

from modules.CONST import CONST


def FileRootDirReader():
    with open(CONST.ROOT_DIR_FILE, "r", encoding="utf-8") as root_dir_file:
        root_dir = root_dir_file.read()
        return root_dir
