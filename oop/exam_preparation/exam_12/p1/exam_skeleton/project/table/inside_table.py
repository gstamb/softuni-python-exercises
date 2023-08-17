from project.table.table import Table


class InsideTable(Table):

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def TABLE_TYPE_RANGE(self):
        return range(1, 51)


if __name__ == "__main__":
    pass
