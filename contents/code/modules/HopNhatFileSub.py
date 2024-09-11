import os


from modules.CONST import CONST
from modules.MyFile import MyFile


from modules.FileRootDirReader import FileRootDirReader
from modules.RemoveRootDirPath import RemoveRootDirPath
from modules.MyExecute import MyExecute


def HopNhatFileSub():
    root_dir = FileRootDirReader()
    srt_files = MyFile.TimKiem(root_dir, CONST.SRT)
    subs = []

    for srt_file in srt_files:
        with open(srt_file, "r", encoding="utf-8") as file:
            contents = file.read()
        subs.append(f"<!--{RemoveRootDirPath(srt_file)}-->\n\n\n\n")
        subs.append(contents)

    with open(os.path.join(root_dir, CONST.ALL_FILE_SUBS), "w", encoding="utf-8") as all_file_subs:
        for sub in subs:
            all_file_subs.write(f"{sub}\n")

    MyExecute(f" code")
    MyExecute(f" code {os.path.join(root_dir, CONST.ALL_FILE_SUBS)}")
