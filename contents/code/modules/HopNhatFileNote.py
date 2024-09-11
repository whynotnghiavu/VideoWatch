import os


from modules.CONST import CONST
from modules.MyFile import MyFile


from modules.FileRootDirReader import FileRootDirReader
from modules.RemoveRootDirPath import RemoveRootDirPath
from modules.MyExecute import MyExecute


def HopNhatFileNote():
    root_dir = FileRootDirReader()
    note_files = MyFile.TimKiem(root_dir, CONST.NOTE)
    notes = []

    for note_file in note_files:
        with open(note_file, "r", encoding="utf-8") as file:
            contents = file.read()
        if contents != f"<!--{RemoveRootDirPath(note_file)}-->\n\n\n\n":
            notes.append(contents)

    with open(os.path.join(root_dir, CONST.ALL_FILE_NOTES), "w", encoding="utf-8") as all_file_notes:
        for note in notes:
            all_file_notes.write(f"{note}\n")

    MyExecute(f" code")
    MyExecute(f" code {os.path.join(root_dir, CONST.ALL_FILE_NOTES)}")
