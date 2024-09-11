import os


from modules.CONST import CONST
from modules.MyLog import MyLog


def CreateFolderData():
    MyLog.info(f"CreateFolderData: Tạo folder data\nCreateFolderData: {CONST.DATA_FOLDER}")
    if not os.path.exists(CONST.DATA_FOLDER):
        os.makedirs(CONST.DATA_FOLDER, exist_ok=True)
