import os


from modules.CONST import CONST
from modules.MyLog import MyLog


from modules.FileRootDirReader import FileRootDirReader


def CreateFolderVideoWatch():
    root_dir = FileRootDirReader()

    MyLog.info(f"TaoVideoWatchFolder: Tạo folder VideoWatch\nTaoVideoWatchFolder: {os.path.join(root_dir, CONST.VIDEO_WATCH)}")
    if not os.path.exists(os.path.join(root_dir, CONST.VIDEO_WATCH)):
        os.makedirs(os.path.join(root_dir, CONST.VIDEO_WATCH), exist_ok=True)
