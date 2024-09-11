import os


from modules.CONST import CONST


def CreateFolderData():
    if not os.path.exists(CONST.DATA_FOLDER):
        os.makedirs(CONST.DATA_FOLDER, exist_ok=True)
