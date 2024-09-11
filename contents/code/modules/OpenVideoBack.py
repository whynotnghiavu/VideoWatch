

from modules.MyLog import MyLog


from modules.FileCurrentReader import FileCurrentReader
from modules.FileCurrentReader import FileCurrentReader
from modules.OpenVideo import OpenVideo
from modules.FileCurrentWriter import FileCurrentWriter


def OpenVideoBack():
    current_index = FileCurrentReader()
    current_index -= 1
    MyLog.info(f"OpenVideoBack: current_index\nOpenVideoBack: {current_index}")
    FileCurrentWriter(current_index)
    MyLog.info(f"OpenVideoBack: current_index\nOpenVideoBack: {current_index}")

    OpenVideo()
