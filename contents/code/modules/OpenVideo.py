

from modules.MyLog import MyLog


from modules.MyExecute import MyExecute
from modules.GetCurrentVideo import GetCurrentVideo
from modules.OpenNote import OpenNote


def OpenVideo(current_video=""):
    if current_video == "":
        current_video = GetCurrentVideo()

    MyLog.info(f"OpenVideo: current_video\nOpenVideo: {current_video}")

    OpenNote(current_video)

    MyExecute(f" start {current_video}")
