from modules.MyLog import MyLog
from modules.CreateFolderData import CreateFolderData
from view.app import app


if __name__ == "__main__":
    MyLog.title("Bắt đầu chương trình")
    CreateFolderData()
    app()
