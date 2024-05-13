from enum import Enum
import sys
import os


global_header_color = "D2F4FA"
global_header_position = "right"
global_pad_left = 2
global_pad_right = 2
global_pad_top = 10
global_pad_bottom = 2
global_pad_x = 3
global_pad_y = 2


class Messages(Enum):
    invalid_data = "Invalid data, check the provided data."


class GeneralStatusEnum(Enum):
    active = 1
    settled = 2
    passed_away = 3
    temp_stop = 4


class Periods:

    period_lst = [y + m for y in [str(1401 + i) for i in range(0, 4)] for m in [str(i).zfill(2) for i in range(1, 13)]]


number_to_persian_month_dict = {
    "1": "فروردین",
    "2": "اردیبهشت",
    "3": "خرداد",
    "4": "تیر",
    "5": "مرداد",
    "6": "شهریور",
    "7": "مهر",
    "8": "آبان",
    "9": "آذر",
    "10": "دی",
    "11": "بهمن",
    "12": "اسفند"
}


if getattr(sys, 'frozen', False):
    not_allowed_to_save_dir = sys._MEIPASS
else:
    not_allowed_to_save_dir = os.path.abspath(os.getcwd() + "\\..")



