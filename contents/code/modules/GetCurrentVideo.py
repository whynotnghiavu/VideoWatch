

from modules.MyLog import MyLog


from modules.FileCurrentReader import FileCurrentReader
from modules.FileMp4Reader import FileMp4Reader


def GetCurrentVideo():
    current_index = FileCurrentReader()
    current_video = FileMp4Reader(current_index)

    MyLog.info(f"GetCurrentVideo: current_video\nGetCurrentVideo: {current_video}")
    return current_video
