from project.table.table import Table


class OutsideTable(Table):
    TABLE_TYPE_RANGE = (51, 101)

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    def free_table_info(self):
        return Table.free_table_info(self)


if __name__ == "__main__":
    pass
