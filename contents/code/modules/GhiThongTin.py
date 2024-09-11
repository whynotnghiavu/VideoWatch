

from modules.CONST import CONST
from modules.MyLog import MyLog
from modules.MyFile import MyFile


from modules.FileRootDirReader import FileRootDirReader


def ThongTinFile(root_dir, extensions):
    type = ""
    count = 0
    for i in extensions:
        type += f" {i} "
        count += MyFile.SoLuong(root_dir, f"{i}")
    if count:
        print(f'\033[32m[{type} = {count}]\033[39m', end=" ")
    else:
        print(f'[{type} = {count}]', end=" ")


def GhiThongTin():
    root_dir = FileRootDirReader()

    MyLog.title(root_dir)
    if not root_dir:
        MyLog.error("GhiThongTin: Chưa chọn thư mục")
        return

    ThongTinFile(root_dir, [CONST.MP4])
    ThongTinFile(root_dir, [CONST.SRT])
    ThongTinFile(root_dir, [CONST.MP4, CONST.SRT])
    print()
