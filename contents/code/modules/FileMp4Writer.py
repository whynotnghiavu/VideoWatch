import os


from modules.CONST import CONST
from modules.MyLog import MyLog
from modules.MyFile import MyFile


from modules.FileRootDirReader import FileRootDirReader


def FileMp4Writer():
    root_dir = FileRootDirReader()

    mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
    with open(os.path.join(root_dir, CONST.ALL_FILE_MP4), "w", encoding="utf-8") as all_file_mp4:
        for mp4_file in mp4_files:
            all_file_mp4.write(f"{mp4_file}\n")

    MyLog.info(f"FileMp4Writer: Ghi tất cả các file {CONST.MP4}\nFileMp4Writer: {os.path.join(root_dir, CONST.ALL_FILE_MP4)}")
