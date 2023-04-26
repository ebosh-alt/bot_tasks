from collections import namedtuple
from SQLite import Sqlite3_Database


class Document:
    def __init__(self, id, **kwargs):
        self.id: int = id
        if len(kwargs):
            self.name = kwargs["name"]

        else:
            self.name: str = ""

    def __iter__(self):
        dict_class = self.__dict__
        Result = namedtuple("Result", ["name", "value"])
        for attr in dict_class:
            if not attr.startswith("__"):
                if attr != "flag":
                    yield Result(attr, dict_class[attr])
                else:
                    yield Result(attr, dict_class[attr].value)


class Documents(Sqlite3_Database):
    def __init__(self, db_file_name, table_name, *args) -> None:
        Sqlite3_Database.__init__(self, db_file_name, table_name, *args)
        self.len = 0

    def add(self, obj: Document) -> None:
        self.add_row(obj)

    def get(self, id: int) -> Document | bool:
        if id in self:
            obj_tuple = self.get_elem_sqllite3(id)
            obj = Document(
                id=obj_tuple[0],
                name=obj_tuple[1]
            )
            return obj
        return False


