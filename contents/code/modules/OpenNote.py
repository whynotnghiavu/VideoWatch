import os


from modules.CONST import CONST
from modules.MyLog import MyLog


from modules.MyNewPath import MyNewPath
from modules.MyExecute import MyExecute
from modules.GetCurrentVideo import GetCurrentVideo
from modules.RemoveRootDirPath import RemoveRootDirPath


def OpenNote(mp4_file_path=""):
    if mp4_file_path == "":
        mp4_file_path = GetCurrentVideo()

    note_file_path = MyNewPath(mp4_file_path, CONST.MP4, CONST.NOTE)
    MyLog.info(f"OpenNote: note_file_path\nOpenNote: {note_file_path}")

    if not os.path.exists(note_file_path):
        with open(note_file_path, 'w', encoding="utf-8") as file:
            file.write(f"<!--{RemoveRootDirPath(note_file_path)}-->\n\n\n\n")

    # MyExecute(f" code")
    MyExecute(f" code {note_file_path}")
