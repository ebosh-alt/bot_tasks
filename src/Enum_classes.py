from enum import Enum


class Flags(Enum):
    NONE = 0


class Admin_flags(Enum):
    NONE = 0
    input_user_by_statistic = 1


class Reminder(Enum):
    NONE = 0
    first_reminder = 1
    second_reminder = 2
    third_reminder = 3
    fourth_reminder = 4
