import os
from tkinter import messagebox


from modules.CONST import CONST
from modules.MyLog import MyLog


from modules.FileRootDirReader import FileRootDirReader


def FileMp4Reader(index):
    if index < 0:
        messagebox.showerror("Thông báo", "Chỉ số video không hợp lệ")
        exit()

    root_dir = FileRootDirReader()

    with open(os.path.join(root_dir, CONST.ALL_FILE_MP4), "r", encoding="utf-8") as all_file_mp4:
        mp4_files = all_file_mp4.readlines()

    if index >= len(mp4_files):
        messagebox.showerror("Thông báo", "Chỉ số video không hợp lệ")
        exit()

    video = mp4_files[index]

    MyLog.info(f"FileMp4Reader: video\nFileMp4Reader: {video}")
    return video
