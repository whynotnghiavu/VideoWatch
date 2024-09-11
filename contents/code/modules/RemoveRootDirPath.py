

from modules.FileRootDirReader import FileRootDirReader


def RemoveRootDirPath(path):
    root_dir = FileRootDirReader()
    return path.replace(root_dir, "")
