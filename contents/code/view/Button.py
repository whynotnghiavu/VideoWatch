from view.UseCase import UseCase
from view.THEMES import THEMES


class Button():
    button_themes = {
        UseCase.XoaManHinh: THEMES.DRACULA,

        UseCase.ChonThuMuc: THEMES.DRACULA,
        UseCase.MoThuMuc: THEMES.DRACULA,
        UseCase.GhiThongTin: THEMES.DRACULA,

        UseCase.MoVideo: THEMES.DARK_BLUE,
        UseCase.MoGhiChu: THEMES.DARK_BLUE,

        UseCase.XemVideoTruoc: THEMES.DRACULA,
        UseCase.XemVideoSau: THEMES.DARK_BLUE,

        UseCase.HopNhatFileNote: THEMES.DRACULA,
        UseCase.HopNhatFileSub: THEMES.DRACULA,


        UseCase.ThoatChuongTrinh: THEMES.EXIT,
    }
