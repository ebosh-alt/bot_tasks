import datetime
from collections import namedtuple

from SQLite import Sqlite3_Database
from Enum_classes import Flags


class User:
    def __init__(self, id, **kwargs):
        """id: int status: bool referral_link: str referral_boss_id: int referral_status_id: int firstname: str lastname: str patronymic: str document_id: int country_id: int registration_date: int full_registered: bool username: str payment_method_id: int withdrawal_account: str balance: int earnings: int count_no_verified: int count_verified_paid: int count_verified_rejected: int flag: int bot_message_id: int delete_message_id: int earnings_on_reff: int """
        self.id: int = id
        if len(kwargs):
            self.status: bool = kwargs["status"]
            self.referral_link: str = kwargs["referral_link"]
            self.referral_boss_id: int = kwargs["referral_boss_id"]
            self.referral_status_id: int = kwargs["referral_status_id"]
            self.registration_date: float = kwargs["registration_date"]
            self.firstname: str = kwargs["firstname"]
            self.lastname: str = kwargs["lastname"]
            self.patronymic: str = kwargs["patronymic"]
            self.document_id: int = kwargs["document_id"]
            self.country_id: int = kwargs["country_id"]
            self.full_registered: bool = kwargs["full_registered"]
            self.username: str = kwargs["username"]
            self.payment_method_id: str = kwargs["payment_method_id"]
            self.withdrawal_account: str = kwargs["withdrawal_account"]
            self.balance: int = kwargs["balance"]
            self.earnings: int = kwargs["earnings"]
            self.count_no_verified: int = kwargs["count_no_verified"]
            self.count_verified_paid: int = kwargs["count_verified_paid"]
            self.count_verified_rejected: int = kwargs["count_verified_rejected"]
            self.flag: Flags = Flags(kwargs["flag"])
            self.bot_message_id: int = kwargs["bot_message_id"]
            self.delete_message_id: int = kwargs["delete_message_id"]
            self.earnings_on_reff = kwargs["earnings_on_reff"]

        else:
            self.status: bool = True
            self.referral_link: str = ""
            self.referral_boss_id: int = 0
            self.referral_status_id: int = 0
            self.firstname: str = ""
            self.lastname: str = ""
            self.patronymic: str = ""
            self.document_id: int = 0
            self.country_id: int = 0
            self.registration_date: int = 0
            self.full_registered: bool = False
            self.username: str = ""
            self.payment_method_id: int = 0
            self.withdrawal_account: str = ""
            self.balance: int = 0
            self.earnings: int = 0
            self.count_no_verified: int = 0
            self.count_verified_paid: int = 0
            self.count_verified_rejected: int = 0
            self.flag: Flags = Flags.NONE
            self.bot_message_id: int = 0
            self.delete_message_id: int = 0
            self.earnings_on_reff: int = 0

    def __iter__(self):
        dict_class = self.__dict__
        Result = namedtuple("Result", ["name", "value"])
        for attr in dict_class:
            if not attr.startswith("__"):
                if attr != "flag":
                    yield Result(attr, dict_class[attr])
                else:
                    yield Result(attr, dict_class[attr].value)


class Users(Sqlite3_Database):
    def __init__(self, db_file_name, table_name, *args) -> None:
        Sqlite3_Database.__init__(self, db_file_name, table_name, *args)
        self.len = self.get_keys()

    def add(self, obj: User) -> None:
        self.add_row(obj)
        self.len += 1

    def __len__(self):
        return self.len

    def __delitem__(self, key):
        self.del_instance(key)
        self.len -= 1

    def get(self, id: int) -> User | bool:
        if id in self:
            obj_tuple = self.get_elem_sqllite3(id)
            obj = User(id=obj_tuple[0],
                       status=obj_tuple[1],
                       referral_link=obj_tuple[2],
                       referral_boss_id=obj_tuple[3],
                       referral_status_id=obj_tuple[4],
                       firstname=obj_tuple[5],
                       lastname=obj_tuple[6],
                       patronymic=obj_tuple[7],
                       document_id=obj_tuple[8],
                       country_id=obj_tuple[9],
                       registration_date=obj_tuple[10],
                       full_registered=obj_tuple[11],
                       username=obj_tuple[12],
                       payment_method_id=obj_tuple[13],
                       withdrawal_account=obj_tuple[14],
                       balance=obj_tuple[15],
                       earnings=obj_tuple[16],
                       count_no_verified=obj_tuple[17],
                       count_verified_paid=obj_tuple[18],
                       count_verified_rejected=obj_tuple[19],
                       flag=Flags(obj_tuple[20]),
                       bot_message_id=obj_tuple[21],
                       delete_message_id=obj_tuple[22],
                       earnings_on_reff=obj_tuple[23]
                       )
            return obj
        return False

    def get_by_username(self, username: str) -> str | None:
        answer = self.get_by_other_field(field="username", value=username, username="username")
        return answer

    def get_referral_boss(self, id: int) -> str | None:
        answer = self.get_by_other_field(field="id", value=id, username="username")
        return answer

    def get_all_balance(self):
        balance = self.get_attribute(attr="balance")
        return sum(balance)

    def get_total_earnings(self):
        total_earnings = self.get_attribute(attr="earnings")
        return sum(total_earnings)

    def get_users_by_time(self, time: int):
        ts = (datetime.datetime.utcnow() - datetime.timedelta(hours=time)).timestamp().__float__()
        conn = self.sqlite_connect()
        curs = conn.cursor()
        curs.execute(f'''SELECT id from {self.table_name} where registration_date >= {ts}''')
        answer = curs.fetchall()
        conn.close()

        return len(answer)
