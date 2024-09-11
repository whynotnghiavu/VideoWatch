

from modules.MyLog import MyLog


from modules.FileCurrentReader import FileCurrentReader
from modules.OpenVideo import OpenVideo
from modules.FileCurrentWriter import FileCurrentWriter


def OpenVideoNext():
    current_index = FileCurrentReader()
    current_index += 1
    MyLog.info(f"OpenVideoNext: current_index\nOpenVideoNext: {current_index}")
    FileCurrentWriter(current_index)
    MyLog.info(f"OpenVideoNext: current_index\nOpenVideoNext: {current_index}")

    OpenVideo()
