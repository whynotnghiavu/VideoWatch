from modules.MyLog import MyLog
from modules.CreateFolderData import CreateFolderData
from view.app import app


if __name__ == "__main__":
    MyLog.title("Bắt đầu chương trình")
    CreateFolderData()
    app()








# ! Chỉnh prtin ======== log
# MyLog.info(f"GhiFileCurrent: current_index\nGhiFileCurrent: {current_index}")
# đúng tên hàm nha
